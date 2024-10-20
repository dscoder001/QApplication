
# QA with Documents (Information Retrieval)

This project provides a Streamlit-based web application where users can upload documents (like PDFs) and ask questions related to the document's content. The system uses Natural Language Processing (NLP) models, embeddings, and vector search to find and present the relevant information from the document.

---

## Table of Contents
- [Features](#features)
- [Folder Structure](#folder-structure)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Project Overview](#project-overview)
  - [Data Ingestion](#data-ingestion)
  - [Embedding](#embedding)
  - [Model API](#model-api)
  - [Streamlit Web App](#streamlit-web-app)
- [License](#license)

---

## Features

- Upload PDF or text documents.
- Ask questions based on the content of the uploaded document.
- Retrieves answers using embeddings and vector search.
- Simple, user-friendly interface built using Streamlit.

---

## Folder Structure

The folder structure for the project is as follows:

```bash
QAPPLICATION/
│
├── QApplication/
│   ├── __pycache__/
│   ├── .vscode/
│   ├── Data/                     # Holds your document files
│   │   └── MLDOC.txt
│   ├── Experiments/              # Jupyter notebooks for testing
│   │   └── experiment.ipynb
│   ├── notebook/                 # Additional notebooks for testing
│   │   └── book.ipynb
│   ├── QAWithPDF/                # Core logic for document processing
│   │   ├── __init__.py
│   │   ├── data_ingestion.py
│   │   ├── embedding.py
│   │   ├── model_api.py
│   ├── storage/                  # Vector storage for embeddings
│   │   ├── default_vector_store.json
│   │   ├── docstore.json
│   │   ├── graph_store.json
│   │   ├── index_store.json
│   ├── logs/                     # Stores log files
│   ├── .venv/                    # Virtual environment for the project
│   ├── StreamlitApp.py           # Streamlit app for the interface
│   ├── setup.py                  # Setup for packaging the app
│   └── custom_logger.py          # Logger setup for the project
├── requirements.txt              # Python dependencies
├── .gitignore                    # Ignore unnecessary files in version control
├── .env                          # Environment variables
└── README.md                     # This readme file
```

---

## Prerequisites

Before running the project, make sure you have the following installed:

- Python 3.x
- [Streamlit](https://streamlit.io/)
- [llama_index](https://github.com/jerryjliu/llama_index) (or any NLP package you're using)
- Virtual environment setup tool (e.g., `virtualenv`)

---

## Installation

Follow the steps below to set up the project locally:

1. **Clone the repository:**

   ```bash
   git clone https://github.com/your-username/QA-with-Documents.git
   cd QA-with-Documents
   ```

2. **Set up the virtual environment:**

   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install the required dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables:**

   Create a `.env` file in the root directory and set your necessary keys (such as the Google API key if you're using one):

   ```bash
   GOOGLE_API_KEY=your_google_api_key
   ```

---

## Usage

1. **Run the Streamlit app:**

   To start the application, run:

   ```bash
   streamlit run StreamlitApp.py
   ```

   This will launch the Streamlit web application in your default browser.

2. **Using the application:**

   - Upload a document (PDF or text file).
   - Type in your question in the input field.
   - Click "Submit & Process" to get the answer based on the content of the uploaded document.

---

## Project Overview
![QA with Documents Interface](./screenshots/Screenshot_117.png)
![Document Upload Example](./screenshots/Screenshot_119.png)

This project involves three main components:

### Data Ingestion

- **File:** `QAWithPDF/data_ingestion.py`
- **Purpose:** 
  - Loads and processes PDF or text documents from the specified folder.
  - Uses `SimpleDirectoryReader` to read the documents.
  
### Embedding

- **File:** `QAWithPDF/embedding.py`
- **Purpose:** 
  - Creates embeddings of the document using the `GeminiEmbedding` model.
  - Persists the embeddings for efficient similarity-based queries.

### Model API

- **File:** `QAWithPDF/model_api.py`
- **Purpose:**
  - Loads and configures the `Gemini-Pro` NLP model using the Google Generative AI API.
  - Handles the natural language processing for question-answering.

### Streamlit Web App

- **File:** `StreamlitApp.py`
- **Purpose:**
  - Provides an easy-to-use web interface for document uploading and question-answering.
  - Communicates with the backend models to process documents and fetch answers.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.

---

This `README.md` file provides a comprehensive overview of your project and serves as a useful guide for users or contributors who want to understand or work with your code.

Let me know if you need any further modifications!
