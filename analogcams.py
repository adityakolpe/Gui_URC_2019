import numpy as np
import cv2

<<<<<<< HEAD
cap = cv2.VideoCapture('rtsp://192.168.1.90/user=root&password=mrm&channel=1&stream=0.sdp?real_stream--rtp-caching=1')
=======
cap = cv2.VideoCapture('rtsp://192.168.1.90/axis-media/media.amp?camera=3')
>>>>>>> 64b8ef3640f1d5c8a592fae197a2df39e7b692a6
while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
   # ret1, frame1 = cap1.read()

    # Display the resulting frame
    cv2.imshow('frame',frame)
   # cv2.imshow('frame1',frame1)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cap1.release()
cv2.destroyAllWindows()