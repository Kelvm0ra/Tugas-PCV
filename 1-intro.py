import cv2

# Code read image
image = cv2.imread( "image2.png")
[h,w,c] = image.shape

# Code Filter color image
for i in range(h) :
    for j in range(w) :
        image [i, j, 1] = 0
        image [i, j, 0] = 0

# Code Show image
scale = 0.5
cv2.namedWindow("Image setelah di filter", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Image setelah di filter", int(w * scale), int(h * scale))
cv2.imshow("Image setelah di filter", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Code filter color video
cap = cv2.VideoCapture(0)

scale = 0.5
while True:
    ret, frame = cap.read()
    if not ret:
        break
    frame[:, :, 0] = 0
    frame[:, :, 1] = 0
    [h, w, c] = frame.shape
    resized = cv2.resize(frame, (int(w * scale), int(h * scale)))
    cv2.imshow("Webcam setelah di filter", resized)

    cv2.waitKey(1)
    if cv2.getWindowProperty("Webcam setelah di filter", cv2.WND_PROP_VISIBLE) < 1:
        break

cap.release()
cv2.destroyAllWindows()