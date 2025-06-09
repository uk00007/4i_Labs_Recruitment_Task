import cv2
import numpy as np

cap = cv2.VideoCapture("4i Labs/video_task.mp4")
fps = cap.get(cv2.CAP_PROP_FPS)

fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out_green = cv2.VideoWriter(
    '4i Labs/video_manipulation_results/green_filter_result.mp4', fourcc, fps, (500, 568))
out_blue = cv2.VideoWriter(
    '4i Labs/video_manipulation_results/blue_filter_result.mp4', fourcc, fps, (500, 568))
out_pink_or_white = cv2.VideoWriter(
    '4i Labs/video_manipulation_results/pink_or_white_filter_result.mp4', fourcc, fps, (500, 568))

out_blue_or_willow = cv2.VideoWriter(
    '4i Labs/video_manipulation_results/blue_or_willow_filter_result.mp4', fourcc, fps, (500, 568))

while (cap.isOpened()):

    ret, frame = cap.read()
    if not ret:
        print('End of video or error in opening the file')
        break

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lower_green = np.array([30, 50, 100])
    upper_green = np.array([80, 255, 255])

    lower_blue = np.array([90, 50, 50])
    upper_blue = np.array([130, 255, 255])

    lower_pink = np.array([140, 50, 100])
    upper_pink = np.array([170, 255, 255])

    lower_white = np.array([0, 0, 200])
    upper_white = np.array([180, 30, 255])

    lower_willow = np.array([0, 10, 0], dtype="uint8")
    upper_willow = np.array([40, 120, 255], dtype="uint8")

    mask_blue = cv2.inRange(hsv, lower_blue, upper_blue)
    mask_green = cv2.inRange(hsv, lower_green, upper_green)
    mask_pink = cv2.inRange(hsv, lower_pink, upper_pink)
    mask_white = cv2.inRange(hsv, lower_white, upper_white)
    mask_pink_or_white = cv2.bitwise_or(mask_pink, mask_white)
    mask_willow = cv2.inRange(hsv, lower_willow, upper_willow)
    mask_blue_or_willow = cv2.bitwise_or(mask_willow, mask_blue)

    result_blue = cv2.bitwise_and(frame, frame, mask=mask_blue)
    result_green = cv2.bitwise_and(frame, frame, mask=mask_green)
    result_pink_or_white = cv2.bitwise_and(
        frame, frame, mask=mask_pink_or_white)
    result_blue_or_willow = cv2.bitwise_and(
        frame, frame, mask=mask_blue_or_willow)

    out_green.write(result_green)
    out_blue.write(result_blue)
    out_pink_or_white.write(result_pink_or_white)
    out_blue_or_willow.write(result_blue_or_willow)
    cv2.imshow('frame', result_blue_or_willow)

    if cv2.waitKey(25) == ord('x'):
        break

out_blue.release()
out_green.release()
out_pink_or_white.release()
out_blue_or_willow.release()
cap.release()
cv2.destroyAllWindows()
