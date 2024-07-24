import numpy as np
import cv2

img = cv2.imread("assets/corgi.png")
cv2.imshow("Original", img)

# custom transformation matrix
mat = np.float32([[3, 0, 0], [0, 3, 0]])
print(mat)
result = cv2.warpAffine(img, M=mat, dsize=(600, 600))
cv2.imshow("600x600 with Scaling", result)

cv2.waitKey(0)
cv2.destroyAllWindows()
