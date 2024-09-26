import easyocr
from cv2 import imread

reader = easyocr.Reader(['en'])

def read_text_from_image(image_path):
    image = imread(image_path)
    if image is None:
        print("Error: Could not read the image.")
        return ""

    result = reader.readtext(image)
    text = "\n".join([text for _, text, _ in result])
    return text
