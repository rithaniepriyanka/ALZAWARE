def prediction():
    import streamlit as st
    from PIL import Image
    import numpy as np
    import joblib
    from tensorflow.keras.preprocessing import image as keras_image
    from tensorflow.keras.applications import VGG16

    import json
    from streamlit_lottie import st_lottie

    # Load the trained SVM classifier
    svm_classifier = joblib.load('C:\\Rithu\\xray\\final\\svm_classifier.joblib')

    # Load the pre-trained VGG16 model
    base_model = VGG16(weights='imagenet', include_top=False, input_shape=(224, 224, 3))

    # Define class names
    class_names = ['VeryMildDemented', 'NonDemented', 'MildDemented', 'ModerateDemented']

    def preprocess_image(img):
        img = img.resize((224, 224))
        
        # Convert the image to RGB if it's not already in RGB format
        if img.mode != "RGB":
            img = img.convert("RGB")
        
        img_array = keras_image.img_to_array(img)
        img_array = np.expand_dims(img_array, axis=0)
        img_array = img_array / 255.0  # Normalize pixel values
        return img_array

    def extract_features(img_array):
        features = base_model.predict(img_array)
        features_flat = features.reshape(features.shape[0], -1)
        return features_flat

    def classify_image(img):
        # Preprocess the input image
        img_array = preprocess_image(img)
        
        # Extract features
        img_features = extract_features(img_array)
        
        # Ensure the input data has the correct shape expected by the SVM classifier
        img_features = img_features[:, :25088]  # Truncate to the first 25088 features
        
        # Predict using the SVM classifier
        prediction = svm_classifier.predict(img_features)
        
        # Map predicted class indices to class names
        predicted_class_name = class_names[prediction[0]]
        
        # Return the predicted class name
        return predicted_class_name

    # Streamlit app
    st.title('We are here to help you out !')

    #Animation
    # Load Lottie animation
    def load_lottiefile1(filepath:str):
        with open(filepath,"r") as f:
            return json.load(f)
        
    lottie_shield = load_lottiefile1("C:\\Rithu\\xray\\final\\webpage\\templates\\shield_anim.json")

    # Display Lottie animation (shield)
    st.markdown(
        """
        <style>
        .logo-container {
            position: absolute;
            top: 10px;
            right: 10px;
            width: 100px; /* Adjust the width as needed */
            height: 100px; /* Adjust the height as needed */
        }
        </style>
        """
    , unsafe_allow_html=True)

    # Add a container div with the logo-container class
    st.markdown("<div class='logo-container'></div>", unsafe_allow_html=True)
    
    # Display the Lottie animation inside the container
    st_lottie(lottie_shield, quality="high", width=100, height=100)


    # File uploader for image input
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

    # Display the uploaded image and prediction
    if uploaded_file is not None:
        img = Image.open(uploaded_file)
        st.image(img, caption='Uploaded Image', use_column_width=True)

        # Prediction button
        if st.button('Predict'):
            predicted_class = classify_image(img)
            st.success(f'Prediction: {predicted_class}')
