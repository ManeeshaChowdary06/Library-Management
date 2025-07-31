from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
import schemas, models
from ..database import get_db
from ..utils import get_password_hash  

router = APIRouter(prefix="/users", tags=["Users"])

@router.post("/", response_model=schemas.UserOut, status_code=status.HTTP_201_CREATED)
def create_user(user_in: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = db.query(models.User).filter(models.User.email == user_in.email).first()
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")

    hashed_password = get_password_hash(user_in.password)

    user = models.User(
        email=user_in.email,
        hashed_password=hashed_password,
        
        role=getattr(user_in, "role", "student")
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user
