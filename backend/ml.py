from keras.models import load_model
import cv2
size = 300

def preprocessing(img):
    img_array = cv2.imread( img,cv2.IMREAD_GRAYSCALE)
    new_array = cv2.resize(img_array, (size, size))
    return new_array/256

def predict(image):
  model = load_model("Model/2-conv-64-nodes-2-dense-1655332877.model.h5")
  input_shape = (1,300,300,1)
  a = image.reshape(input_shape)
  return model.predict(a)[0][0]
