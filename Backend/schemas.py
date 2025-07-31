from pydantic import EmailStr,BaseModel
from typing import Optional,List
from datetime import datetime
from enum import Enum

class UserRole(str, Enum):
    student = "student"
    admin = "admin"

class UserCreate(BaseModel):
    email: EmailStr
    password: str   

class UserOut(BaseModel):
    id: int
    email: EmailStr
    role: str        
    class Config:
        orm_mode = True

class CategoryOut(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True 

class BookRequest(BaseModel):
    title: str
    author: str
    category_id: int

class BookOut(BaseModel):
    id: int
    title: str
    author: str
    available_copies: int
    category: Optional[CategoryOut]

    class Config:
        orm_mode = True

class ReservationStatus(str, Enum):
    pending = "pending"
    approved = "approved"
    borrowed = "borrowed"
    returned = "returned"
    rejected = "rejected"

class ReservationRequest(BaseModel):
    book_id: int  

class ReservationOut(BaseModel):
    id: int
    user_id: int
    book_id: int
    status: ReservationStatus
    reserved_at: Optional[datetime]
    borrowed_at: Optional[datetime]
    returned_at: Optional[datetime]
    due_date: Optional[datetime]

    class Config:
        orm_mode = True

class UserWithReservations(UserOut):
    reservations: List[ReservationOut] = []


       

