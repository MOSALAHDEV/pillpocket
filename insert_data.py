#!/usr/bin/python3
import pandas as pd
from sqlalchemy import create_engine
from models.medication import Medication, Base
from models.engine.db_storage import DBStorage
from sqlalchemy.orm import sessionmaker
import os


user = os.getenv("PILLPOCKET_MYSQL_USER")
passwd = os.getenv("PILLPOCKET_MYSQL_PWD")
host = os.getenv("PILLPOCKET_MYSQL_HOST")
db = os.getenv("PILLPOCKET_MYSQL_DB")
engine = create_engine(f"mysql+mysqldb://{user}:{passwd}@{host}/{db}", pool_pre_ping=True)
Session = sessionmaker(bind=engine)
session = Session()

# load excel file
file_path = "pillpocket.xlsx"
data = pd.read_excel(file_path, engine="openpyxl")

# cleaning data
medication_data = data[['Medication', 'Quantity', 'Quantity Value (RSP)']]

# loop over the data
for index, row in medication_data.iterrows():
    medication_name = row['Medication']
    quantity = row['Quantity']
    quantity_value = row['Quantity Value (RSP)']
    existing = session.query(Medication).filter_by(name=medication_name).first()
    if existing:
        existing.stock += quantity
        existing.price = quantity_value
    else:
        new_medication = Medication(name=medication_name, stock=quantity, price=quantity_value, dosage="unknown")
        session.add(new_medication)

session.commit()
session.close()
print("Data inserted successfully")
