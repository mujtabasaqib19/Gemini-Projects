from dotenv import load_dotenv
import streamlit as st
import google.generativeai as genai
import sqlite3
import os

load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

#function to generate SQL from natural language question
def response(question, prompt):
     model = genai.GenerativeModel('gemini-pro')
     response = model.generate_content([prompt,question])
     return response.text

#function to execute SQL query on database
def read_query(sql, db):
    conn = sqlite3.connect(db)
    cur = conn.cursor()
    try:
        cur.execute(sql)
        rows = cur.fetchall()
    except sqlite3.Error as e:
        rows = [("Error", str(e))]
    conn.close()
    return rows

prompt = """
You are an expert in converting English questions to SQL query!  
The SQL database has the name EMPLOYEES and has the following columns - NAME, DEPARTMENT, SALARY, JOB_TITLE  

For example:  
1. How many employees are in the database?  
   The SQL command will be something like this: SELECT COUNT(*) FROM EMPLOYEES;  
2. Show all employees working in the Computer Science department.  
   The SQL command will be something like this: SELECT * FROM EMPLOYEES WHERE DEPARTMENT = 'Computer Science';  
3. List the names of employees who have a salary greater than 60000.  
   The SQL command will be something like this: SELECT NAME FROM EMPLOYEES WHERE SALARY > 60000;  

Note: The SQL code should not have ````sql` or any additional formatting, and the SQL keyword should always be in uppercase.
"""

st.set_page_config(page_title="SQL QUERYING")
st.header("SQL LLM App with Gemini Pro and SQLite")

#input from user
question = st.text_input("Enter your question:", key="input")

if st.button("Ask the Question"):
    if question:
        sql_query = response(question, prompt)
        st.subheader("Generated SQL Query:")
        st.code(sql_query)
        data = read_query(sql_query, "employees.db")
        
        st.subheader("Query Results:")
        if data:
            for row in data:
                st.write(row)
        else:
            st.write("No results found.")
    else:
        st.error("Please enter a question.")


    