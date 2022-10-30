import cv2
import easyocr
from flask import Flask
from flask import request

reader = easyocr.Reader(['en', "ru"])

app = Flask(__name__)


@app.route('/img_to_text', methods=['POST'])
def upload():
    try:
        request.files['image'].save("ok.png")
        img = cv2.imread("ok.png")

        imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        text = reader.readtext(image, detail=0)
        # a = reader.readtext(ok, detail=0)
        return text
    except Exception as err:
        print(str(err))
