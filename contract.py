
from pydantic import BaseModel, EmailStr, PositiveFloat, PositiveInt
from datetime import datetime
from enum import Enum

class ProductEnum(str, Enum): 
    """
    Enum containing the available products.
    """
    product1 = "Product 1"
    product2 = "Product 2"
    product3 = "Product 3"



class Sales(BaseModel):
    """
    Validates the data entered by the user, ensuring that the email is valid, 
    the date is in the correct format, the value is a positive float, the 
    quantity is a positive integer, and the category is one of the allowed options.

    Args:
        email (EmailStr): The email of the user.
        date (datetime): The date of the sale.
        value (PositiveFloat): The value of the sale.
        quantity (PositiveInt): The quantity of the sale.
        product (ProductEnum): The product of the sale.
    """
       
    email: EmailStr
    date: datetime 
    value: PositiveFloat
    quantity: PositiveInt
    product: ProductEnum
