import cv2
import numpy as np
from matplotlib import pyplot as plt

#camera img
cap = cv2.VideoCapture(0)


template1 = cv2.imread('dorito.png',0)

template2 = cv2.imread('just_a_star.png',0)

template3 = cv2.imread('love.png',0)

template4 = cv2.imread('pi.png',0)

template5 = cv2.imread('square.png',0)

template6 = cv2.imread('stonks.png',0)

template7 = cv2.imread('treasure.png',0)

# Prints rectangles if 'template' is in 'frame' with probability of at least 'thresh'
#         :param frame: A frame
#         :param template: An image to search in 'frame'.
#         :param thresh: The minimum probability required to accept template.
#         :param original: original frame
#         :if a is not false, prints rectangles on both images
def exists(frame, template, thresh, original):
        a = True
        res = cv2.matchTemplate(frame, template, cv2.TM_CCOEFF_NORMED)
        loc = np.where(res >= thresh)
        w, h = template.shape[::-1]

        
        if len(loc[-1]) == 0:
            a = False
            

        for pt in zip(*loc[::-1]):
            if res[pt[1]][pt[0]] == 1:
                a = False

        if a != False:
            min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
            top_left = max_loc
            bottom_right = (top_left[0] + w, top_left[1] + h)
            cv2.rectangle(frame,top_left, bottom_right, 255, 2)
            cv2.rectangle(original,top_left, bottom_right, 255, 2)
            return True

# probably only need this method 'cv2.TM_CCOEFF_NORMED', third argument in cv2.matchTemplate
while True:
    ret, frame = cap.read()

    #shape is searched from grayboy
    grayboy = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)


    
    #This at the same time makes the function be called all the time and checks its value, which is True if the template is detected with a high enough likelihood
    #Likelihood depends on complexity of shape and accuracy of your drawing to the source material, created in Paint
    if exists(grayboy, template1, 0.5, frame) == True:
        print("Tasty dorito")
        #or do anything else, eg dance or display a light show on a dot matrix
    elif exists(grayboy, template2, 0.4, frame) == True:
        print("Milky way")
    elif exists(grayboy, template3, 0.5, frame) == True:
        print("Very sweet")
    elif exists(grayboy, template4, 0.4, frame) == True:
        print("Looks quite round")
    elif exists(grayboy, template5, 0.5, frame) == True:
        print("Lego?")
    elif exists(grayboy, template6, 0.4, frame) == True:
        print("Stonk market")
    elif exists(grayboy, template7, 0.5, frame) == True:
        print("Captain Jack Sparrow is calling")
    
    
    cv2.imshow('Original with detection', frame)
    cv2.imshow('Grayscale with detection', grayboy)
    #You will have to press this twice
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.waitKey(0)
cv2.destroyAllWindows()
