# -*- coding: utf-8 -*-

import cv2


def make_background_foggy(image_cv2):
    """
    draw background for foggy
    :param image_cv2: img cv2
    :return: None
    """
    for y in range(image_cv2.shape[0]):
        cv2.line(image_cv2, (0, y), (image_cv2.shape[1], y), (144, 144, 144), 1)


def make_background_cloudy(image_cv2):
    """
    draw background for cloudy
    :param image_cv2: img cv2
    :return: None
    """
    for y in range(image_cv2.shape[0]):
        pix = 255 - .5 * y if y <= 254 else 128
        cv2.line(image_cv2, (0, y), (image_cv2.shape[1], y), (pix, pix, pix), 1)


def make_background_rain(image_cv2):
    """
    draw background for rain
    :param image_cv2: img cv2
    :return: None
    """
    for y in range(image_cv2.shape[0]):
        pix_blue = 173 + .5 * y if y <= 164 else 255
        pix = 173 - .5 * y if y <= 146 else 100
        cv2.line(image_cv2, (0, y), (image_cv2.shape[1], y), (int(pix_blue), int(pix), int(pix)), 1)


def make_background_overcast(image_cv2):
    """
    draw background for overcast
    :param image_cv2: img cv2
    :return: None
    """
    for y in range(image_cv2.shape[0]):
        pix = 128 + .5 * y if y <= 254 else 255
        cv2.line(image_cv2, (0, y), (image_cv2.shape[1], y), (pix, pix, pix), 1)


def make_background_snow(image_cv2):
    """
    draw background for snow
    :param image_cv2: img cv2
    :return: None
    """
    for y in range(image_cv2.shape[0]):
        pix = 255 - y if y <= 255 else 0
        cv2.line(image_cv2, (0, y), (image_cv2.shape[1], y), (255, 255, pix), 1)


def make_background_clear(image_cv2):
    """
    draw background for clear
    :param image_cv2: img cv2
    :return: None
    """
    for y in range(image_cv2.shape[0]):
        pix = y if y <= 255 else 255
        cv2.line(image_cv2, (0, y), (image_cv2.shape[1], y), (pix, 255, 255), 1)


def make_background_windy(image_cv2):
    """
    draw background for windy
    :param image_cv2: img cv2
    :return: None
    """
    for x in range(image_cv2.shape[1]):
        pix = 255 - 2 * x if x <= 122 else 0
        cv2.line(image_cv2, (x, 0), (x, image_cv2.shape[0]), (255, 255, pix), 1)
