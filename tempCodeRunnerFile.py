import cv2
from PIL import Image
from pytesseract import pytesseract
import requests,time


def capture_and_recognize():
    camera = cv2.VideoCapture(0)
    # The API endpoint
    url = "http://127.0.0.1:5000/vehicules/car_in_out/"
    text=""

    #tentatives
    tentative1=""
    tentative2=""

    while True:
        _, image = camera.read()
        cv2.imshow('Text detection', image)

        #Appliquer la reconnaissance de texte
        path_to_tesseract = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
        pytesseract.tesseract_cmd = path_to_tesseract
        text = pytesseract.image_to_string(Image.fromarray(image))

        print("Texte détecté : ", text[:-1]) 
        if text[:-1]:
            tentative1=str(text[:-1]).replace("\n", "").replace(" ","")
            if tentative1==tentative2:
                # matriculeFormat = tentative1.split("|");

                ## EXAMPLE OF THE MATRICULE "1234|A|1"
                # if len(matriculeFormat) == 3 and tentative1.count("|") == 2 and tentative1.index("|") == 4 and tentative1.rindex("|") == 6:
                # print("correct Format : " + matriculeFormat[1])

                # A GET request to the API
                response = requests.get(url+tentative1)

         
                print(response.status_code)

                time.sleep(5)


                
            else:
                tentative2=tentative1
                tentative1=""


# Capture et reconnaissance automatique
capture_and_recognize()
