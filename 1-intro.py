import cv2
from matplotlib import pyplot as plt

image = cv2.imread( "image2.png")
[h,w,c] = image.shape

for i in range(h) :
    for j in range(w) :
        image [i, j, 1] = 0
        image [i, j, 0] = 0

#Menampilkan Citra
scale = 0.5
cv2.namedWindow("Image Merah", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Image Merah", int(w * scale), int(h * scale))
cv2.imshow("Image Merah", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
plt.imshow(image)
plt.title("Image")
plt.show()