import cv2
import numpy as np
from PIL import Image

import pytesseract



def Corver_Gray(image_path):
    # 读取模板图像
    img = cv2.imread(image_path)
    # 图像放大
    x,y=img.shape[0:2]
    ref=cv2.resize(img,(int(y*2),int(x*2)))
    cv2.imshow('resize', ref)
    cv2.waitKey()
    # 转换为灰度图 也可读取时直接转换
    ref = cv2.cvtColor(ref, cv2.COLOR_BGR2GRAY)
    cv2.imshow('gray',ref)
    cv2.waitKey()

    # 转换成二值图像
    # ref = cv2.threshold(ref, 127, 255, cv2.THRESH_BINARY_INV)[1]
    ref = cv2.threshold(ref, 127, 255, cv2.THRESH_BINARY)[1]
    cv2.imshow('binary', ref)
    cv2.waitKey()
    # # 均值滤波
    # ref=cv2.blur(ref,ksize=[1,1])
    # cv2.imshow('mean', ref)
    # cv2.waitKey()
    # # 膨胀
    # ref=cv2.dilate(ref,kernel=np.ones((1,1),dtype=np.uint8),iterations=1)
    # cv2.imshow('dilate', ref)
    # cv2.waitKey()
    # # 腐蚀
    # ref=cv2.erode(ref,kernel=np.ones((1,1),dtype=np.uint8),iterations=1)
    # cv2.imshow('erod', ref)
    # cv2.waitKey()
    return ref


def Read_Img(img_path):
    image = Corver_Gray(img_path)
    image = cv2.imwrite("test.png", image)
    return image

if __name__ == '__main__':
    img_path=r'D:\chepaijiance\yolov5-7.0\runs\detect\exp10\crops\license-plate\fed5c0275ff3a440_jpg.rf.e5109ca74608d31d401d0d1e6e8e6ad92.jpg'
    # img_path=r'D:\chepaijiance\yolov5-7.0\runs\detect\exp10\crops\license-plate\f5128e7a123b4fa8_jpg.rf.f0b1b11e39538a41d4cf9793804ed4123.jpg'
    # img_path=r'D:\chepaijiance\yolov5-7.0\runs\detect\exp10\crops\license-plate\f6256bceaf66693f_jpg.rf.3d5dc6962e641d544cbf59697833caa6.jpg'


    Read_Img(img_path)


    # text = pytesseract.image_to_string(Image.open("test.png"), lang="chi_sim")
    img=Image.open("test.png")
    img.show()
    lang='eng'  # ['chi_sim', 'chi_sim_vert', 'chi_tra', 'chi_tra_vert', 'eng', 'osd']
    text = pytesseract.image_to_string(img,lang=lang)
    print(text)
