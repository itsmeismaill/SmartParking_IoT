import cv2
from PIL import Image
from pytesseract import pytesseract

#pip install opencv-python pytesseract   
# pip install pytesseract tesseract  
# https://www.youtube.com/watch?v=t4c-WkLWH9I&ab_channel=AKPython

def capture_and_recognize():
    # Initialiser la capture vidéo à partir de la caméra par défaut (index 0)
    camera = cv2.VideoCapture(0)

    while True:
        _, image = camera.read()
        cv2.imshow('Text detection', image)

        # Appliquer la reconnaissance de texte
        path_to_tesseract = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
        pytesseract.tesseract_cmd = path_to_tesseract
        text = pytesseract.image_to_string(Image.fromarray(image))

        print("Texte détecté : ", text[:-1])

        # Quitter la boucle si la touche 'q' est enfoncée
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    camera.release()
    cv2.destroyAllWindows()

# Capture et reconnaissance automatique
capture_and_recognize()
