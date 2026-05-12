import tensorflow
from flask import Flask, request, render_template
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np


app = Flask(__name__)

# Load your trained model
model = load_model('orall_cancer_resnet50.h5')

@app.route('/', methods=['GET', 'POST'])
def upload_predict():
    if request.method == 'POST':
        image_file = request.files['image']
        if image_file:
            image_path = "./uploads/" + image_file.filename
            image_file.save(image_path)

            img = image.load_img(image_path, target_size=(224, 224))
            img_array = image.img_to_array(img)
            img_array = np.expand_dims(img_array, axis=0) / 255.0

            prediction = model.predict(img_array)
            class_name = "Cancer" if prediction[0][0] < 0.9994 else "Not Cancer"

            print(prediction[0][0])

            return render_template('index.html', prediction=class_name)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, port=5000)
