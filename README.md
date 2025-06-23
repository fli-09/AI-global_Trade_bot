AI-global_Trade_bot

Overview

The AI-global_Trade_bot is an advanced Python-based application designed to streamline global trade analysis and management. This project leverages artificial intelligence to automate tasks such as FAQ database creation, trade data processing, and user feedback analysis. Developed as part of an internship project, it aims to provide a robust tool for trade professionals and enthusiasts to enhance decision-making and operational efficiency.

Features





FAQ Database Management: Utilizes create_faq_database.py to generate and maintain a comprehensive FAQ database stored in faq_database.csv, aiding in quick access to trade-related information.



Data Processing: Processes trade and feedback data from faq_database.csv and feedback.csv, enabling detailed analytics and insights.



Main Application: The core script app.py serves as the entry point, orchestrating bot functionalities and user interactions.



Testing and Validation: Includes test.py for unit testing and validation of the bot's features.



Documentation: Provides requirements.txt for dependency management, trade_glossary.txt and wto_faq.txt for reference, and cbp_faq.txt and dgft_qa.txt for additional trade-related FAQs.



Development Tools: Incorporates vs.BuildTools.exe for build and development support.

Installation

Prerequisites





Python 3.8 or higher



Git (for cloning the repository)



Internet connection (for installing dependencies)

Steps





Clone the Repository: Open a terminal and run:

git clone https://github.com/fli-09/AI-global_Trade_bot.git
cd AI-global_Trade_bot



Set Up a Virtual Environment (Recommended): Create and activate a virtual environment to avoid dependency conflicts:

python -m venv venv
venv\Scripts\activate  # On Windows
source venv/bin/activate  # On macOS/Linux



Install Dependencies: Install the required Python packages listed in requirements.txt:

pip install -r requirements.txt



Configure Environment Variables:





Create a .env file in the project root (ensure it’s added to .gitignore to avoid committing sensitive data).



Add necessary API keys or configuration settings, e.g.:

API_KEY=your_api_key_here
DB_PATH=faq_database.csv



Run the Bot: Execute the main application script:

python app.py

Usage





Interactive Mode: Run app.py to interact with the bot via command-line inputs for trade queries or feedback submission.



Batch Processing: Use create_faq_database.py with command-line arguments to update the FAQ database (e.g., python create_faq_database.py --update).



Testing: Run tests to validate functionality:

python test.py

Project Structure





env/: Virtual environment directory (optional, created during setup).



.gitignore: Specifies files to exclude from version control (e.g., .env).



app.py: Main bot application script.



create_faq_database.py: Script to create and update the FAQ database.



faq_database.csv: Primary database file for FAQs.



feedback.csv: Stores user feedback data.



requirements.txt: Lists Python dependencies.



test.py: Unit tests for the project.



trade_glossary.txt, wto_faq.txt, cbp_faq.txt, dgft_qa.txt: Documentation and reference files.



vs.BuildTools.exe: Build tools for development (optional).



README.md: This file, providing project documentation.

Contributing

This project welcomes contributions! To contribute:





Fork the repository.



Create a new branch (git checkout -b feature-branch).



Make your changes and commit them (git commit -m "Describe your changes").



Push to the branch (git push origin feature-branch).



Open a pull request on GitHub.

For bug reports or feature requests, please use the GitHub Issues tab.

License

This project is currently unlicensed. Consider adding a license (e.g., MIT, Apache 2.0) by creating a LICENSE file. For now, contact the maintainer for usage permissions.

Acknowledgments





Developed during an internship with guidance from mentors.



Utilizes open-source tools and libraries listed in requirements.txt.
