from fastapi import APIRouter

router = APIRouter()


# Get user profile
@router.get("/{user_pk}")
async def profile():
    return {"message": "Hello World"}
