import cv2
import easyocr
from flask import Flask
from flask import request
from matplotlib import pyplot as plt
import numpy as np

reader = easyocr.Reader(['en', "ru"])

app = Flask(__name__)


@app.route('/img_to_text', methods=['POST'])
def upload():
    try:
        request.files['image'].save("ok.png")
        img = cv2.imread("ok.png")
        blur = cv2.blur(img, (2, 2))
        dst = cv2.fastNlMeansDenoisingColored(blur, None, 10, 10, 7, 21)
        thresh = 128
        img_binary = cv2.threshold(dst, thresh, 255, cv2.THRESH_BINARY)[1]

        text = reader.readtext(img_binary, detail=0)
        # a = reader.readtext(ok, detail=0)
        return text
    except Exception as err:
        print(str(err))
