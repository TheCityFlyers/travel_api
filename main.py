from fastapi import FastAPI
from search.flight.app.main import app as flight_app

app = FastAPI(
    title="Travel API",
    description="API for flight, hotel, and other travel services",
    version="1.0.0"
)

# Include the flight search router
app.mount("/search/flight", flight_app)

# Root endpoint
@app.get("/")
async def root():
    return {
        "message": "Welcome to Travel API",
        "version": "1.0.0",
        "docs_url": "/docs"
    }