import os
import glob
import cv2
import matplotlib.pyplot as plt
import cvlib as cv
from PIL import Image

dirname = os.path.dirname(__file__)


def troll_directory(directory_path: str) -> None:
    image_paths = []
    for filename in glob.iglob(directory_path + "**/*.png", recursive=True):
        image_paths.append()


def troll_image(image_path: str) -> None:
    image = cv2.imread(image_path)
    faces, confidences = cv.detect_face(image)
    image = Image.fromarray(image)
    for face in faces:
        dx = int(0.2 * (face[2] - face[0]))
        dy = int(0 * (face[3] - face[1]))
        sx, sy = face[0] - dx, face[1] - dy
        ex, ey = face[2] + dx, face[3] + dy
        troll_face = Image.open(os.path.join(dirname, "images/trollface.png"))
        troll_face = troll_face.resize((ex - sx, ey - sy))
        image.paste(troll_face, (sx, sy), mask=troll_face)
    plt.imshow(image)
    plt.show()


troll_directory("")
