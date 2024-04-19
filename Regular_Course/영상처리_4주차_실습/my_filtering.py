import cv2
import numpy as np
import time
def my_padding(src, pad_size, pad_type='zeros'):
    (h, w) = src.shape
    p_h, p_w = pad_size
    pad_img = np.zeros((h + p_h * 2, w + p_w * 2), dtype=np.uint8)
    pad_img[p_h:h + p_h, p_w:w + p_w] = src

    if pad_type == 'repetition':
        print('repetition padding')
        #up
        pad_img[:p_h, p_w:p_w + w] = src[0, :]
        #down
        pad_img[p_h + h:, p_w:p_w + w] = src[h-1, :]
        #left
        pad_img[:, :p_w] = pad_img[:, p_w:p_w + 1]
        #right
        pad_img[:, p_w + w:] = pad_img[:, p_w + w - 1:p_w + w]

    else:
        # else is zero padding
        print('zero padding')

    return pad_img

def my_filtering(src, kernel, pad_type='zeros'):
    (h, w) = src.shape
    (k_h, k_w) = kernel.shape

    # 직접 구현한 my_padding 함수를 이용
    img_pad = my_padding(???)
    print(f'<img_pad.shape>: {img_pad.shape}')

    dst = ???
    time_start = time.time()
    
    # filtering 진행하는 반복문 구현
    ???
    
    print(f'filtering time: {time.time()-time_start}')

    dst = ??? # float -> uint8 변환

    return dst

if __name__ == '__main__':
    src = cv2.imread('Lena.png', cv2.IMREAD_GRAYSCALE)
    
    # average filter 생성
    kernel = ???
    print('<kernel>')
    print(kernel)

    dst = my_filtering(???)

    print(f'src.shape: {src.shape}')
    print(f'dst.shape: {dst.shape}')

    cv2.imshow('original', src)
    cv2.imshow('dst', dst)

    cv2.waitKey()
    cv2.destroyAllWindows()