from typing import Optional
from ml import predict, preprocessing
from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
import shutil
import cv2

app = FastAPI(title="OSC-Medical-Analysis-Application-Using-ML",description="An CNN based binary classification model to classify X-Ray scans on whether they are suffering from pneumonia or not.")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

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

