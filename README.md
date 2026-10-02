# Economy & Crafting API

A FastAPI-based backend for managing professions, resources, items, and crafting recipes in an RPG-style economy system.

## Features

- Create and manage professions
- Create and manage resources
- Create and manage items
- Create crafting recipes
- Calculate the total resource requirements for crafting a specific quantity

## Tech Stack

- Python
- FastAPI
- SQLAlchemy
- SQLite

## Project Structure

- `main.py` - FastAPI app and routes
- `models.py` - SQLAlchemy models
- `schemas.py` - Pydantic schemas
- `services.py` - business logic
- `database.py` - database configuration

## Setup

1. Create and activate a virtual environment:
   ```bash
   python -m venv env
   source env/bin/activate   # Linux/macOS
   env\Scripts\activate      # Windows
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the application:
   ```bash
   uvicorn main:app --reload
   ```

4. Open the API docs in the browser:
   - http://127.0.0.1:8000/docs

## API Endpoints

- `POST /api/professions/`
- `POST /api/resources/`
- `POST /api/items/`
- `POST /api/recipes/`
- `GET /api/items/{item_id}`
- `GET /api/items/{item_id}/calculate-cost`

## Notes

The app uses SQLite by default and creates the database automatically on startup.
