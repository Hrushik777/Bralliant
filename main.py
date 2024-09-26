import cv2
import os
from datetime import datetime
from text_reader import read_text_from_image
from text_handler import save_text_to_file


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
            image_path = f"images\\{timestamp}.jpg"
            text_path = f"texts\\{timestamp}.txt"

            cv2.imwrite(image_path, frame)
            print(f"Image saved as {timestamp}.jpg")

            text = read_text_from_image(image_path)
            save_text_to_file(text_path, text)
            

        elif key == ord('q'):
            print("Exiting...")
            break

    cam.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    capture_and_process()