from collections import deque

import cv2
import numpy as np


def min_max_scaling(src):
    return 255 * ((src - src.min()) / (src.max() - src.min()))


def get_DoG_filter(fsize, sigma):
    DoG_x = np.zeros((fsize, fsize), np.float64)
    DoG_y = np.zeros((fsize, fsize), np.float64)
    half = fsize // 2
    for y in range(-half, half + 1):
        for x in range(-half, half + 1):
            DoG_x[y + half, x + half] = (-x / (2 * np.pi * sigma ** 4)) * np.exp(
                -((x ** 2 + y ** 2) / (2 * sigma ** 2)))
            DoG_y[y + half, x + half] = (-y / (2 * np.pi * sigma ** 4)) * np.exp(
                -((x ** 2 + y ** 2) / (2 * sigma ** 2)))

    return DoG_x, DoG_y


def calculate_magnitude(gradient_x, gradient_y):
    magnitude = np.sqrt(gradient_x ** 2 + gradient_y ** 2)
    return magnitude


def non_maximum_suppression(gradient_x, gradient_y, magnitude, n):
    ???

    return large_magnitude


def double_thresholding(nms_result, high_threshold, low_threshold):
    ???

    return thresholding_result


def determine_edge(thresholding_result):
    ???

    return canny_edge_result


def main():
    image = cv2.imread('noise_Lena.png', cv2.IMREAD_GRAYSCALE).astype(np.float32)

    DoG_x, DoG_y = get_DoG_filter(fsize=5, sigma=1)
    gradient_y = cv2.filter2D(image, -1, DoG_y)
    gradient_x = cv2.filter2D(image, -1, DoG_x)
    magnitude = calculate_magnitude(gradient_x=gradient_x, gradient_y=gradient_y)
    nms_result = non_maximum_suppression(gradient_x=gradient_x, gradient_y=gradient_y, magnitude=magnitude, n=5)
    thresholding_result = double_thresholding(nms_result=nms_result, high_threshold=10, low_threshold=4)
    canny_edge_result = determine_edge(thresholding_result=thresholding_result)

    cv2.imwrite('magnitude.png', min_max_scaling(magnitude))
    cv2.imwrite('nms.png', min_max_scaling(nms_result))
    cv2.imwrite('thresholding.png', thresholding_result)
    cv2.imwrite('canny_edge.png', canny_edge_result)


if __name__ == '__main__':
    main()