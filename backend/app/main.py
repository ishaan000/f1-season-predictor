from fastapi import FastAPI
from app.routers import prediction

app = FastAPI(
    title="F1 Season Predictor API",
    description="API for predicting F1 season standings and race outcomes",
    version="1.0.0",
)

# Include API routes
app.include_router(prediction.router)

@app.get("/")
async def root():
    return {"message": "Welcome to the F1 Season Predictor API!"}
