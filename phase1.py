#To load image
import cv2
image = cv2.imread(r"c:\Users\shris\OneDrive\Pictures\133946061638512189.jpg")
#To display image
cv2.imshow("Output",image)
cv2.waitKey(0)
cv2.destroyAllWindows()
#To save image
cv2.imwrite("Output.jpg",image)
#shape of image
print(image.shape)
#To convert image to grayscale
gray_image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
cv2.imshow("Gray Image",gray_image)
cv2.waitKey(0)
cv2.destroyAllWindows()