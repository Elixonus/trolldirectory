import os
import cv2
import matplotlib.pyplot as plt
import cvlib as cv

dirname = os.path.dirname(__file__)
trollface - cv2.imread(os.path.join(dirname, "images/trollface.png"))

def troll_image(image_path: str) -> None:
    image = cv2.imread(image_path)
    plt.imshow(image)
    plt.show()

    faces, confidences = cv.detect_face(image)
    # loop through detected faces and add bounding box
    for face in faces:
        startX, startY = face[0], face[1]
        endX, endY = face[2], face[3]
        # draw rectangle over face
        cv2.rectangle(image, (startX, startY), (endX, endY), (0, 255, 0), 2)
    # display output
    plt.imshow(image)
    plt.show()

trollimage("couple.jpeg")