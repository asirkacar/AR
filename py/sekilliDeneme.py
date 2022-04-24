import numpy as np
import cv2

camera = cv2.VideoCapture(0)

while(1):
    _, frame = camera.read()
    width  = frame.shape[1]
    height = frame.shape[0]
    distCoeff = np.zeros((4,1),np.float64)
    k1 = 10.0e-5; # negative to remove barrel distortion
    k2 = 0.0;
    p1 = 0.0;
    p2 = 0.0;

    distCoeff[0,0] = k1;
    distCoeff[1,0] = k2;
    distCoeff[2,0] = p1;
    distCoeff[3,0] = p2;

  # assume unit matrix for camera
    cam = np.eye(3,dtype=np.float32)

    cam[0,2] = width/2.0  # define center x
    cam[1,2] = height/2.0 # define center y
    cam[0,0] = 8.        # define focal length x  10
    cam[1,1] = 8.        # define focal length y    10

  # here the undistortion will be computed
    dst = cv2.undistort(frame,cam,distCoeff)
    im_h = cv2.hconcat([dst, dst])


    cv2.imshow('dst',im_h)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cv2.destroyAllWindows()