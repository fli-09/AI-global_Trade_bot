import pandas as pd
import re

def parse_faq_file(file_path, source):
    faqs = []
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
        # Split by question-answer pairs (assuming 'Q:' and 'A:' format)
        entries = content.split('Q:')
        for entry in entries[1:]:  # Skip first split if empty
            if 'A:' in entry:
                question, answer = entry.split('A:', 1)
                faqs.append({
                    'source': source,
                    'question': question.strip(),
                    'answer': answer.strip()
                })
    return faqs

def parse_glossary(file_path, source):
    glossary = []
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
        entries = content.split('Term:')
        for entry in entries[1:]:
            if 'Definition:' in entry:
                term, definition = entry.split('Definition:', 1)
                glossary.append({
                    'source': source,
                    'question': f"What is {term.strip()}?",
                    'answer': definition.strip()
                })
    return glossary

# Parse all files
wto_faqs = parse_faq_file('wto_faq.txt', 'WTO')
cbp_faqs = parse_faq_file('cbp_faq.txt', 'CBP')
dgft_faqs = parse_faq_file('dgft_qa.txt', 'DGFT')
glossary = parse_glossary('trade_glossary.txt', 'Glossary')

# Combine into a single DataFrame
all_faqs = wto_faqs + cbp_faqs + dgft_faqs + glossary
df = pd.DataFrame(all_faqs)

# Save to CSV
df.to_csv('faq_database.csv', index=False)
print("FAQ database created as faq_database.csv")