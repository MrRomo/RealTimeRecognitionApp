from t2s import t2s


datos = {u'faceId': u'67c09f42-492f-4b0d-b2ec-89f6c4e36569', u'faceRectangle': {u'width': 176, u'top': 72, u'height': 176, u'left': 37}, 'name': 'Dilan', u'faceAttributes': {u'emotion': {u'sadness': 0.001, u'neutral': 0.999, u'contempt': 0.0, u'disgust': 0.0, u'anger': 0.0, u'surprise': 0.0, u'fear': 0.0, u'happiness': 0.0}, u'gender': u'male', u'age': 14.0, u'makeup': {u'lipMakeup': False, u'eyeMakeup': False}, u'accessories': [], u'facialHair': {u'sideburns': 0.0, u'moustache': 0.0, u'beard': 0.0}, u'hair': {u'invisible': False, u'hairColor': [{u'color': u'black', u'confidence': 0.99}, {u'color': u'brown', u'confidence': 0.86}, {u'color': u'other', u'confidence': 0.36}, {u'color': u'gray', u'confidence': 0.31}, {u'color': u'blond', u'confidence': 0.09}, {u'color': u'red', u'confidence': 0.07}], u'bald': 0.05}, u'headPose': {u'yaw': 14.5, u'roll': 9.1, u'pitch': 5.3}, u'smile': 0.0, u'glasses': u'NoGlasses'}}


spech = t2s()

spech.play(datos)
