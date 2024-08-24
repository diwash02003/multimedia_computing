import cv2
import os

image_path = 'payment.png'

if not os.path.exists(image_path):
    print(f"Error: File '{image_path}' not found.")
else:
    image = cv2.imread(image_path)

    if image is None:
        print(f"Error: Could not load image '{image_path}'. Check the file path and try again.")
    else:
        # Convert the color image to grayscale
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # Save the grayscale image
        cv2.imwrite('gray_image.png', gray_image)

        # Display the grayscale image
        cv2.imshow('Grayscale Image', gray_image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
