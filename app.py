import numpy as np
import tensorflow as tf

from utils import load_image, preprocess_image


if __name__ == '__main__':
    # Load the pre-trained model
    MODEL  = tf.keras.models.load_model('hand_gesture.h5')

    labels = {0: '02_l',
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
    path = str(input("Enter the valid path of an input image: "))
    img = load_image(path)
    img = preprocess_image(img)
    pred = MODEL.predict(img)[0]
    index = np.argmax(pred)
    print(labels[index])
       

    