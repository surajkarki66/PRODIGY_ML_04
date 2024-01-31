import cv2

def preprocess_image(image):
    img = cv2.resize(image, (150, 150))
    # Convert the frame to grayscale
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # Normalize the pixel values
    img = img / 255
    # Reshape the frame to (1, 150, 150, 1)
    img = img.reshape((1, 150, 150, 1))

    return img

def load_image(image_path):
    img = cv2.imread(image_path)
    if img is None:
        print(f"The image at '{image_path}' does not exist.")
        exit(1)

    return img
    