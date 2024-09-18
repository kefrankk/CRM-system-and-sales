
from pydantic import BaseModel, EmailStr, PositiveFloat, PositiveInt
from datetime import datetime
from enum import Enum

class ProductEnum(str, Enum):
    product1 = "Product 1"
    product2 = "Product 2"
    product3 = "Product 3"



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
    quantity: PositiveInt
    product: ProductEnum
