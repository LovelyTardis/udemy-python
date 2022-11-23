"""
    This is a test file that is used to try how face_recognition and cv2 packages works.
"""
from cv2 import cv2
import face_recognition as fr

# Default = 0.6
TOLERANCE = 0.6


def main():
    """ Main function that do everything. """
    # Load photos
    control_photo = fr.load_image_file("photos/PhotoA.jpg")

    # Photo B is alike, Photo C is different
    test_photo = fr.load_image_file("photos/PhotoB.jpg")
    # test_photo = fr.load_image_file("photos/PhotoC.jpg")

    # Photos to RGB
    control_photo = cv2.cvtColor(control_photo, cv2.COLOR_BGR2RGB)
    test_photo = cv2.cvtColor(test_photo, cv2.COLOR_BGR2RGB)

    # Locate faces
    loc_a = fr.face_locations(control_photo)[0]
    loc_b = fr.face_locations(test_photo)[0]
    encoded_a = fr.face_encodings(control_photo)[0]
    encoded_b = fr.face_encodings(test_photo)[0]

    # Face rectangles
    cv2.rectangle(
        control_photo,
        (loc_a[3], loc_a[0]),
        (loc_a[1], loc_a[2]),
        (0, 255, 0),
        2
    )
    cv2.rectangle(
        test_photo,
        (loc_b[3], loc_b[0]),
        (loc_b[1], loc_b[2]),
        (0, 255, 0),
        2
    )

    # Compare photos
    result = fr.compare_faces([encoded_a], encoded_b, TOLERANCE)
    print("They are alike." if result == [True] else "They are different.")

    # Distance check
    distance = fr.face_distance([encoded_a], encoded_b)

    # Put text in the photo
    cv2.putText(
        test_photo,
        f"{result}, {distance.round(2)}",
        (50, 50),
        cv2.FONT_ITALIC,
        1,
        (255, 255, 255),
        2
    )

    # Show photos
    cv2.imshow("Control", control_photo)
    cv2.imshow("Test", test_photo)

    # Remains the program opened
    cv2.waitKey(0)


if __name__ == '__main__':
    main()
