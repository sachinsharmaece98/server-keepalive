import time
import random
import requests

SERVER_URL = "https://concept-management-backend.onrender.com/"  # Change this to your server endpoint

def make_request():
    try:
        response = requests.get(SERVER_URL)
        print(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] Request sent. Status: {response.status_code}")
    except Exception as e:
        print(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] Request failed: {e}")

if __name__ == "__main__":
    wait_time = random.randint(300, 600)  # 5–10 minutes
    print(f"Waiting {wait_time // 60} min {wait_time % 60} sec before sending request...")
    time.sleep(wait_time)
    make_request()
