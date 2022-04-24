faces = faceCascade.detectMultiScale(
     gray,
     scaleFactor=1.1,
     minNeighbors=5,
     minSize=(30, 30),
     flags = cv2.CV_HAAR_SCALE_IMAGE
 )