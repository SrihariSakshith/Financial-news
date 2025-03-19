# Financial News Summarization and Compliance Monitoring System

This project implements a real-time financial news summarization and compliance monitoring system using Retrieval-Augmented Generation (RAG) with Pathway.

## Features

- **Real-Time Data Ingestion**: Fetch financial news from APIs and RSS feeds.
- **Efficient Storage & Indexing**: Use FAISS for real-time vector database storage and retrieval.
- **RAG Pipeline**:
  - Summarize financial news using LLMs (e.g., OpenAI).
  - Detect compliance risks by identifying regulatory mentions.
- **REST API**: Expose endpoints for summarization and compliance monitoring using FastAPI.
- **Interactive UI**: Streamlit-based interface for real-time updates, alerts, and structured reports.
- **Dockerized Deployment**: Portable and easy-to-deploy Docker setup.

## Project Structure

```
financial-news/
├── data_ingestion/
│   ├── rss_ingestor.py       # Fetch news from RSS feeds
│   ├── api_ingestor.py       # Fetch news from APIs
├── storage/
│   ├── vector_store.py       # FAISS-based vector database
├── rag_pipeline/
│   ├── summarizer.py         # Summarize news using LLMs
│   ├── compliance_monitor.py # Detect compliance risks
├── api/
│   ├── main.py               # FastAPI backend
├── ui/
│   ├── app.py                # Streamlit-based UI
├── Dockerfile                # Docker configuration
├── requirements.txt          # Python dependencies
├── config.py                 # Configuration file
└── README.md                 # Project documentation
```

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/financial-news.git
   cd financial-news
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up the configuration:
   - Update `config.py` with your RSS feed URLs, API keys, and compliance keywords.

## Usage

### Run the Backend API
Start the FastAPI server:
```bash
uvicorn api.main:app --host 0.0.0.0 --port 8000
```

### Run the UI
Start the Streamlit UI:
```bash
streamlit run ui/app.py
```

### Docker Deployment
Build and run the Docker container:
```bash
docker build -t financial-news .
docker run -p 8000:8000 financial-news
```

## API Endpoints

- **POST /summarize/**: Summarize financial news and detect compliance risks.
  - Request Body: `{"text": "Financial news text"}`
  - Response: `{"summary": "Summarized text", "risks": ["risk1", "risk2"]}`

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request.

## Acknowledgments

- [FastAPI](https://fastapi.tiangolo.com/)
- [Streamlit](https://streamlit.io/)
- [FAISS](https://github.com/facebookresearch/faiss)
- [OpenAI](https://openai.com/)
- [LangChain](https://langchain.com/)
