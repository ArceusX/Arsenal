import cv2

fn = "/home/triet/Desktop/video.mp4"
cap = cv2.VideoCapture(fn)
while not cap.isOpened():
    cap = cv2.VideoCapture(fn)
    cv2.waitKey(1000)
    print "Wait for header"

pos_frame = cap.get(cv2.cv.CV_CAP_PROP_POS_FRAMES)
count = 0
while True:
    flag, frame = cap.read()
    if flag:
        cv2.imshow('video', frame)
        pos_frame = cap.get(cv2.cv.CV_CAP_PROP_POS_FRAMES)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        print str(pos_frame)+" frames"
        cv2.imwrite("/home/triet/Desktop/frames3/frame%d.jpg" % count, frame)
    else:
        cap.set(cv2.cv.CV_CAP_PROP_POS_FRAMES, pos_frame-1)
        cv2.waitKey(1000)
    if cv2.waitKey(2) == 27:
        cv2.destroyAllWindows()
        break
    if cap.get(cv2.cv.CV_CAP_PROP_POS_FRAMES) == cap.get(cv2.cv.CV_CAP_PROP_FRAME_COUNT):
        break
    count+=1
