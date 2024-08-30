import psycopg2
from psycopg2 import Error

DATABASE_CONNECTION_STRING = "postgresql://parth:parth@localhost:5432/company_details"

def fetch_company_data():
    try:
        connection = psycopg2.connect(DATABASE_CONNECTION_STRING)
        cursor = connection.cursor()
        cursor.execute(""" SELECT company_id,company_linkedin_url FROM company_data """)
        data = cursor.fetchall()
        connection.close()
        return data
    except Error as e:
        raise Exception(f"Failed to fetch company data: {e}")