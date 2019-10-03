from Class.person_cloud import PersonCloud
from Class.packet import Packing
from Class.azure import Azure
from Class.neural_class import Utils
import face_recognition
import cv2
import numpy as np
from t2s import t2s

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
        print(cv2.VideoCapture())
        self.videoCapture = cv2.VideoCapture(1)
        self.known_face_names = []
        self.known_face_encodings = [[0]]
        self.frame = None
        self.percent = 13
        self.upload = 0
        self.spech = t2s()
        self.p = 1
        self.color = {"rojo":(0, 0, 255), 'verde':(0, 255, 0), 'azul':(255, 50, 50)}
        
    def unpack(self):
        self.personGroup = self.packing.unpack(self.fileName[0])
        self.personModel = self.packing.unpack(self.fileName[1])
        self.names = []
        self.ages = []
        for person in self.personGroup:
            self.names.append(person['name'])
            self.ages.append(person['faceAttributes']['age'])
        print(self.personGroup)
        print(self.personModel)


    def neural_detector(self):
        face_locations = []
        face_encodings = []
        face_names = []
        
        frame = self.videoCapture.read()[1]
        # frame = cv2.imread('Resources/gente2.jpg')


        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
        rgb_small_frame = small_frame[:, :, ::-1]
        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)
        self.frame, isInFront = self.cropper(frame,face_locations)
        frame = cv2.resize(frame, (0, 0), fx=self.p, fy=self.p)

        face_names = ["Desconocido"]*len(face_locations)
        ages = [' ']*len(face_locations)
        if (len(self.personModel)):
            face_names = []
            ages = []
            for face_encoding in face_encodings:
                # See if the face is a match for the known face(s)
                name = "Desconocido"
                age = " "
                matches = face_recognition.compare_faces(self.personModel, face_encoding)
                face_distances = face_recognition.face_distance(self.personModel, face_encoding)
                if(len(face_distances)):
                    best_match_index = np.argmin(face_distances)
                    print('List index best match :', best_match_index)
                    if matches[best_match_index]:
                        print(len(self.names))
                        name = self.names[best_match_index]
                        age = self.ages[best_match_index]
                    face_names.append(name)
                    ages.append(age)

        # Display the results
        # print(len(face_locations),face_names, len(face_encodings))
        for (top, right, bottom, left), name, age in zip(face_locations, face_names, ages):
            # Scale back up face locations since the frame we detected in was scaled to 1/4 size
            top *= int(4*self.p)
            right *= int(4*self.p)
            bottom *= int(4*self.p)
            left *= int(4*self.p)
            percent = self.utils.getPercent(frame.shape,(top, right, bottom, left))
            color = self.color['rojo'] if (percent<self.percent) else self.color['verde']
            color = self.color['azul'] if (self.upload) else color

            cv2.rectangle(frame, (left, top), (right, bottom), color, 2)
            cv2.rectangle(frame, (left, bottom - 35),(right, bottom), color, cv2.FILLED)
            font = cv2.FONT_HERSHEY_DUPLEX
            cv2.putText(frame,name + " " + str(age) , (left + 6, bottom - 12),font, 0.7, (255, 255, 255), 1)

        # Display the resulting image
        return [frame, isInFront]

    def cropper(self, frame,face_locations):
        frame_area = frame.shape[0]*frame.shape[1]
        person_loc = face_locations
        person_loc.sort(key=self.utils.sortLocation, reverse=True)
        # print(person_loc)
        if(len(person_loc)):  # detecta si hay personas
            # print("Person detect: {}".format(len(person_loc)))
            people, areas = self.utils.setDictionary(person_loc)
            # print(areas)
            # top, rigth, bottom, left (t,r,b,l)
            t, r, b, l = self.utils.increase(list(np.asarray(person_loc[0])*4))
            percent = max(areas)*100/float(frame_area)
            # print(percent)
            if(percent >= self.percent):
                # recortar imagenes image[y:y+h, x:x+w]
                return [frame[t:b, l:r], True]

        return [frame, False]

    def neural_recognition(self, name, frame):
        self.upload = 1 #trabajando en la caracterizacion
        person = self.person_cloud.detectPerson(frame)
        face_encodings = face_recognition.face_encodings(frame)
        print("face encoding: " + str(len(face_encodings)))
        if(len(person)):
            person = person[0]
            if(len(face_encodings)):
                self.personModel.append(face_encodings[0])
                person["name"] = name
                # print ("person ATTRIBUTES{}".format(person))
                self.personGroup.append(person)
                print(self.personGroup)
                self.packing.pack(self.personGroup, self.fileName[0])
                self.packing.pack(self.personModel, self.fileName[1])
                self.unpack()
                # self.spech.play(person)
        self.upload = 0 #caracterizacion finalizada
        return person

