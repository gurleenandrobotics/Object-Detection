import cv2

def reddetection(frame):
    #print("Red detection script started\n")
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Red range 1
    lower_red1 = (0, 120, 70)
    upper_red1 = (10, 255, 255)
    mask1 = cv2.inRange(hsv, lower_red1, upper_red1)

    # Red range 2
    lower_red2 = (170, 120, 70)
    upper_red2 = (180, 255, 255)
    mask2 = cv2.inRange(hsv, lower_red2, upper_red2)

    mask = mask1 + mask2
    res = cv2.bitwise_and(frame, frame, mask=mask)
    #print("Red detection script ended\n")
    return res

# Webcam loop
cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    if not ret:
        break

    red_frame = reddetection(frame)  # Apply red detection

    cv2.imshow("Original", frame)
    cv2.imshow("Red Detection", red_frame)  # Show red-only frame

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
