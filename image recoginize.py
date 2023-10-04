import requests
import json

# IBM Cloud Visual Recognition API endpoint and API key
api_key = 'YOUR_API_KEY'
url = 'https://api.us-south.visual-recognition.watson.cloud.ibm.com/instances/YOUR_INSTANCE_ID/v3/classify?version=2018-03-19'

# Function to classify an image using IBM Cloud Visual Recognition
def classify_image(image_path):
    with open(image_path, 'rb') as image_file:
        files = {'images_file': image_file}
        headers = {'apikey': api_key}
        response = requests.post(url, files=files, headers=headers)
        return response.json()

# Example usage
if __name__ == "__main__":
    image_path = 'path_to_your_image.jpg'  # Replace with the path to your image file
    classification_result = classify_image(image_path)

    # Print the classification result
    print(json.dumps(classification_result, indent=2))
