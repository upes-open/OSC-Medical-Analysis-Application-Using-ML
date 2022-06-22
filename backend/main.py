from typing import Optional
from ml import predict, preprocessing
from fastapi import FastAPI, File, UploadFile
import shutil
import cv2

app = FastAPI(title="OSC-Medical-Analysis-Application-Using-ML",description="An CNN based binary classification model to classify X-Ray scans on whether they are suffering from pneumonia or not.")

@app.post("/")
async def root(file: UploadFile = File(...)):
    threshold = 0.75
    with open("tmp.jpg","wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    image = preprocessing("tmp.jpg")
    prediction = predict(image)
    options = ["Normal","Potentially Pneumonia"]
    msg = 0
    if prediction > threshold:
        msg = 1
    return {"result":  options[msg], "prediction":str(prediction)}

