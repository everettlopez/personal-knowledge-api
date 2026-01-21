# Personal Knowledge API 
This project is a backend system built with FastAPI, Pydantic, and uv. It’s designed to demonstrate clean API design, modern Python tooling, and real‑time development practices. The API stores “knowledge entries” (articles, notes, videos, concepts) and provides tagging, search, and analytics endpoints.

## Setup & Running Locally
1. Clone the Repo
```python
git clone https://github.com/everettlopez/personal-knowledge-api.git
cd personal-knowledge-api
```

2. Install dependencies
```python
uv sync
```

3. Start the dev server
```python
uv run fastapi dev
```