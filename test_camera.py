import cv2
from PIL import Image
from pytesseract import pytesseract
#pip install opencv-python pytesseract   
# pip install pytesseract tesseract  
#https://www.youtube.com/watch?v=t4c-WkLWH9I&ab_channel=AKPython

def capture_image():
    # Initialiser la capture vidéo à partir de la caméra par défaut (index 0)
    camera = cv2.VideoCapture(0)

    while True:
        _, image = camera.read()
        cv2.imshow('Text detection', image)
        
        # Quitter la boucle si la touche 's' est enfoncée
        if cv2.waitKey(1) & 0xFF == ord('s'):
            cv2.imwrite('test.jpg', image)
            break

    camera.release()
    cv2.destroyAllWindows()

def tesseract():
    path_to_tesseract = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
    image_path = 'test.jpg'
    pytesseract.tesseract_cmd = path_to_tesseract
    text = pytesseract.image_to_string(Image.open(image_path))
    print("text",text[:-1])

# Capturer l'image
capture_image()

# Appliquer la reconnaissance de texte
tesseract()
