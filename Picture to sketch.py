import cv2

#image upload
image = cv2.imread("sample image.jpg")

#convertion of the colours to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#invertion of the grayscale image to get the negative image, which enhances details.
inverted_image = 255 - gray_image

#creation of the pencil sketch by mixing the grayscale image with the inverted blurry image.
blurred = cv2.GaussianBlur(inverted_image, (21, 21), 0)
inverted_blurred = 255 - blurred
pencil_sketch = cv2.divide(gray_image, inverted_blurred, scale=256.0)

#We now got our pencil_sketch. So, display it using OpenCV.
cv2.imshow("Original Image", image)
cv2.imshow("Pencil Sketch of Dog", pencil_sketch)
cv2.waitKey(0)