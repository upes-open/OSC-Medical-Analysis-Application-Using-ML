# OSC-Medical-Analysis-Application-Using-ML

An CNN based binary classification model to classify X-Ray scans on whether they are suffering from pneumonia or not. It would be trained on the Kaggle dataset mentioned below and would be built with Keras and TensorFlow. The frontend would act as an interface where we would upload images for inference. It would access the model through an api built using python.

## Star ⭐ and Fork the repository to earn bonus points.

## Tech Stack

- ML: Tensorflow, Keras, NumPy, Pandas, SciKit-Learn, MatPlotlib
- Frontend: React.js, HTML, CSS, JavaScript
- Backend: FastAPI

## Data

The data originates from a [2018 Kaggle competition](https://www.kaggle.com/datasets/paultimothymooney/chest-xray-pneumonia).

The dataset is organized into 3 folders (train, test, val) and contains subfolders for each image category (Pneumonia/Normal). There are 5,863 X-Ray images (JPEG) and 2 categories (Pneumonia/Normal).

Chest X-ray images (anterior-posterior) were selected from retrospective cohorts of pediatric patients of one to five years old from Guangzhou Women and Children’s Medical Center, Guangzhou. All chest X-ray imaging was performed as part of patients’ routine clinical care.

For the analysis of chest x-ray images, all chest radiographs were initially screened for quality control by removing all low quality or unreadable scans. The diagnoses for the images were then graded by two expert physicians before being cleared for training the AI system. In order to account for any grading errors, the evaluation set was also checked by a third expert.

## The Model

The model would be a CNN built through Keras and TensorFLow, the architecture of the model is left to the contributor, it is recommended to use a combination of convolution, maxpooling, dense and dropout layer to ensure maximum accuracy and efficiency. Since it is a binary classifier, Binary cross enthropy loss function is recommended.

The current Model uses 2 Convolutional Layers and 2 Dense Layers of 64 nodes and has the following metrics
    ```loss: 5.8201e-05 - accuracy: 1.0000 - val_accuracy: 0.9505```

The Model input undergoes the following preprocessing
```python
    def preprocessing(img):
    img_array = cv2.imread( img,cv2.IMREAD_GRAYSCALE) #convert image to grayscale
    
    new_array = cv2.resize(img_array, (size, size)) #resize image

    # return image 
    return new_array/256
```
## Frontend

The frontend would be made using react. It would consist of a Form like interface where one can upload an image. The image would then be send to the backend for inference and would await a response from the backend. On recieving the prediction it would display it to the user.

## File Structure

1. The frontend folder consist of an new react app created using npx create-react-app, it will house the entire frontend that will be used to access the model.
2. The backend folder will contain the api which will receive photos send buy the frontend and perform inference in them
3. The ML Model folder will contain the Jupyter notebook used for data processing and training and the saved model.

## Repository Setup
1. Install Anaconda
2. Create a new environment using the `environment.yml` file
    ```conda env create -f environment.yml```
3. Activate the environment
    ```conda activate OSC-Medical-Analysis```

## Backend
The backend uses a simple api created using FastAPI that acceps the images as binary strings and returns the prediction in the following format
```json
    {
        "result": "Potentially Pneumonia", // or Normal
        "prediction": "95.1230" // model's prediction
    }
```

### Backend Setup
1. Navigate to the backend folder
   ```cd backend```
2. Start the server
    ```uvicorn main:app --reload```
3. Open http://localhost:8000/docs
