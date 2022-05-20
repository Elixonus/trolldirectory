import os
import glob
import cv2
import matplotlib.pyplot as plt
import cvlib as cv
from PIL import Image

dirname = os.path.dirname(__file__)


def troll_directory(directory_path: str) -> None:
    image_paths = []
    for file_path in glob.iglob(directory_path + "**/*.png", recursive=True):
        image_paths.append(file_path)
    for file_path in glob.iglob(directory_path + "**/*.jpg", recursive=True):
        image_paths.append(file_path)
    for file_path in glob.iglob(directory_path + "**/*.jpeg", recursive=True):
        image_paths.append(file_path)
    for file_path in glob.iglob(directory_path + "**/*.gif", recursive=True):
        image_paths.append(file_path)
    for i, image_path in enumerate(image_paths):
        troll_image(image_path)
        print(f"Trolled {(i + 1)} out of {len(image_paths)}\r")


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


print(r"""
  _____    ____    U  ___ u   _       _      
 |_ " _|U |  _"\ u  \/"_ \/  |"|     |"|     
   | |   \| |_) |/  | | | |U | | u U | | u   
  /| |\   |  _ <.-,_| |_| | \| |/__ \| |/__  
 u |_|U   |_| \_\\_)-\___/   |_____| |_____| 
 _// \\_  //   \\_    \\     //  \\  //  \\  
(__) (__)(__)  (__)  (__)   (_")("_)(_")("_) 
""")

directory = input("Directory to troll: ")
print(f"You sure you want to troll directory? {os.path.abspath(directory)}")
while True:
    do = input("Sure? [Y][N]: ")
    if do.upper() == "YES" or do.upper() == "Y":
        break
    elif do.upper() == "NO" or do.upper() == "N":
        quit()
    else:
        continue
print()

troll_directory(directory)