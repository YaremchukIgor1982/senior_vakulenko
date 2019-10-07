import random

import cv2
import pytest

from PIL import Image
import imagehash

dev = 'http://burganic.smashedmedia.guru/'
uris = [
      '/',
    'about',
    'menu',
    'organic',
    'contact-us',
    'menu-inner',
    'support-local',
    'menu-inner/?step=tab-burgers',
    'menu-inner/?step=tab-salads',
    'menu-inner/?step=tab-sweets'
]


@pytest.mark.parametrize('uri',uris)
def test_Page_UI(app,uri):
        app.open(dev+uri)
        if uri=='/':
                uri='home'
        elif uri=='menu-inner/?step=tab-burgers':
            uri='burgers'
        elif uri == 'menu-inner/?step=tab-salads':
            uri = 'salads'
        elif uri == 'menu-inner/?step=tab-sweets':
            uri = 'others'
        app.fullpage_screenshot('{}.png'.format(str(uri)))
#
#
#
# @pytest.mark.parametrize('uri',uris)
# def test_get_image_difference(uri):
#     image_1_path = '{}.png'.format(str(uri))
#     image_2_path = './mock/{}.png'.format(str(uri))
#     image_1 = cv2.imread(image_1_path, 0)
#     image_2 = cv2.imread(image_2_path, 0)
#     first_image_hist = cv2.calcHist([image_1], [0], None, [256], [0, 256])
#     second_image_hist = cv2.calcHist([image_2], [0], None, [256], [0, 256])
#
#     img_hist_diff = cv2.compareHist(first_image_hist, second_image_hist, cv2.HISTCMP_BHATTACHARYYA)
#     img_template_probability_match = cv2.matchTemplate(first_image_hist, second_image_hist, cv2.TM_CCOEFF_NORMED)[0][0]
#     img_template_diff = 1 - img_template_probability_match
#
#         # taking only 10% of histogram diff, since it's less accurate than template method
#     commutative_image_diff = (img_hist_diff / 10) + img_template_diff
#     if uri=='/':
#         uri='home'
#     print("Page {} ".format(uri)+str(commutative_image_diff*100))
# @pytest.mark.parametrize('uri', uris)
# def test_compare_images():
#     original = cv2.imread('home.png')
#     duplicate = cv2.imread('./mock/home.png')
#     image1 = original.shape
#     image2 = duplicate.shape
#     print(image1)
#     print(image2)
#     cv2.imshow('original',original)
#     cv2.imshow('Mock Up',duplicate)
#
#     cv2.waitKey(0)
#     cv2.destroyAllWindows()
@pytest.mark.parametrize('uri',uris)
def test_compare_hash(uri):

        if uri=='/':
                uri='home'
        hash0 = imagehash.average_hash(Image.open('{}.png'.format(str(uri))))


        hash1 = imagehash.average_hash(Image.open('.\mock\{}.png'.format(uri)))
        print(uri,hash0,hash1)

        cutoff = 5

        if hash0 - hash1 < cutoff:
                print('images are similar')
        else:
                print('images are not similar')
