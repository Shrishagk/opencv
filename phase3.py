#Drawing a line
import cv2
image = cv2.imread(r"c:\Users\shris\OneDrive\Pictures\133946061638512189.jpg")
line_image = image.copy()
cv2.line(line_image, (50, 50), (200, 200), (0, 255, 0), 5) # Green line with thickness 5
cv2.imshow("Line Image", line_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
#Drawing a rectangle
rectangle_image = image.copy()
cv2.rectangle(rectangle_image, (50, 50), (200, 200), (255, 0, 0), 1) # Blue rectangle with thickness 3
cv2.imshow("Rectangle Image", rectangle_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
#Drawing a circle
circle_image = image.copy()
cv2.circle(circle_image, (150, 150), 75, (0, 0, 255), -1) # Red filled circle
cv2.imshow("Circle Image", circle_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
#Drawing text
text_image = image.copy()
cv2.putText(text_image, "OpenCV", (50, 250), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 255), 3) # White text
cv2.imshow("Text Image", text_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
#Drawing an ellipse
ellipse_image = image.copy()
cv2.ellipse(ellipse_image, (250, 250), (100, 50), 0, 0, 360, (255, 255, 0), -1) # Cyan filled ellipse
cv2.imshow("Ellipse Image", ellipse_image)
cv2.waitKey(0)
cv2.destroyAllWindows()