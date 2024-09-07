import cv2
import easyocr
import os
import subprocess
from datetime import datetime

reader = easyocr.Reader(['en'])

def capture_and_process():

    os.makedirs("./images/", exist_ok=True)
    os.makedirs("./texts/", exist_ok=True)

    cam = cv2.VideoCapture(0)
    if not cam.isOpened():
        print("Could not open camera.")
        return

    while True:

        ret, frame = cam.read()
        if not ret:
            print("Error: Could not capture frame.")
            break
        cv2.imshow('Frame', frame)

        key = cv2.waitKey(1) & 0xFF

        if key == ord(' '):
            timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            image_path = f"./images/{timestamp}.jpg"

            cv2.imwrite(image_path, frame)
            print(f"Image saved as {timestamp}.jpg")

            text = read_text_from_image(image_path)
            text_path = f"./texts/{timestamp}.txt"
            with open(text_path, 'w') as file:
                file.write(text)
            print(f"Text saved as {timestamp}.txt")
            open_file(text_path)

        elif key == ord('q'):
            print("Exiting...")
            break

    cam.release()
    cv2.destroyAllWindows()

def read_text_from_image(image_path):
    image = cv2.imread(image_path)
    if image is None:
        print("Error: Could not read the image.")
        return ""

    result = reader.readtext(image)
    text = "\n".join([text for _, text, _ in result])
    return text

def open_file(file_path):
    if os.name == 'nt':  # Windows
        os.startfile(file_path)
    elif os.uname().sysname == 'Darwin':  # macOS
        subprocess.Popen(['open', file_path])
    else:  # Linux
        subprocess.Popen(['xdg-open', file_path])

if __name__ == "__main__":
    capture_and_process()
