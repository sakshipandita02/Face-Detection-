import cv2

# Create a CascadeClassifier Object
face_cascade = cv2.CascadeClassifier("C:\\Users\\Sakshi\\Anaconda3\\Lib\\site-packages\\cv2\\data\\haarcascade_frontalface_default.xml")

# Read img
img = cv2.imread("C:\\Users\\Sakshi\\Desktop\\bcd_friends_web_900x506.jpg")

# Read img as gray scale img
gray_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# Findthe co-ordintes of img
faces =face_cascade.detectMultiScale(gray_img,1.1,5)
for x,y,w,h in faces:
    img = cv2.rectangle(img, (x,y), (x+w,y+h),(0,255,0),3)
 
resized = cv2.resize(img, (int(img.shape[1]),int(img.shape[0])))
cv2.imshow("SAKSHI PANDITA", resized)
cv2.waitKey(0)
cv2.destroyAllWindows()
