# Flask Cat Fact API

A simple yet fun Flask API that fetches random cat facts 🐱 from catfact.ninja
 and provides basic user info.
Perfect as a lightweight Flask demo project — simple structure, easy setup, ready for deployment to any platform (Render, Railway, Vercel, etc.).

## 🚀 Features

✅ / route – Health check endpoint

✅ /me route – Returns user info, timestamp, and a random cat fact

🧠 Uses .env for configuration

⚙️ Built with Flask + Requests

🌍 Ready for deployment (supports environment variables like PORT)


## 📁 Project Structure
```
CatAPI/
│
├── .env                # Environment variables
├── app.py              # Main Flask app
├── requirements.txt    # Python dependencies
└── README.md           # You’re here 💛
```


## 🧰 Requirements

Before running this project, ensure you have:

Python 3.8+

pip (Python package installer)

virtualenv (optional but recommended)

## ⚙️ Setup & Installation
- 1. Clone the Repository
```git clone https://github.com/wiseman-umanah/CatAPI.git
cd CatAPI
```

- 2. Create a Virtual Environment
```
python -m venv venv
source venv/bin/activate   # for Mac/Linux
venv\Scripts\activate      # for Windows
```

- 3. Install Dependencies
```pip install -r requirements.txt```

- 4. Configure Environment Variables
Create a file named .env in the project root:

```PORT=5000```

## ▶️ Running the Application

Run your Flask server:

```python app.py```


or explicitly specify environment variables:

```PORT=8080 python app.py```

Example Output:

```* Running on http://127.0.0.1:5000/```


Then visit:

``` http://127.0.0.1:5000/```
 → returns Hello World!

```http://127.0.0.1:5000/me```
 → returns your user info and a cat fact


## 🧪 Sample Response

GET /me

Response:

```json
{
  "status": "success",
  "user": {
    "email": "wisemanumanah@gmail.com",
    "name": "Wiseman Umeh",
    "stack": "Python/Flask"
  },
  "timestamp": "2025-10-19T14:15:22.354013",
  "fact": "Cats sleep for 70% of their lives."
}
```

