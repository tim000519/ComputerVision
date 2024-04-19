import cv2
import numpy as np


def my_naive_downsampling(old_img, ratio_y, ratio_x):
    # old_img의 height와 width
    h_old, w_old = ???

    # new_img의 height와 width
    h_new = ???
    w_new = ???

    # 빈 new_img 선언
    new_img = ???

    # new_img 픽셀 값 채워넣기
    ???

    return new_img


def main():
    # OpenCV를 이용하여 Lena.png를 grayscale로 불러오기
    old_img = ???

    # average 혹은 gaussian filter 만들기
    filter = ???

    # cv2.filter2D 함수를 통해 filtering 혹은
    # 저번주차 과제가 완성되었으면 저번주차 과제 코드로 해보기
    filtered_img = ???

    # my_naive_downsampling 함수를 이용하여 filtered_img를 downsampling
    new_img = ???

    # OpenCV를 이용하여 new_img 저장
    ???

    return

if __name__ == '__main__':
    main()