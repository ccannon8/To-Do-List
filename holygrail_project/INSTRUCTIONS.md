# Flask Application Instructions

## Project Structure

├── app/
│ ├── init.py # Flask application initialization
│ ├── routes.py # Application routes/endpoints
│ └── models.py # Data models
├── requirements.txt # Python dependencies
└── run.py # Application entry point

## Setup Instructions

1. Create a virtual environment:

```
python3 -m venv venv
```

2. Activate the virtual environment:

```
source venv/bin/activate
```

3. Install the requirements:

```
pip install -r requirements.txt
```

4. Run the application:

```
set FLASK_APP=run.py
set FLASK_ENV=development
flask run
```

The application will be available at: `http://127.0.0.1:5000/`

## Stopping the Application

1. Press `CTRL+C` in the terminal to stop the Flask server

2. Deactivate the virtual environment:

```
deactivate
```

## Important Notes

- Always make sure your virtual environment is activated before running the application
- The development server is not suitable for production use
- Keep your `requirements.txt` updated when adding new dependencies
