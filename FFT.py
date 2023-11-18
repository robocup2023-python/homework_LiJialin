import cv2
import numpy as np
img = cv2.imread('test.png',0)#导入
pin_pu = cv2.dft(np.float32(img),flags=cv2.DFT_COMPLEX_OUTPUT)
shift = np.fft.fftshift(pin_pu)#平移
result = 20*np.log(cv2.magnitude(shift[:,:,0],shift[:,:,1]))#映射
fu_du = np.abs(shift)#幅度
fu_du_img = 20*np.log(cv2.magnitude(fu_du[:,:,0],fu_du[:,:,1]))
xiang_wei = np.angle(shift)
xiang_wei_img = 20*np.log(cv2.magnitude(xiang_wei[:,:,0],xiang_wei[:,:,1]))
cv2.imwrite('fudu.png',fu_du_img)
# cv2.imwrite('.png',result)
cv2.imwrite('xiangwei.png',xiang_wei_img)
# img2 = cv2.imread('test2.png',0)#导入
# pin_pu2 = cv2.dft(np.float32(img2),flags=cv2.DFT_COMPLEX_OUTPUT)
# xiang_wei2 = np.angle(pin_pu2)
# img_add = pin_pu*np.e**(1j*pin_pu2)
# # img_add = 20*np.log(cv2.magnitude(img_add0[:,:,0],img_add0[:,:,1]))
# img_out = cv2.idft(img_add)
# cv2.imwrite('相位2.png',img_out)