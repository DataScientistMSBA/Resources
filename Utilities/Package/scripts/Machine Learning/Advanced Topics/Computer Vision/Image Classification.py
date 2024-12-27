# coding: utf-8



def ComingSoon():
    print("Coming Soon")
    return


# # Function



import tensorflow as tf
from tensorflow.keras.applications import MobileNetV2
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input, decode_predictions
from tensorflow.keras.preprocessing import image
import numpy as np

def Image_Classification(img_path):
    """
    Performs image classification on a single image using MobileNetV2.

    Parameters:
        img_path (str): The file path to the image.

    Returns:
        dict: A dictionary containing the top 3 predicted classes and their probabilities.
    """
    try:
        # Load the MobileNetV2 model pre-trained on ImageNet
        model = MobileNetV2(weights='imagenet')

        # Load and preprocess the image
        img = image.load_img(img_path, target_size=(224, 224))
        img_array = image.img_to_array(img)
        img_array = np.expand_dims(img_array, axis=0)
        img_array = preprocess_input(img_array)

        # Make predictions
        predictions = model.predict(img_array)

        # Decode the predictions to get human-readable labels
        decoded_predictions = decode_predictions(predictions, top=3)[0]

        # Format the predictions into a dictionary
        results = {label: float(prob) for (_, label, prob) in decoded_predictions}

        return results

    except Exception as e:
        print("An error occurred during image classification:", e)
        return None


# # Examples



Image_Classification(img_path = r'../../../Datasets/Testing/test_xml.xml')

