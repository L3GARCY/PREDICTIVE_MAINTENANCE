import pickle
import pymongo
from pipeline import final


client = pymongo.MongoClient("mongodb://localhost:27017/")  
db = client["Timed"]  
collection = db["result"]  

with open("rf_classifier.pkl", "rb") as f:
    classifier = pickle.load(f)

def predict():
    df = final()
    prediction = classifier.predict(df)
    df["failure"] = prediction
    collection.insert_many(df.to_dict("records"))

predict()

