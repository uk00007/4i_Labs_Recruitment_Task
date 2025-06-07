import cv2
import numpy as np


def find_digits(img_path, template_folder_name):

    img = cv2.imread(img_path, 0)
    methods = [cv2.TM_CCOEFF, cv2.TM_CCOEFF_NORMED, cv2.TM_CCORR,
               cv2.TM_CCORR_NORMED, cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]

    for i in range(10):
        template = cv2.imread(
            f'4i Labs/Digit_Dataset/{template_folder_name}/{i}.png', 0)
        height, width = template.shape

        count = 0
        for method in methods:
            img2 = img.copy()
            result = cv2.matchTemplate(img2, template, method)

            min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

            if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
                location = min_loc
            else:
                location = max_loc

            right_corner_loc = (location[0]+width, location[1]+height)

            cv2.rectangle(img2, location, right_corner_loc, 0, 3)

            cv2.imwrite(
                f'4i Labs/template_matching_results/digit{i}_{template_folder_name}_{count}.png', img2)
            count += 1

            cv2.waitKey(0)
            cv2.destroyAllWindows()


find_digits('4i Labs/Digit_Dataset/templete.png', 'Arial')
find_digits('4i Labs/Digit_Dataset/templeteT.png', 'ArialT')
