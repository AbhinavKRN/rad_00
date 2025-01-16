from fastapi import APIRouter, HTTPException, status
from motor.motor_asyncio import AsyncIOMotorClient
from bson import ObjectId
from datetime import datetime
from typing import List

from ..models.user import UserCreate, UserUpdate, UserResponse
from ..config import MONGODB_URL, DATABASE_NAME

router = APIRouter()
client = AsyncIOMotorClient(MONGODB_URL)
db = client[DATABASE_NAME]

@router.post("/users/", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
async def create_user(user: UserCreate):
    if await db.users.find_one({"email": user.email}):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already registered"
        )
    
    user_dict = user.dict()
    user_dict["created_at"] = datetime.utcnow()
    
    result = await db.users.insert_one(user_dict)
    
    created_user = await db.users.find_one({"_id": result.inserted_id})
    created_user["id"] = str(created_user["_id"])
    
    return UserResponse(**created_user)

@router.get("/users/{user_id}", response_model=UserResponse)
async def get_user(user_id: str):
    try:
        user = await db.users.find_one({"_id": ObjectId(user_id)})
        if user:
            user["id"] = str(user["_id"])
            return UserResponse(**user)
        raise HTTPException(status_code=404, detail="User not found")
    except:
        raise HTTPException(status_code=404, detail="Invalid user ID")

@router.get("/users/", response_model=List[UserResponse])
async def list_users():
    users = []
    async for user in db.users.find():
        user["id"] = str(user["_id"])
        users.append(UserResponse(**user))
    return users

@router.put("/users/{user_id}", response_model=UserResponse)
async def update_user(user_id: str, user_update: UserUpdate):
    try:
        # Remove None values from update
        update_data = {k: v for k, v in user_update.dict().items() if v is not None}
        
        if not update_data:
            raise HTTPException(status_code=400, detail="No valid update data provided")

        result = await db.users.update_one(
            {"_id": ObjectId(user_id)},
            {"$set": update_data}
        )
        
        if result.modified_count == 0:
            raise HTTPException(status_code=404, detail="User not found")
            
        updated_user = await db.users.find_one({"_id": ObjectId(user_id)})
        updated_user["id"] = str(updated_user["_id"])
        return UserResponse(**updated_user)
    except:
        raise HTTPException(status_code=404, detail="Invalid user ID")

@router.delete("/users/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_user(user_id: str):
    try:
        result = await db.users.delete_one({"_id": ObjectId(user_id)})
        if result.deleted_count == 0:
            raise HTTPException(status_code=404, detail="User not found")
    except:
        raise HTTPException(status_code=404, detail="Invalid user ID")