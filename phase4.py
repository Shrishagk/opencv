import cv2
#Video Capture from webcam
cap = cv2.VideoCapture(0)# 0 is usually the default webcam in laptops 
while True:# Infinite loop to continuously get frames
    ret, frame = cap.read()# ret is a boolean(returns true/false) indicating if frame is read correctly
    if not ret:
        break
    cv2.imshow("Webcam Feed", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):# Press 'q' to quit, 1 millisecond delay and ord returns ASCII value of 'q'
        print("Quitting...")
        break
cap.release()# stop video capture
cv2.destroyAllWindows()
#Video writer
frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))# Get width of the frames by telling the capture object to return the width property
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))# Get height of the frames by telling the capture object to return the height property
codec = cv2.VideoWriter_fourcc(*'XVID')#video_writer_fourcc is a function that defines the codec, here we are using XVID meaning .avi format
out = cv2.VideoWriter('output.avi', codec, 20.0, (frame_width, frame_height))# Create VideoWriter object, 20.0 is fps(frames per second)
cap = cv2.VideoCapture(0)# Reinitialize video capture
while True:
    ret, frame = cap.read()
    if not ret:
        break
    out.write(frame)# Write the frame to the output file
    cv2.imshow("Recording live", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        print("Quitting...")
        break
cap.release()
out.release()# Release the video writer
cv2.destroyAllWindows()
#Video writing in mp4 format
cap = cv2.VideoCapture(0)
frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
codec = cv2.VideoWriter_fourcc(*'mp4v')# mp4v codec for .mp4 format
out = cv2.VideoWriter('output.mp4', codec, 20.0, (frame_width, frame_height))
while True:
    ret, frame = cap.read()
    if not ret:
        break
    out.write(frame)
    cv2.imshow("Recording live in mp4", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        print("Quitting...")
        break

cap.release()
out.release()
cv2.destroyAllWindows()