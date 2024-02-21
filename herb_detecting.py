from collections import deque
import cv2 as cv
import imutils
import communication

# Initialize serial communication
usart = communication.SerialCommunication()
usart.initialize_port()

# define the lower and upper boundaries of the "green"
greenLower = (26, 80, 71)
greenUpper = (40, 255, 255)
pts = deque(maxlen=40)

# define a video capture object
vid = cv.VideoCapture(0)

while True:
    # Capture the video frame by frame
    ret, frame = vid.read()

    # resize the frame,blur it, and convert it to the HSV
    frame = imutils.resize(frame, width=600, height=450)
    blurred = cv.GaussianBlur(frame, (11, 11), 0)
    hsv = cv.cvtColor(blurred, cv.COLOR_BGR2HSV)

    # construct a mask for the color "green", then perform
    # a series of dilations and erosions to remove any small
    # blobs left in the mask
    mask = cv.inRange(hsv, greenLower, greenUpper)
    mask = cv.erode(mask, None, iterations=2)
    mask = cv.dilate(mask, None, iterations=2)

    # find contours in the mask and initialize the current
    # (x, y) center of the ball
    cnts = cv.findContours(mask.copy(), cv.RETR_EXTERNAL,
                           cv.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)
    center = None

    # only proceed if at least one contour was found
    if len(cnts) > 0:
        # find the largest contour in the mask, then use
        # it to compute the minimum enclosing circle and centroid
        c = max(cnts, key=cv.contourArea)
        ((x, y), radius) = cv.minEnclosingCircle(c)
        M = cv.moments(c)
        print(x, y)

        # sending x and y location of herb (green ball) to STM32
        usart.send_data_to_stm32(x, y)

        center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))
        # only proceed if the radius meets a minimum size
        #if radius > 15:
            # draw the circle and centroid on the frame,
            # then update the list of tracked points
            # cv.circle(frame, (int(x), int(y)), int(radius),
                      #(0, 255, 255), 2)
            # cv.circle(frame, center, 5, (0, 0, 255), -1)
    # update the points queue
    pts.appendleft(center)

    # loop over the set of tracked points
    for i in range(1, len(pts)):
        # if either of the tracked points are None, ignore them
        if pts[i - 1] is None or pts[i] is None:
            continue
        # otherwise, compute the thickness of the line and
        # draw the connecting lines
        # cv.line(frame, pts[i - 1], pts[i], (0, 0, 255), 3)

    # Display the resulting frame
    cv.imshow('frame', frame)

    # the 'q' button is set as the quitting button
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

# After the loop release the cap object
vid.release()
# Destroy all the windows
cv.destroyAllWindows()
