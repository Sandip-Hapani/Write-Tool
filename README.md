# Writer Tool Backend API

This project is a FastAPI-based backend for generating blog content, summaries, rephrased text, email drafts, taglines, blog outlines, job description hashtags, headlines, and product descriptions using OpenAI.

## Requirements

- Python 3.8+
- pip

## Setup Instructions

1. Clone the repository and open it in your terminal.
2. Create and activate a virtual environment:

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

3. Install the required packages:

```powershell
pip install -r requirments.txt
```

4. Create your environment file by copying the example file:

```powershell
Copy-Item example.env .env
```

5. Open the new .env file and set your OpenAI API key:

```env
OPENAI_API_KEY=your_openai_api_key_here
```

6. Start the application:

```powershell
python main.py
```

The API will run on http://0.0.0.0:8008.

## API Documentation

Once the server is running, you can view the interactive docs here:

- http://127.0.0.1:8008/docs

## Available Endpoints

The backend exposes endpoints such as:

- POST /v1/blog-gen
- POST /v1/rephraser
- POST /v1/summerizer
- POST /v1/email
- POST /v1/tagline
- POST /v1/blog_outline
- POST /v1/job_desc
- POST /v1/headline
- POST /v1/product_description

## Notes

- The application uses the .env file for configuration.
- If you encounter a PowerShell execution policy issue while activating the virtual environment, run:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```
