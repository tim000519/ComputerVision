import cv2
import numpy as np
import matplotlib.pyplot as plt


def generate_sobel_filter():
    ???
    return sobel_x, sobel_y


def calculate_magnitude(sobel_x, sobel_y):
    ???
    return magnitude


def show_images(images, titles):
    fig, axs = plt.subplots(2, 2)

    for image, title, ax in zip(images, titles, axs.flatten()):
        image = image.clip(0, 255)
        ax.imshow(image, cmap='gray')
        ax.set_title(title, y=-0.17, fontsize=18)
        ax.axis('off')

    plt.show()

if __name__ == "__main__":
    ???

    show_images([image, np.abs(gradient_x), magnitude, np.abs(gradient_y)], ['Original', 'x-direction derivative', 'Gradient magnitude', 'y-direction derivative'])
