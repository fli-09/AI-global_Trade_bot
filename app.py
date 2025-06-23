import streamlit as st
import pandas as pd
import requests
import os
from dotenv import load_dotenv
from googletrans import Translator
from datetime import datetime

# Load environment variables from .env file
load_dotenv()

# Hugging Face API configuration
API_TOKEN = os.getenv("HF_API_TOKEN")
if not API_TOKEN:
    st.error("Hugging Face API token not found. Please set the HF_API_TOKEN in the .env file.")
    st.stop()
API_URL = "https://api-inference.huggingface.co/models/t5-small"
headers = {"Authorization": f"Bearer {API_TOKEN}"}

# Load FAQ database
@st.cache_data
def load_faq_database():
    try:
        return pd.read_csv('faq_database.csv')
    except FileNotFoundError:
        st.error("FAQ database file (faq_database.csv) not found. Please run create_faq_database.py first.")
        st.stop()

# Initialize translator
translator = Translator()

# Feedback file setup
FEEDBACK_FILE = 'feedback.csv'
if not os.path.exists(FEEDBACK_FILE):
    pd.DataFrame(columns=['query', 'response', 'rating', 'comment', 'timestamp']).to_csv(FEEDBACK_FILE, index=False)

# Function to query Hugging Face API
def query_huggingface(payload):
    try:
        response = requests.post(API_URL, headers=headers, json=payload)
        response.raise_for_status()
        output = response.json()
        if isinstance(output, list) and len(output) > 0:
            return output[0].get('generated_text', "No response from model")
        return "Unexpected response format from API"
    except requests.exceptions.HTTPError as http_err:
        return f"HTTP error: {http_err} - Check API token or model access"
    except requests.exceptions.RequestException as req_err:
        return f"Request error: {req_err} - Check network or API endpoint"
    except ValueError as val_err:
        return f"JSON decode error: {val_err} - Invalid API response"
    except Exception as e:
        return f"General error: {str(e)} - Contact support"

# Function to find matching FAQ
def find_matching_faq(query, df):
    query_lower = query.lower()
    for index, row in df.iterrows():
        if query_lower in row['question'].lower() or row['question'].lower() in query_lower:
            return row['answer'], row['source']
    return None, None

# Function to handle multilingual query
def process_query(query, lang='en'):
    if lang != 'en':
        try:
            query = translator.translate(query, dest='en').text
        except Exception as e:
            return f"Translation error: {str(e)}"
    df = load_faq_database()
    
    # Try FAQ matching first
    answer, source = find_matching_faq(query, df)
    if answer:
        response = f"Answer from {source}: {answer}"
    else:
        # Fall back to Hugging Face model
        prompt = f"Answer the following question about international trade: {query}"
        response = query_huggingface({"inputs": prompt})
    
    # Translate response back if needed
    if lang != 'en':
        try:
            response = translator.translate(response, dest=lang).text
        except Exception as e:
            return f"Translation error: {str(e)}"
    return response

# Streamlit app
st.title("Global Trade AI Support System")
st.write("Ask your trade-related questions in any language!")

# Language selection
lang = st.selectbox("Select Language", ['en', 'es', 'fr', 'de', 'hi', 'zh-cn'], format_func=lambda x: {
    'en': 'English', 'es': 'Spanish', 'fr': 'French', 'de': 'German', 'hi': 'Hindi', 'zh-cn': 'Chinese'
}[x])

# Query input
query = st.text_input("Enter your question:")
if query:
    with st.spinner("Processing..."):
        response = process_query(query, lang)
        st.write("**Response:**")
        st.write(response)
        
        # Feedback section
        st.subheader("Feedback")
        rating = st.slider("Rate the response (1-5)", 1, 5, 3)
        comment = st.text_area("Additional comments (optional)")
        if st.button("Submit Feedback"):
            feedback = pd.DataFrame([{
                'query': query,
                'response': response,
                'rating': rating,
                'comment': comment,
                'timestamp': datetime.now()
            }])
            feedback.to_csv(FEEDBACK_FILE, mode='a', header=False, index=False)
            st.success("Feedback submitted!")

# Display feedback data (for admin view)
if st.checkbox("Show Feedback Data (Admin)"):
    feedback_df = pd.read_csv(FEEDBACK_FILE)
    st.write(feedback_df)