# Web Content Q&A Tool

## Overview

It is a web-based Q&A tool that ingests content from provided URLs and allows users to ask questions based solely on the scraped website content. The answer is generated using a transformer-based question-answering model (DistilBERT fine-tuned on SQuAD). The backend is built using Flask, and a static version of the UI is hosted on Netlify.

## Live/Hosted Link to the UI

You can view the static user interface (frontend) at the following URL:

**[https://marvelous-melba-a28d2e.netlify.app](https://marvelous-melba-a28d2e.netlify.app)**

*Note:* This link hosts only the static UI. To test the full Q&A functionality—including content ingestion and model inference—please follow the instructions below to run the application locally.

## Running the Application Locally

### Prerequisites

- **Python 3.12** (or higher)
- **Git**
- An internet connection (for downloading dependencies and NLTK data)

### Setup Instructions

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/abhaybansal12/AiSensy.git
   cd Ai-Scraper
2. Create and Activate a Virtual Environment:

python3 -m venv venv
source venv/bin/activate   # On Windows, use: venv\Scripts\activate

3. Install Dependencies:

pip install -r requirements.txt

4. Run the Application:

Start the Flask development server by running:
python app.py

5. Test the Q&A Functionality:

(a)Open your web browser and navigate to http://127.0.0.1:5000.

(b)On the home page, enter one or more URLs (separated by commas or newlines) to ingest website content.

(c)Once ingestion is complete, you will be redirected to the Q&A page.

(d)Enter your question (which should be answerable based solely on the ingested content) and click "Get Answer."

(e)The answer generated by the transformer model will be displayed on the page.


Project Structure:

Ai-Scraper/
├── app.py               # Main Flask application with content ingestion and Q&A functionality

├── index.html           # Static HTML file for the UI (hosted on Netlify)

├── requirements.txt     # List of Python dependencies

├── .gitignore           # Git ignore file (excludes the venv folder, etc.)

└── README.md            # This README file


How It Works?

1. Content Ingestion
   URL Input: The user provides one or more URLs on the home page.
   Scraping: The application uses requests and BeautifulSoup to fetch and clean the text from each URL.
   Storage: The scraped text is combined and stored in a global variable for processing.
2. Text Processing and Question Answering
   Chunking: The ingested text is divided into manageable chunks (approximately 400 words per chunk) using NLTK’s sentence tokenizer with overlap to preserve context.
   QA Model: A Hugging Face transformer-based QA model (DistilBERT fine-tuned on SQuAD) processes each chunk.
   Answer Selection: The answer with the highest confidence score is selected and displayed on the Q&A page.


   

   





