from flask import Flask, render_template,request
from tensorflow import keras
from tensorflow.keras.preprocessing import image
import numpy as np
from PIL import Image

app = Flask(__name__)
model = keras.models.load_model('Pneumonia_Classification_Model.h5')

@app.route('/')
def index():
    return render_template("index.html", name="Tariq")


@app.route('/prediction', methods=["POST"])
def prediction():
    img = request.files['img']
    img.save('img.jpg')

    img = image.load_img("img.jpg", target_size=(224,224))
    x=image.img_to_array(img) / 255
    resized_img_np = np.expand_dims(x,axis=0)
    prediction = model.predict(resized_img_np)
    

    p1=1-prediction
    if prediction>p1:
        pred="Covid-19 Positive"
    else:
        pred="Normal"    


    return render_template("prediction.html", data=pred)


if __name__ =="__main__":
    app.run(debug=True)