"""
    This day's project is a face recognizer for a supposed business
    that wants to control its employees' attendance.
    It has a folder with employees' face photos and takes a picture with
    a connected camera. Then compares both photos and shows them with a text.
"""

import os
from datetime import datetime
from cv2 import cv2
import face_recognition as fr
import numpy


# default = 0.6
TOLERANCE = 0.6
PATH = "photos/employees"
EMPLOYEE_LIST = os.listdir(PATH)
photos = []
employee_names = []


def main():
    """ Main function """
    init_employees()
    encoded_photos = encode_photos(photos)
    init_camera(encoded_photos)


def init_employees():
    """
    Initializes all employees from an employee list.
    Adds every photo in the photos list.
    """
    for employee in EMPLOYEE_LIST:
        photo = cv2.imread(f"{PATH}/{employee}")
        photos.append(photo)
        employee_names.append(os.path.splitext(employee)[0])


def init_camera(encoded_photos: list):
    """
    Takes a photo with a connected camera.
    If it can't take it, returns. Else
    :param encoded_photos: a list with all encoded photos
    """
    cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    success, image = cam.read()
    if not success:
        print("Photo could not be taken.")
    else:
        face_cam = fr.face_locations(image)
        encoded_face_cam = fr.face_encodings(image, face_cam)
        for encoded_face, face_location in zip(encoded_face_cam, face_cam):
            distances = fr.face_distance(encoded_photos, encoded_face)
            coincidence_index = numpy.argmin(distances)

            if distances[coincidence_index] < TOLERANCE:
                employee_name = employee_names[coincidence_index]

                y_1, x_2, y_2, x_1 = face_location
                cv2.rectangle(image, (x_1, y_1), (x_2, y_2), (0, 255, 0), 2)
                cv2.rectangle(image, (x_1, y_2 - 35), (x_2, y_2), (255, 255, 255), cv2.FILLED)
                cv2.putText(image, employee_name, (x_1 + 6, y_2 - 6), cv2.FONT_ITALIC, 1, (0, 0, 0))

                register_attendance(employee_name)
                cv2.imshow("Web image", image)
            cv2.waitKey(0)


# Encode photos
def encode_photos(photos_to_encode: list):
    """
    Encodes every photo for a given list
    :param photos_to_encode: a list of photos
    :return: a list of the encoded photos
    """
    encoded_list = []
    for photo in photos_to_encode:
        photo = cv2.cvtColor(photo, cv2.COLOR_BGR2RGB)
        encoded_photo = fr.face_encodings(photo)[0]
        encoded_list.append(encoded_photo)
    return encoded_list


def register_attendance(employee_name):
    """
    Opens a file named "registry.csv" and adds the name and exact hour of the taken photo
    :param employee_name: a string of the employee name
    :return:
    """
    with open("registry.csv", "r+", encoding="utf-8") as file:
        registry_data = file.readlines()
        registry_names = []
        for line in registry_data:
            attendance = line.split(",")
            registry_names.append(attendance[0])
        if employee_name not in registry_names:
            now = datetime.now().strftime("%H:%M:%S")
            file.writelines(f"\n{employee_name}, {now}")
        file.close()


if __name__ == '__main__':
    main()
