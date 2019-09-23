from Class.person_cloud import PersonCloud
from Class.packet import Packing
from Class.azure import Azure
from Class.neural_class import Utils
import face_recognition
import cv2
import numpy as np


class Neural:
    def __init__(self):
        self.person_cloud = PersonCloud()
        self.packing = Packing()
        self.utils = Utils()
        self.fileName = ["personGroup.pckl", "personModel.pckl"]
        self.personGroup = None
        self.personModel = None
        self.names = []
        self.unpack()
        self.videoCapture = cv2.VideoCapture(0)
        self.known_face_names = []
        self.known_face_encodings = [[0]]
        self.frame = None
        self.percent = 3
        self.state = 0
        
    def unpack(self):
        self.personGroup = self.packing.unpack(self.fileName[0])
        self.personModel = self.packing.unpack(self.fileName[1])
        self.names = []
        for person in self.personGroup:
            self.names.append(person['name'])
        print(self.personGroup)
        print(self.personModel)


    def neural_detector(self):
        face_locations = []
        face_encodings = []
        face_names = []

        frame = self.videoCapture.read()[1]
        # frame = cv2.imread('Resources/gente1.jpg')

        self.frame, isInFront = self.cropper(frame)

        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

        rgb_small_frame = small_frame[:, :, ::-1]

        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)
        color = (0, 0, 255)
        if(isInFront):
           color = (0, 255, 0)
        face_names = ["Desconocido"]
        if (len(self.personModel)):
            face_names = []
            for face_encoding in face_encodings:
                # See if the face is a match for the known face(s)
                name = "Desconocido"
                matches = face_recognition.compare_faces(self.personModel, face_encoding)
                face_distances = face_recognition.face_distance(self.personModel, face_encoding)
                print(self.personModel,matches,face_distances)
                best_match_index = np.argmin(face_distances)
                if matches[best_match_index]:
                    name = self.names[best_match_index]
                face_names.append(name)

        # Display the results
        for (top, right, bottom, left), name in zip(face_locations, face_names):
            # Scale back up face locations since the frame we detected in was scaled to 1/4 size
            top *= 4
            right *= 4
            bottom *= 4
            left *= 4

            cv2.rectangle(frame, (left, top), (right, bottom), color, 2)
            cv2.rectangle(frame, (left, bottom - 35),(right, bottom), color, cv2.FILLED)
            font = cv2.FONT_HERSHEY_DUPLEX
            cv2.putText(frame, name, (left + 6, bottom - 12),font, 0.7, (255, 255, 255), 1)

        # Display the resulting image
        return [frame, isInFront]

    def cropper(self, frame):
        frame_area = frame.shape[0]*frame.shape[1]
        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
        person_loc = face_recognition.face_locations(small_frame)
        person_loc.sort(key=self.utils.sortLocation, reverse=False)
        # print(person_loc)
        if(len(person_loc)):  # detecta si hay personas
            # print("Person detect: {}".format(len(person_loc)))
            people, areas = self.utils.setDictionary(person_loc)
            for person in person_loc:
                t, r, b, l = self.utils.increase(list(np.asarray(person)*4))
                # recortar imagenes image[y:y+h, x:x+w]

            # ordena las caras de mayor a menor detectadas en el frame
            # people.sort(key=self.utils.sortDictionary, reverse=True)
            # encuentra la cara mas grande
            person_location = person_loc[np.argmax(areas)]
            people = people[np.argmax(areas)]
            # top, rigth, bottom, left (t,r,b,l)
            t, r, b, l = self.utils.increase(list(np.asarray(person_location)*4))
            percent = max(areas)*100/float(frame_area)
            # print(percent)
            if(percent >= self.percent):
                # recortar imagenes image[y:y+h, x:x+w]
                return [frame[t:b, l:r], True]

        return [frame, False]

    def neural_recognition(self, name):
        self.state = 1 #trabajando en la caracterizacion
        person = self.person_cloud.detectPerson(self.frame)
        if(len(person)):
            person = person[0]
            face_encodings = face_recognition.face_encodings(self.frame)
            if(len(face_encodings)):
                print(person)
                print(face_encodings)
                self.personModel.append(face_encodings[0])
                person["name"] = name
                # print ("person ATTRIBUTES{}".format(person))
                self.personGroup.append(person)
                print(self.personGroup)
                self.packing.pack(self.personGroup, self.fileName[0])
                self.packing.pack(self.personModel, self.fileName[1])
                self.unpack()
        self.state = 0 #caracterizacion finalizada
        return person

