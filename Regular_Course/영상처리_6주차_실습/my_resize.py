import cv2
import numpy as np

def match_up_coordinates(old_shape, new_shape):
    a_y = ???
    a_x = ???
    b_y = ???
    b_x = ???
    return (a_y, a_x, b_y, b_x)

def my_resize(old_img, new_shape):
    # 빈 배열 만들기
    new_img = ???

    # match_up_coordinates
    a_y, a_x, b_y, b_x = ???

    # new_img의 모든 픽셀 값 채워넣기
    for row in range(???):
        for col in range(???):
            # y, x 좌표 매칭
            y = ???
            x = ???

            # ⌊𝑦⌋, ⌊𝑥⌋, ⌊𝑦+1⌋, ⌊𝑥+1⌋ 구하기
            y_floor = ???
            x_floor = ???
            y_ceil = ???
            x_ceil = ???

            # binary interpolation을 통해 픽셀 값 구하기
            intensity = ???

            new_img[row, col] = round(intensity)

    return new_img

def main():
    old_img = cv2.imread('Lena.png', cv2.IMREAD_GRAYSCALE)
    new_img_1000by1024 = my_resize(old_img, new_shape=(1000, 1024))
    new_img_256by200 = my_resize(old_img, new_shape=(256, 200))
    ??? 'new_img_1000by1024.png'
    ??? 'new_img_256by200.png'

    return

if __name__ == '__main__':
    main()
