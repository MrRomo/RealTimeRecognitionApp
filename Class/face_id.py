# -*- coding: utf-8 -*-
#!/usr/bin/env python
# license removed for brevity
# //======================================================================//
# //  This software is free: you can redistribute it and/or modify        //
# //  it under the terms of the GNU General Public License Version 3,     //
# //  as published by the Free Software Foundation.                       //
# //  This software is distributed in the hope that it will be useful,    //
# //  but WITHOUT ANY WARRANTY; without even the implied warranty of      //
# //  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE..  See the      //
# //  GNU General Public License for more details.                        //
# //  You should have received a copy of the GNU General Public License   //
# //  Version 3 in the file COPYING that came with this distribution.     //
# //  If not, see <http://www.gnu.org/licenses/>                          //
# //======================================================================//
# //                                                                      //
# //      Copyright (c) 2019 SinfonIA Pepper RoboCup Team                 //
# //      Sinfonia - Colombia                                             //
# //      https://sinfoniateam.github.io/sinfonia/index.html              //
# //                                                                      //
# //======================================================================//
from characterization import Characterization
from characterization import Characterization
import cv2
import time
from datetime import datetime
import numpy as np
from utils import Utils



class FaceID():
    def __init__(self, camera, person):
        self.person = Characterization(person)
        self.source = camera
        self.frame = None
        self.resolution = [120, 240, 480, 960, 1920, 0, 0, 0, 60, 30]
        self.res = 4
        self.request = False
        self.utils = Utils(self.source, self.person.percent_of_face)

    def detectFace(self):
        print("Detect request")
        # self.initCamera()
        frame = self.utils.take_picture_source(self.frame)
        self.frame = None
        self.request = False
        people = self.person.detect_person(frame)
        res = self.utils.add_features_to_image(frame, people)
     
        return res["isInFront"]

    def recognizeFace(self, req):
        print("Recognize request")
        # self.initCamera()
        frame = self.utils.take_picture_source(self.frame)
        self.frame = None
        self.request = False
        people = self.person.indentify_person(frame)
        if req.cvWindow and people:
            res = self.utils.add_features_to_image(frame, [people])
            self.imagePub.publish(res["frame"])

        return str(people)

    def memorizeFace(self, req):
        print("Memorize request")
        # self.initCamera()
        images = []
        for i in range(req.n_images):
            frame = self.utils.take_picture_source(self.frame)
            frame = cv2.GaussianBlur(frame, (5, 5), 0)
            print(frame.shape)
            images.append(frame)
            if(self.source == 'pepper'):
                self.frame = None
                while self.frame is None:
                    pass

        print("n_images toke {}".format(len(images)))

        person = self.person.add_person(req.name, images)  # Add person
        print("Person faceid", person)

        return str(person)
