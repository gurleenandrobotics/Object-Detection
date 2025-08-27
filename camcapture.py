import cv2

def vid():
    #print("Script started")

    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
      #  print(" Failed to open camera")
        exit()

    #print("Camera opened")

    while True:
        ret, frame = cap.read()
        if not ret:
           # print("Failed to grab frame")
            break

        cv2.imshow("Webcam", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
    return frame
    print("Script ended")
