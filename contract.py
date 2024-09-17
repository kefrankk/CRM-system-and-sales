
from pydantic import BaseModel, EmailStr, PositiveFloat, PositiveInt
from datetime import datetime
from enum import Enum

class CategoryEnum(str, Enum):
    category1 = "Category 1"
    category2 = "Category 2"
    category3 = "Category 3"



class Sales(BaseModel):
    """
    Sales data model
    
    Attributes:
    email (EmailStr): Seller's email
    date (datetime): Date of sale
    value (PositiveFloat): Value of sale
    n_products (PositiveInt): Number of products sold
    category (CategoryEnum): Category of product sold
    """
       
    email: EmailStr
    date: datetime 
    value: PositiveFloat
    n_products: PositiveInt
    category: CategoryEnum
