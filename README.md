# Server KeepAlive (GitHub Actions)

A simple GitHub Actions workflow + Python script to keep a server awake by sending random requests every **5–10 minutes**.  
Useful for free-tier hosting platforms (like Render, Railway, Heroku free tier) that put your server to sleep after a period of inactivity.

---

## 🚀 How It Works
- **GitHub Actions** runs every **5 minutes**.
- The Python script waits a **random delay (5–10 minutes)** before sending a request.
- Ensures your server receives at least one request within a 15-minute inactivity window.
- Prevents the server from going into "sleep" mode.

---

## 📂 Project Structure
.
├── .github
│ └── workflows
│ └── ping.yml # GitHub Actions workflow file
├── random_request.py # Python script that sends the request
├── requirements.txt # Python dependencies
└── README.md # Project documentation
