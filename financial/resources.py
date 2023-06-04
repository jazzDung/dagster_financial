import json, sqlalchemy, smtplib, ssl

# Get email info
f = open('financial/secret/email.json')
data = json.load(f)
EMAIL_SENDER = data['sender_email']
EMAIL_PASSWORD = data['password']
f.close()

# Email authorization 
context = ssl.create_default_context() 
SMTP = smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context)

# Get database info
f = open('financial/secret/postgres.json')
data = json.load(f)
DB_URL = data['url']
f.close()

# Setup connection
engine = sqlalchemy.create_engine(DB_URL)
DB_CONNECTION = engine.connect() 
# metadata = sqlalchemy.MetaData(schema="financial_clean")

def get_query(query):
    output = DB_CONNECTION.execute(query)
    try:
        result = output.fetchall()
        return [record._asdict() for record in result]
    except:
        return True

# Airbyte connection
f = open('financial/secret/airbyte.json')
data = json.load(f)
AIRBYTE_USERNAME = data['username']
AIRBYTE_PASSWORD = data['password']
f.close()