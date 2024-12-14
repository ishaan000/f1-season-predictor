from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def root():
    return {"message": "Prediction route is working!"}
