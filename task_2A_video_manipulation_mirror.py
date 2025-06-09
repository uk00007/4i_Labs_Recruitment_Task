import cv2
import numpy as np

cap = cv2.VideoCapture("4i Labs/video_task.mp4")
width = int(cap.get(3))
length = int(cap.get(4))
fps = cap.get(cv2.CAP_PROP_FPS)


fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter('4i Labs/video_manipulation_results/mirror_video_result.mp4',
                      fourcc, fps, (500, 568))

while (cap.isOpened()):
    ret, frame = cap.read()

    if not ret:
        print('End of video or error in opening the file')
        break

    img = np.zeros(frame.shape, np.uint8)
    smaller_frame = cv2.resize(frame, (0, 0), fx=0.5, fy=0.5)

    img[:length//2, :width//2] = smaller_frame
    img[:length//2, width // 2:] = cv2.flip(smaller_frame, 1)
    img[length//2:, :width//2] = cv2.flip(smaller_frame, 0)
    img[length//2:, width//2:] = cv2.flip(smaller_frame, -1)

    out.write(img)
    cv2.imshow('frame', img)
    if cv2.waitKey(25) == ord('x'):
        break

out.release()
cap.release()
cv2.destroyAllWindows()
