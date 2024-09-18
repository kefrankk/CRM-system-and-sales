
import os
import streamlit as st
from dotenv import load_dotenv
from sqlalchemy import create_engine, text, inspect

load_dotenv()

DB_HOST = os.getenv('DB_HOST')
DB_NAME = os.getenv('DB_NAME')
DB_USER = os.getenv('DB_USER')
DB_PASS = os.getenv('DB_PASS')
DB_PORT = os.getenv('DB_PORT')

DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASS}@dcs-postgres:5432/{DB_NAME}"
engine = create_engine(DATABASE_URL)



def check_table_exists(table_name):
    inspector = inspect(engine)
    tables = inspector.get_table_names()
    return table_name in tables



def save_postgres(data):

    with engine.connect() as connection:
        if check_table_exists('sales'):
            print("A tabela 'sales' existe.")
        else:
            create_table_query = '''
                CREATE TABLE IF NOT EXISTS sales (
                    id SERIAL PRIMARY KEY,
                    email VARCHAR(255) NOT NULL,
                    date TIMESTAMP NOT NULL,
                    value NUMERIC NOT NULL,
                    quantity INTEGER NOT NULL,
                    product VARCHAR(50) NOT NULL
                );
                '''
            connection.execute(text(create_table_query))
            st.write("Tabela criada com sucesso!")


        insert_query = text(
            "INSERT INTO sales (email, date, value, quantity, product) VALUES (:email, :date, :value, :quantity, :product)"
        )
        connection.execute(insert_query, {
                'email': data.email,
                'date': data.date,
                'value': data.value,
                'quantity': data.quantity,
                'product': data.product
                       } ) 
        st.write("Data saved successfully to the database!")

        connection.commit()

        result = connection.execute(text("SELECT * FROM sales"))
        data = result.fetchall()
        for row in data:
            st.write(row)


