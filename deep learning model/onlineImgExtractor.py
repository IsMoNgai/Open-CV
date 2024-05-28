import json
import requests
import os
import cv2
import numpy as np
import requests
from io import BytesIO

# Load the JSON file
with open('the-simpsons-characters-dataset-metadata.json', 'r') as file:
    data = json.load(file)

# Extract image URLs from the JSON data
image_urls = ['https://storage.googleapis.com/kagglesdsdata/datasets/1408/27569/simpsons_dataset/abraham_grampa_simpson/pic_0005.jpg?X-Goog-Algorithm=GOOG4-RSA-SHA256&X-Goog-Credential=databundle-worker-v2%40kaggle-161607.iam.gserviceaccount.com%2F20240506%2Fauto%2Fstorage%2Fgoog4_request&X-Goog-Date=20240506T105412Z&X-Goog-Expires=345600&X-Goog-SignedHeaders=host&X-Goog-Signature=56cfade11087f4f0442e72da0ec9fe9b91d492ba1337baef49519ab8a406475f29e6df097fae1d7a01bf7842fee413a3648f0fc4c101e03ca08d883dae4fbd0ea45a1d3f1ce2965b4718b037f0394cc4e3cbd1dba10778a97befc67747ee9f23dba9e238c2fd5b9676f0338ba4f0e00267d26c76c2e83836955e9a4cd27ca84488c711b8e33cc1252d69719b2b2d871bad508c6f44d03964a250821ec2ff2771c4949623b79ea3c75b4ae40fb60c8ae6959cf3b567617912e1759d092d04200124258523b1a0d323448652769ebb9abecbc95b85c375f13455b5693e56e56fc0f526da7af6263a3fa3a4860e15260cbd67e94bfbd305517559d091035ebfd403']
for distribution in data['distribution']:
    if 'contentUrl' in distribution and 'encodingFormat' in distribution and distribution['encodingFormat'].startswith('image'):
        image_urls.append(distribution['contentUrl'])

print(len(image_urls))

for image_url in image_urls:
    response = requests.get(image_url)
    image_array = np.asarray(bytearray(response.content), dtype=np.uint8)

    image = cv2.imdecode(image_array, cv2.IMREAD_COLOR)

    cv2.imshow('Image', image)

cv2.waitKey(0)
cv2.destroyAllWindows

