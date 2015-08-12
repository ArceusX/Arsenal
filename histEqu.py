fd_in = "/home/triet/Desktop/frames2/"
fd_out = "/home/triet/Desktop/frames4/"

import cv2
import glob
import re

def process(filename, key):
    img = cv2.imread(filename,0)
    img = cv2.equalizeHist(img)
    cv2.imwrite(fd_out+'frame_{}.jpg'.format(key),img)
    print 'frame_{}.jpg'.format(key)

digits = re.compile(r'(\d+)')

def tokenize(filename):
    return tuple(int(token) if match else token
                 for token, match in
                 ((fragment, digits.search(fragment))
                  for fragment in digits.split(filename)))
                      
for (i,image_file) in enumerate(glob.iglob(fd_in+'*.jpg')):
        process(image_file, i)
        
        