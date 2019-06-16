import cv2
vidcap = cv2.VideoCapture('face.mp4')
success,image = vidcap.read()
count = 0
while success:
  cv2.imwrite("zdjęcie%d.jpg" % count, image)        
  success,image = vidcap.read()
  print('Tworzenie nowego zdjęcia: ', success)
  count += 1
