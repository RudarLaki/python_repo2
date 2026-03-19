import cv2
import datetime


img = cv2.imread('aot.png', -1)
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite('aot1.png', img)




capture = cv2.VideoCapture(0)

widthId = cv2.CAP_PROP_FRAME_WIDTH
heightId = cv2.CAP_PROP_FRAME_HEIGHT

FRAME_WIDTH = capture.get(cv2.CAP_PROP_FRAME_WIDTH)
FRAME_HEIGHT = capture.get(cv2.CAP_PROP_FRAME_HEIGHT)

capture.set(widthId, 120)
capture.set(heightId, 300) #if not valid -> closest smaller valid


fourcc = cv2.VideoWriter_fourcc(*'XVID')
#out = cv2.VideoWriter('output.avi', fourcc, 20.0, (FRAME_WIDTH,FRAME_HEIGHT))

while(capture.isOpened()):
    ret, frame = capture.read()

    if(not ret):
        break
    
    font = cv2.FONT_HERSHEY_COMPLEX
    datet = str(datetime.datetime.now())

    frame = cv2.putText(frame, datet, (10, 50), font, 1, (0, 255, 255), 2, cv2.LINE_AA )

    #out.write(frame)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('frame', gray)
    if cv2.waitKey(1) == 27:
        break



capture.release()
#out.release()
cv2.destroyAllWindows()
