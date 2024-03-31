import numpy as np
from sklearn.metrics import classification_report
from tensorflow.keras.models import load_model
from load_dataset import load_dataset

# Load the trained model
model = load_model('model_comparison/alzheimer_classification_model.h5')

# Enter the path to your testing dataset folder here:
testing_dataset_directory = 'C:\\Rithu\\xray\\Alzheimer_s Dataset\\test'

# Load testing dataset
test_dataset, test_labels = load_dataset(testing_dataset_directory)

# Evaluate the model
loss, accuracy = model.evaluate(test_dataset, test_labels)
print("Test Loss:", loss)
print("Test Accuracy:", accuracy)

# Make predictions
predictions = model.predict(test_dataset)
predicted_labels = np.argmax(predictions, axis=1)

# Generate classification report
print("Classification Report:")
print(classification_report(test_labels, predicted_labels))
