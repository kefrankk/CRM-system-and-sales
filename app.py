
import streamlit as st

def main():

    st.title("CRM System and Sales")

    email       = st.text_input("Seller's Email")
    date        = st.date_input("Date of Sale")
    time        = st.time_input("Time of Sale")
    value       = st.number_input("Sale Value")
    n_produts   = st.number_input("Number of Products Sold", min_value=0)
    catogory    = st.selectbox("Category of Product Sold", ["Category 1", "Category 2", "Category 3"])

    if st.button("Save"):
        st.write(f"Email: {email}")
        st.write(f"Date: {date}")
        st.write(f"Time: {time}")
        st.write(f"Sales Value: $ {value}")
        st.write(f"Number of Products Sold: {n_produts}")
        st.write(f"Category: {catogory}")

        

if __name__ == "__main__":
    main()