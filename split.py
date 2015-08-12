import cv2
fn = "/home/triet/Desktop/cat_video.mp4"
cap = cv2.VideoCapture(fn)
while not cap.isOpened():
    cap = cv2.VideoCapture(fn)
    cv2.waitKey(1000)
    print "Wait for the header"

pos_frame = cap.get(cv2.cv.CV_CAP_PROP_POS_FRAMES)
count = 0
while True:
    flag, frame = cap.read()
    if flag:
        cv2.imshow('video', frame)
        pos_frame = cap.get(cv2.cv.CV_CAP_PROP_POS_FRAMES)
        print str(pos_frame)+" frames"
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
        cv2.imwrite("/home/triet/Desktop/frames/frame%d.jpg" % count, frame)
        print str(pos_frame)+" frames"
    else:
        cap.set(cv2.cv.CV_CAP_PROP_POS_FRAMES, pos_frame-1)
        cv2.waitKey(1000)
        
    if cv2.waitKey(2) == 27:
        cv2.destroyAllWindows()
        break
    if cap.get(cv2.cv.CV_CAP_PROP_POS_FRAMES) == cap.get(cv2.cv.CV_CAP_PROP_FRAME_COUNT):
        break
    count+=1
    
    import cv2
    
im_gray = cv2.imread('grayscale_image.png', cv2.CV_LOAD_IMAGE_GRAYSCALE)

(thresh, im_bw) = cv2.threshold(im_gray, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
thresh = 127
im_bw = cv2.threshold(im_gray, thresh, 255, cv2.THRESH_BINARY)[1]
cv2.imwrite('bw_image.png', im_bw)