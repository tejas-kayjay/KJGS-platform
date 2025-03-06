from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, HttpUrl
import requests

# Create a FastAPI app
app = FastAPI()

# Define a Pydantic model for the request body
class URLRequest(BaseModel):
    url: HttpUrl

@app.post("/check_url")
async def check_url(request: URLRequest):
    """
    Endpoint to check if the provided URL is reachable.
    """
    try:
        # Send a GET request to the provided URL
        response = requests.get(request.url, timeout=5)
        
        # Check if the response status code is 200 (OK)
        if response.status_code == 200:
            return {"message": "Success! The URL is reachable."}
        else:
            raise HTTPException(status_code=400, detail="The URL is not reachable.")
    except requests.RequestException as e:
        # Handle exceptions such as connection errors or timeouts
        raise HTTPException(status_code=400, detail=f"Error reaching the URL: {str(e)}")
