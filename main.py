from fastapi import FastAPI
import requests

app = FastAPI()

# ThousandEyes API credentials
Bearer_TOKEN = "c5417ad7-47db-4761-917e-cde91d0d1989"


# ThousandEyes API base URL
API_BASE_URL = "https://api.thousandeyes.com/v6"

# Endpoint to retrieve all tests
@app.get("/tests")
def get_tests():
    headers = {
        "Authorization": f"Bearer {Bearer_TOKEN}"
    }
    url = f"{API_BASE_URL}/tests.json"
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return response.json()  
    else:
        return {"error": "Failed to retrieve tests."}

# Endpoint to create a test
@app.post("/tests")
def create_test(test_name: str):
    headers = {
        "Authorization": f"Bearer {Bearer_TOKEN}",
        "Content-Type": "application/json"
    }
    url = f"{API_BASE_URL}/tests"
    payload = {
        "testName": test_name,
        "interval": 300,
        "agents": [
            {
                "agentId": 1
            }
        ]
    }
    response = requests.post(url, headers=headers, json=payload)

    if response.status_code == 200:
        return response.json()
    else:
        return {"error": "Failed to create test."}
