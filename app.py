
import streamlit as st
from contract import Sales
from datetime import datetime, time
from pydantic import ValidationError

def main():

    st.title("CRM System and Sales")

    email       = st.text_input("Seller's Email")
    s_date      = st.date_input("Date of Sale", datetime.now())
    s_time      = st.time_input("Time of Sale", time(9, 0))
    value       = st.number_input("Sale Value", min_value=0.0)
    n_products   = st.number_input("Number of Products Sold", min_value=1, step=1)
    category    = st.selectbox("Category of Product Sold", ["Category 1", "Category 2", "Category 3"])

    if st.button("Save"):
        try:
            date_time = datetime.combine(s_date, s_time)

            sale = Sales(
                    email = email,
                    date = date_time,
                    value = value,
                    n_products = n_products,
                    category = category
                )
            
            st.write(sale)

        except ValidationError as e:
            st.error(f"Error {e}")

        

if __name__ == "__main__":
    main()