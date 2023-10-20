import matplotlib
matplotlib.use('Qt5Agg')
import matplotlib.pyplot as plt
import cv2
import numpy
# img = cv2.imread('./test.png')
def showimg(name,img):
  cv2.imshow(name,img)
  cv2.waitKey(0)
#高斯滤波核生成
def gauss(size=5,sigma=1):
  if(sigma==0):
    raise ValueError('0不能做除数')
  x_d = numpy.linspace(-3*sigma,3*sigma,size)
  y_d = numpy.linspace(-3*sigma,3*sigma,size)
  x,y = numpy.meshgrid(x_d,y_d)
  gauss_origin = (1 / (2 * numpy.pi * sigma**2)) * numpy.exp(-(x**2 + y**2)/(2*sigma**2))
  return gauss_origin*(1/gauss_origin.sum())
#反射边缘
def reflect(img,px:int=5):
  top = img[0:px,:]
  bottom = img[-px:-1,:]
  top_f = top[::-1,:]
  bottom_f = bottom[::-1,:]
  add_top = numpy.concatenate((top_f,img),axis=0)
  add_bottom = numpy.concatenate((add_top,bottom_f),axis=0)
  left = add_bottom[:,0:px]
  right = add_bottom[:,-px:-1]
  left_f = left[:,::-1]
  right_f = right[:,::-1]
  add_left = numpy.concatenate((left_f,add_bottom),axis=1)
  add_right = numpy.concatenate((add_left,right_f),axis=1)
  return add_right
#法二，平移（写完反射实在想挑个简单的）
def move(img,px):
  top = img[0:px,:]
  bottom = img[-px:-1,:]
  add_top = numpy.concatenate((bottom,img),axis=0)
  add_bottom = numpy.concatenate((add_top,top),axis=0)
  left = add_bottom[:,0:px]
  right = add_bottom[:,-px:-1]
  add_left = numpy.concatenate((right,add_bottom),axis=1)
  add_right = numpy.concatenate((add_left,left),axis=1)
  return add_right
#读取图像
img = cv2.imread('./Python/opencv_homework/test.png')
#边缘处理展示
showimg('reflect_padding.png',reflect(img,30))
showimg('move_padding.png',move(img,30))
# 高斯模糊展示
showimg('gauss.png',cv2.filter2D(reflect(img,10),-1,gauss(21,5)))
#高斯函数展示
plt.matshow(gauss(100,1))
plt.show()
plt.matshow(gauss(100,10))
plt.show()