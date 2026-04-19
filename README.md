# Telegram CTI Crawler

This repository contains a complete Telegram CTI crawler project. It includes all necessary components for extracting indicators of compromise (IOCs) from Telegram using the Telethon library. This project is organized into a FastAPI backend and a React frontend dashboard, along with various integrations and configurations.

## Project Structure

```plaintext
cyberhawk-telegram-crawler/
├── backend/
│   ├── main.py                  # FastAPI application entry point
│   ├── models.py                # PostgreSQL models
│   ├── tasks.py                 # Celery worker tasks
│   ├── crawler.py               # Telethon crawler logic
│   ├── ioc_extraction.py        # IOC extraction methods
│   ├── requirements.txt          # Python dependencies
│   └── Dockerfile                # Docker container configuration for backend
│
├── frontend/
│   ├── src/
│   │   ├── App.js              # Main React application
│   │   ├── dashboard.js          # Dashboard component
│   │   └── index.js             # Entry point for React
│   ├── package.json              # Node.js dependencies
│   └── Dockerfile                # Docker container configuration for frontend
│
├── docker-compose.yml           # Docker Compose file for the entire application
└── README.md                    # Project overview and setup instructions
```

## Backend Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/rudraverma/cyberhawk-telegram-crawler.git
   cd cyberhawk-telegram-crawler/backend
   ```

2. Create a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Set up your PostgreSQL database and configure settings in `models.py`.

5. Start the FastAPI application:

   ```bash
   uvicorn main:app --host 0.0.0.0 --port 8000
   ```

## Frontend Setup

1. Navigate to the frontend directory:

   ```bash
   cd frontend
   ```

2. Install dependencies:

   ```bash
   npm install
   ```

3. Start the React application:

   ```bash
   npm start
   ```

## Running with Docker

1. Ensure Docker and Docker Compose are installed.

2. Run the following command in the root directory:

   ```bash
   docker-compose up --build
   ```

This will build and start both the backend and frontend services.

## Features

- **Telethon Crawler**: A powerful tool to extract data from Telegram channels.
- **IOC Extraction**: Extract indicators of compromise using specified patterns.
- **Keyword Matching**: Match messages against specified keywords to identify relevant content.
- **Elasticsearch Integration**: Store extracted data in Elasticsearch for easy search and analysis.
- **Celery Workers**: Asynchronous task processing for long-running operations.
- **React Frontend**: A user-friendly dashboard for visualizing extracted data.

## License

This project is licensed under the MIT License.