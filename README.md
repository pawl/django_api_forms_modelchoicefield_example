An example of using [Django API Forms](https://github.com/Sibyx/django_api_forms) with a ModelChoiceField.

## Installation

1. Clone this repository and navigate to the directory.
1. Create virtualenv: `virtualenv .venv`
1. Activate the virtualenv: `source .venv/bin/activate`
1. Install dependencies: `pip install -r requirements.txt`
1. Initialize database schema: `python manage.py migrate`
1. Load initial data: `python manage.py loaddata myapp/fixtures/*`

## Usage

Start the back-end in your first terminal:
`python manage.py runserver`

Run this command to POST json to the api:
`curl -X POST -H "Content-Type: application/json" -d @./example.json http://localhost:8000/`
