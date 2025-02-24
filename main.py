
import cv2 as cv

from util import get_limits
from PIL import Image

yellow = [0,255,255]


cap = cv.VideoCapture(0)

while True:
    ret, frame = cap.read()
    
    hsv_img = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    
    lower_limit, upper_limit = get_limits(color=yellow)
    
    mask = cv.inRange(hsv_img, lower_limit, upper_limit)
    
    
    
   
    
    mask_ = Image.fromarray(mask)
    
    box = mask_.getbbox()
    
    if box is not None:
        x1, y1, x2, y2 = box
        
        cv.rectangle(frame, (x1, y1), (x2, y2), (0,0,255), 5)
        
     
    cv.imshow('video', frame)    
    
    if cv.waitKey(1) & 0xFF == ord('q'):
        break
    
    
cap.release()
cv.destroyAllWindows()


