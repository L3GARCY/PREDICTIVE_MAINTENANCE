import pymongo
import streamlit as st

client = pymongo.MongoClient("mongodb://localhost:27017/")  
db = client["Timed"] 
collection = db["result"] 

latest_record = collection.find_one(sort=[("_id", pymongo.DESCENDING)])

if latest_record:
  print("Latest record:")
  print(latest_record)  
else:
  print("No records found in the collection.")
st.title("Latest Sensor Readings")

if latest_record:
  st.text("Vibration:")
  st.write(latest_record["vibration"])
  st.text("RPM:")
  st.write(latest_record["rotate"])
  st.text("Pressure:")
  st.write(latest_record["pressure"])
  st.text("Voltage:")
  st.write(latest_record["volt"])
else:
  st.warning("No records found in the collection.")

client.close()

