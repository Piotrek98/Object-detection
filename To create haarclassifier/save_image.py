import cv2
vidcap = cv2.VideoCapture('...') #path to your video
success,image = vidcap.read()
count = 0
while success:
  cv2.imwrite("image%d.jpg" % count, image)        
  success,image = vidcap.read()
  print('Create new image: ', success)
  count += 1
