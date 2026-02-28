#resizing image 
import cv2
image = cv2.imread(r"c:\Users\shris\OneDrive\Pictures\133946061638512189.jpg")
resized_image = cv2.resize(image,(500,500))
cv2.imshow("Resized Image",resized_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
# cropping image
cropped_image = image[100:400, 100:400]
cv2.imshow("Cropped Image",cropped_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
# rotating image
(h, w) = image.shape[:2]
center = (w // 2, h // 2)
M = cv2.getRotationMatrix2D(center, 45, 1.0)# 45-degree rotation, scale factor 1.0(1.0 means same image size)
rotated_image = cv2.warpAffine(image, M, (w, h))
cv2.imshow("Rotated Image", rotated_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
# flipping image
flipped_image_horizontal = cv2.flip(image, 1) # 1 for horizontal flip
flipped_image_vertical = cv2.flip(image, 0)   # 0 for vertical flip
flipped_image_both = cv2.flip(image, -1)      # -1 for both axes
cv2.imshow("Flipped Image", flipped_image_horizontal)
cv2.imshow("Flipped Image", flipped_image_vertical)
cv2.imshow("Flipped Image", flipped_image_both)
cv2.waitKey(0)
cv2.destroyAllWindows()
