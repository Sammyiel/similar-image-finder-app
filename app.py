from io import BytesIO
import cv2
import base64
from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
  # Get the uploaded image
  image_b64 = request.json['image']
  image = Image.open(BytesIO(base64.b64decode(image_b64)))

  # Get similar images
  similar_images = predict_similar_images(image)

  # Convert images to base64 format
  similar_images_b64 = []
  for image in similar_images:
    image = (image * 255).astype('uint8')
    _, image_b64 = cv2.imencode('.jpg', image)
    similar_images_b64.append(base64.b64encode(image_b64).decode())

  return jsonify({'similar_images': similar_images_b64})

if __name__ == '__main__':
  app.run(debug=True)

