import numpy as np
import cv2

# events = [i for i in dir(cv2) if 'EVENT' in i]
# for i in events:
    # print(i)

def click_event(event, x, y, flags, param, ):
    if event == cv2.EVENT_LBUTTONDOWN:
        str1 = str(x) + " " + str(y)

        print(str1)
        font = cv2.FONT_HERSHEY_COMPLEX
        cv2.putText(img, str1, (x, y), font, 1, (0,122,255), 5, cv2.LINE_AA)
        cv2.imshow('image', img)

    if event == cv2.EVENT_RBUTTONDOWN:
        blue = img[y, x, 0] #get blue content
        red = img[y, x, 1] # get red content   on x, y on picture,  example:(203,11,223)
        green = img[y, x, 2] #get green content

        strBGR = str(blue) + " " + str(red) + " " + str(green)

        font = cv2.FONT_HERSHEY_COMPLEX
        cv2.putText(img, strBGR, (x, y), font, 1, (0,122,255), 5, cv2.LINE_AA)
        cv2.imshow('image', img)
    
# img = np.zeros((512, 512, 3), np.uint8)
img = cv2.imread('aot.png')
cv2.imshow('image', img)
cv2.setMouseCallback('image', click_event)

cv2.waitKey(0)
cv2.destroyAllWindows()