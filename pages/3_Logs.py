import streamlit as st
import pandas as pd
from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["Timed"]
collection = db["result"]

# Function to fetch latest 20 records from MongoDB collection
def fetch_latest_records():
    records = collection.find().sort("_id", -1).limit(20)
    df = pd.DataFrame(records)
    return df

# Main function to run Streamlit app
def main():
    st.title("Latest 20 Records from MongoDB Collection")
    
    # Fetch latest records from MongoDB
    df = fetch_latest_records()
    
    # Display as CSV
    csv_data = df.to_csv(index=False)
    st.download_button(
        label="Download CSV",
        data=csv_data,
        file_name="latest_records.csv",
        mime="text/csv"
    )
    
    # Display the DataFrame
    st.write(df)

if __name__ == "__main__":
    main()
