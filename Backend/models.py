from sqlalchemy.ext.declarative import declarative_base
import enum
from sqlalchemy import Column,Integer,String,ForeignKey,DateTime,Enum
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

Base=declarative_base()

class UserRole(str,enum.Enum):
    student="student"
    admin="admin"

class User(Base):
    __tablename__="user"
    id=Column(Integer,primary_key=True,index=True)
    email=Column(String,nullable=False,index=True,unique=True)
    hashed_password=Column(String,nullable=False)
    role=Column(Enum(UserRole),default=UserRole.student,nullable=False)
    reservations=relationship("reservation",back_populates="user")

class Book(Base):
    __tablename__="book"
    id=Column(Integer,primary_key=True,index=True)
    title=Column(String,nullable=False)
    author=Column(String,nullable=False)
    category_id=Column(Integer,ForeignKey("category.id"),nullable=True)
    available_copies=Column(Integer,default=10)
    description=Column(String,nullable=True)
    image_url = Column(String, nullable=True)
    category = relationship("category", back_populates="books")
    reservations = relationship("reservation", back_populates="book")

class ReservationStatus(str,enum.Enum):
    pending = "pending"
    approved = "approved"
    borrowed = "borrowed"
    returned = "returned"
    rejected = "rejected"

class Reservation(Base):
    __tablename__="reservation"
    id=Column(Integer,primary_key=True,index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    book_id = Column(Integer, ForeignKey("books.id"), nullable=False)
    status = Column(Enum(ReservationStatus), default=ReservationStatus.pending, nullable=False)
    due_date = Column(DateTime(timezone=True), nullable=True)
    reserved_at = Column(DateTime(timezone=True), server_default=func.now())
    borrowed_at = Column(DateTime(timezone=True), nullable=True)
    returned_at = Column(DateTime(timezone=True), nullable=True)
    due_date = Column(DateTime(timezone=True), nullable=True)
    user = relationship("user", back_populates="reservations", foreign_keys=[user_id])
    book = relationship("book", back_populates="reservations")

class Category(Base):
    __tablename__ = "category"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, nullable=False)
    books = relationship("book", back_populates="category")

