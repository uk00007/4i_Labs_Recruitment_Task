import cv2
import numpy as np


def show_and_save_image(filtered_img, filter_name, index):

    cv2.imwrite(
        f'4i Labs/image_filter_results/{index}_{filter_name}.jpg', filtered_img)
    cv2.imshow('filtered-img', filtered_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def apply_filter_2D(image_path, kernel=np.array([
    [0, 0, 0],
    [0, 1, 0],
    [0, 0, 0]
])):

    img = cv2.imread(image_path)
    if img is None:
        raise ValueError('Image not found or Invalid path !')

    filtered_img = cv2.filter2D(img, ddepth=-1, kernel=kernel)

    return img, filtered_img


def apply_gaussian_filter(image_path, kernel, sx, sy):
    img = cv2.imread(image_path)
    if img is None:
        raise ValueError('Image not found or Invalid path !')

    filter_img = cv2.GaussianBlur(img, ksize=kernel, sigmaX=sx, sigmaY=sy)

    return img, filter_img


def apply_box_blur(image_path, kernel):
    img = cv2.imread(image_path)
    if img is None:
        raise ValueError('Image not found or Invalid path !')

    blur_img = cv2.blur(img, ksize=kernel)

    return img, blur_img


def apply_bilateral_filter(image_path, d, sigmacolor, sigmaspace):
    img = cv2.imread(image_path)
    if img is None:
        raise ValueError('Image not found or Invalid path !')

    bilateral_filter_img = cv2.bilateralFilter(
        img, d=d, sigmaColor=sigmacolor, sigmaSpace=sigmaspace)

    return img, bilateral_filter_img


def get_edges(img):
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray_img = cv2.GaussianBlur(gray_img, ksize=(3, 3), sigmaX=1, sigmaY=1)

    edges = cv2.Laplacian(gray_img, ddepth=-1)

    return edges


# GaussianBlur for image_1
img, filter_img = apply_gaussian_filter(
    '4i Labs/underwater_images/1.jpg', (7, 7), 0, 0)

frame = show_and_save_image(filter_img, 'GaussianBlur', 1)


# bilateral filter for image_2
img, bilateral_filter_img = apply_bilateral_filter(
    '4i Labs/underwater_images/2.jpg', 5, 200, 200)

frame = show_and_save_image(bilateral_filter_img, 'bilateralFilter', 2)


# edges for image_3
img = cv2.imread('4i Labs/underwater_images/3.jpg')

edges = get_edges(img)

frame = show_and_save_image(edges, 'Laplacian', 3)

# sharpening using filter2D for image_4
sharpen_filter_kernel = np.array([
    [0, -1, 0],
    [-1, 5, -1],
    [0, -1, 0]
])

img, sharp_img = apply_filter_2D(
    '4i Labs/underwater_images/4.jpg', sharpen_filter_kernel)

frame = show_and_save_image(sharp_img, 'filter2D', 4)


# brightening using frame2D for image_1
kernel = np.array([
    [0, 0, 0],
    [0, 1, 0],
    [0, 0, 0]
], np.float16)
kernel *= 1.5
img, brighten_img = apply_filter_2D('4i Labs/underwater_images/1.jpg', kernel)

frame = show_and_save_image(brighten_img, 'filter2D', 1)


# box-blur for image_2
img, blur_img = apply_box_blur('4i Labs/underwater_images/2.jpg', (5, 5))

frame = show_and_save_image(blur_img, 'blur', 2)
