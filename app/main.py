from fastapi import FastAPI

app = FastAPI()

@app.get("/status")
def test_status():
    """
    Test the route for FastAPI
    """
    
    return {
        "status": "ok"
    }