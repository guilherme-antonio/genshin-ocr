import cv2
import numpy as np
import easyocr

class OCR():
    def __init__(self):
        self.reader = easyocr.Reader(['en'])

    def image_processing(self, image):
        img = cv2.imread(image)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        kernel = np.ones((1, 1), np.uint8)
        img = cv2.dilate(img, kernel, iterations=1)
        img = cv2.erode(img, kernel, iterations=1)
        cv2.adaptiveThreshold(cv2.bilateralFilter(img, 9, 75, 75), 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 31, 2)
        return img

    def read(self, image):
        return self.reader.readtext(self.image_processing(image), detail= 0, width_ths= 100, height_ths=0.35)