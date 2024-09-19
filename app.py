
import streamlit as st
from contract import Sales
from datetime import datetime, time
from pydantic import ValidationError
from database import save_postgres

def main():
    """
    Main function for the CRM System.

    This function creates a Streamlit app for registering sales.
    It prompts the user for the seller's email, date of sale, time of sale, value of sale, number of products sold, and product sold.
    It then creates a Sales object with the given data and saves it to the database using save_postgres.
    If any of the inputs are invalid, it shows an error message with the validation error.
    """
    
    st.title("CRM System")

    email       = st.text_input("Seller's Email")
    s_date      = st.date_input("Date of Sale", datetime.now())
    s_time      = st.time_input("Time of Sale", time(9, 0))
    value       = st.number_input("Sale Value", min_value=0.0)
    quantity    = st.number_input("Number of Products Sold", min_value=1, step=1)
    product     = st.selectbox("Product Sold", ["Product 1", "Product 2", "Product 3"])

    if st.button("Save"):
        try:
            date_time = datetime.combine(s_date, s_time)

            sale = Sales(
                    email = email,
                    date = date_time,
                    value = value,
                    quantity = quantity,
                    product = product
                )
            
            save_postgres(sale)

        except ValidationError as e:
            st.error(f"Error {e}")
        

if __name__ == "__main__":
    main()