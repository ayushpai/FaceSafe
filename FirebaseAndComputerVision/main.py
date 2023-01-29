import cv2
import face_recognition
from simple_facerec import SimpleFacerec

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

import yagmail

from mss import mss
from PIL import Image

# Encode faces from a folder
sfr = SimpleFacerec()
sfr.load_encoding_images("images/")

# Load Camera

TEXT = " "
cap = cv2.VideoCapture(0)

cred = credentials.Certificate(r"/Users/ayushpai/PycharmProjects/pythonProject1/service.json")
firebase_admin.initialize_app(cred)
db = firestore.client()
doc_ref = db.collection(u'detector').document(u'live')

previous_name = "no one"

while True:
    ret, frame = cap.read()

    # Detect Faces
    face_locations, face_names = sfr.detect_known_faces(frame)
    for face_loc, name in zip(face_locations, face_names):
        y1, x2, y2, x1 = face_loc[0], face_loc[1], face_loc[2], face_loc[3]

        cv2.putText(frame, name,(x1, y1 - 10), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 0, 200), 2)
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 200), 4)

    cv2.imshow("Frame", frame)


    if sfr.name != previous_name:
        print(sfr.name)
        name_update = {"name": sfr.name}
        doc_ref.update(name_update)


    previous_name = sfr.name
    key = cv2.waitKey(1)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()