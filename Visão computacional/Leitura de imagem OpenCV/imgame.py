# [J]efferson , Eng. De Produção
import cv2

cascade = 'haarcascade_frontalface_alt2.xml'


# Carregar classificação do arquivo encontrado no openCv no gitHub
faceClassifier = cv2.CascadeClassifier(cascade)
# Ativação da câmera do notebook
caputara = cv2.VideoCapture(0)
# Tamanho da tela das telas que irão abrir.
caputara.set(cv2.CAP_PROP_FRAME_WIDTH, 500)
caputara.set(cv2.CAP_PROP_FRAME_HEIGHT, 400)

while caputara.isOpened():

    ret, frame = caputara.read()

    cinza = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    face = faceClassifier.detectMultiScale(cinza)

    for x, y, w, h in face:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 1)

    for x, y, w, h in face:
        cv2.rectangle(cinza, (x, y), (x + w, y + h), (0, 255, 0), 1)

    cv2.imshow('color', frame)
    cv2.imshow('gray', cinza)

    if cv2.waitKey(5) & 0xFF == 27:
      break


caputara.release()
