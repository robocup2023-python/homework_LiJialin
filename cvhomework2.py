import cv2
img = cv2.imread("test2.png",0)
# 高斯滤波
blurred = cv2.GaussianBlur(img,(5,5),5)
# Sobel 算子
x = cv2.Sobel(blurred, cv2.CV_16S, 1, 0)
y = cv2.Sobel(blurred, cv2.CV_16S, 0, 1)
# 转 uint8 ,图像融合
absX = cv2.convertScaleAbs(x)
absY = cv2.convertScaleAbs(y)
add = cv2.addWeighted(absX, 0.5, absY, 0.5, 0)
#连接边缘
result = cv2.Canny(add,15,25)
cv2.imwrite('bianyuan.png',result)
cv2.imwrite('xtidu.png',x)
cv2.imwrite('ytidu.png',y)
#下面是角点检测但是没整好
# 高斯滤波
gauss = cv2.GaussianBlur(img,(5,5),3)
x_deg = cv2.Sobel(gauss,cv2.CV_16S,1,0)
y_deg = cv2.Sobel(gauss,cv2.CV_16S,0,1)
abs_1 = cv2.convertScaleAbs(x_deg**2)
abs_2 = cv2.convertScaleAbs(y_deg**2)
abs_3 = cv2.convertScaleAbs(x_deg*y_deg)
cv2.imwrite('x^2.png',abs_1)
cv2.imwrite('y^2.png',abs_2)
cv2.imwrite('xy.png',abs_3)
gauss1 = cv2.GaussianBlur(abs_1,(5,5),1)
gauss2 = cv2.GaussianBlur(abs_2,(5,5),1)
gauss3 = cv2.GaussianBlur(abs_3,(5,5),1)
