# [J]efferson , Eng. De Produção

import cv2

cascade = 'haarcascade_eye.xml'

faceClassifier = cv2.CascadeClassifier(cascade)

caputara = cv2.VideoCapture(0)

caputara.set(cv2.CAP_PROP_FRAME_WIDTH, 800)
caputara.set(cv2.CAP_PROP_FRAME_HEIGHT, 700)


while caputara.isOpened():

    ret, frame = caputara.read()

    cinza = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    face = faceClassifier.detectMultiScale(cinza)

    for x, y, w, h in face:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 1)

    cv2.imshow('color', frame)

    if cv2.waitKey(5) & 0xFF == 27:
      break


caputara.release()