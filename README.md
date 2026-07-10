# Soccer Engine

A FastAPI project with a Pydantic `Player` model, player routes, and a service layer.

## Project structure

- `app/main.py` - FastAPI application entrypoint
- `app/routes/PlayerRouter.py` - player API routes
- `app/services/PlayerService.py` - player service layer
- `app/models/Player.py` - Pydantic `Player` model
- `app/utils/players_data.py` - player data store
- `Dockerfile` - container image build definition
- `docker-compose.yml` - dev/prod compose configuration
- `requirements.txt` - Python dependencies

## Installation

1. Create a virtual environment:

   python -m venv .venv
   .venv\Scripts\activate

2. Install dependencies:

   pip install -r requirements.txt

## Run locally

Start the app with Uvicorn:

uvicorn app.main:app --reload --port 8001

## Docker

Build the image:

docker build -t soccerengine .

Run the container:

docker run --rm -p 8000:8000 soccerengine

## Docker Compose

Run development profile:

docker compose --profile dev up --build

Run production profile:

docker compose --profile prod up --build

## API documentation

OpenAPI docs are available at:

- `http://127.0.0.1:8001/docs` (local)
- `http://127.0.0.1:8000/docs` (Docker)

## Endpoints

- `GET /health` - health check
- `GET /api/teams/` - list teams
- `GET /api/teams/{team_id}` - get team by id
- `POST /api/teams/` - create a team

## Player model fields

- `player_id` (integer)
- `name` (string)
- `goals` (integer)
- `passes` (integer)
- `assists` (integer)
- `shots` (integer)
- `position` (string)
- `age` (integer)
- `leagues` (list of strings)
- `matches_own` (integer)
