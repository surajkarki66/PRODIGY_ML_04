import cv2
import numpy as np
import tensorflow as tf

from utils import preprocess_image

MODEL = tf.keras.models.load_model('hand_gesture.h5')

LABELS = {0: '02_l',
          1: '04_fist_moved',
          2: '09_c',
          3: '10_down',
          4: '06_index',
          5: '08_palm_moved',
          6: '07_ok',
          7: '05_thumb',
          8: '01_palm',
          9: '03_fist'
          }

def main():
    # Set up camera
    cap = cv2.VideoCapture(0)
    # Create a window
    cv2.namedWindow("Hand Gesture Recognition")

    while True:
        # Read a frame from the camera
        ret, frame = cap.read()
        img = preprocess_image(frame)
        pred = MODEL.predict(img)[0]
        index = np.argmax(pred)
        label = LABELS[index]

        # Display the predicted label on the frame
        cv2.putText(frame, f"Gesture: {label}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

        # Display the frame
        cv2.imshow("Hand Gesture Recognition", frame)

        # Break the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the camera and close all OpenCV windows
    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()