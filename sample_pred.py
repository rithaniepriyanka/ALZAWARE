import joblib
import numpy as np
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications import VGG16

# Load the trained SVM classifier
svm_classifier = joblib.load('C:\\Rithu\\xray\\final\\svm_classifier.joblib')

# Load the pre-trained VGG16 model
base_model = VGG16(weights='imagenet', include_top=False, input_shape=(224, 224, 3))

# Define class names
class_names = ['VeryMildDemented', 'NonDemented', 'MildDemented', 'ModerateDemented']

def preprocess_image(img_path):
    img = image.load_img(img_path, target_size=(224, 224))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = img_array / 255.0  # Normalize pixel values
    return img_array

def extract_features(img_array):
    features = base_model.predict(img_array)
    features_flat = features.reshape(features.shape[0], -1)
    return features_flat

def classify_image(img_path):
    # Preprocess the input image
    img_array = preprocess_image(img_path)
    
    # Extract features
    img_features = extract_features(img_array)
    
    # Predict using the SVM classifier
    prediction = svm_classifier.predict(img_features)
    
    # Map predicted class indices to class names
    predicted_class_name = class_names[prediction[0]]
    
    # Return the predicted class name
    return predicted_class_name

# Example usage
img_path = 'C:\\Rithu\\xray\\Alzheimer_s Dataset\\pred\\2.jpg'
predicted_class = classify_image(img_path)
print("Predicted class:", predicted_class)
