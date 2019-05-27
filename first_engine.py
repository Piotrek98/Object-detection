import cv2


face_cascade = cv2.CascadeClassifier(0) # 1 for online camera
video = cv2.VideoCapture(0)


while True:
    ret,img = video.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.55, minNeighbors=5)

    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y), (x+w, y+h), (0,255,0),2)


    cv2.imshow('img', img)

    k = cv2.waitKey(1)
    if k == ord('q'):
        break


video.release()
cv2.destroyAllWindows()
