import json
import sqlalchemy
import smtplib
import ssl

# Get email info
f = open('financial/secret/email.json')
data = json.load(f)
EMAIL_SENDER = (data['sender_email'])
EMAIL_PASSWORD = (data['password'])
f.close()

# Email authorization 
context = ssl.create_default_context() 
SMTP = smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context)

# Get database connection
engine = sqlalchemy.create_engine("postgresql://postgres:02092001@localhost:5432/financial_data")
DB_CONNECTION = engine.connect() 
metadata = sqlalchemy.MetaData(schema="financial_clean")

def get_query(query):
    output = DB_CONNECTION.execute(query)
    try:
        result = output.fetchall()
        return [record._asdict() for record in result]
    except:
        return True
