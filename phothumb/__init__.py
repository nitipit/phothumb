#!/usr/bin/env python

from PIL import Image, ImageFile
import io
import sys


def _thumbnail(
        image,
        width,
        max_height=None,
        f=None,
        t=0):

    # Image.load() wont raise an error if image is truncated
    ImageFile.LOAD_TRUNCATED_IMAGES = True
    # there are some images with exif blocks > 64kB
    ImageFile.MAXBLOCK = 2**20

    try:
        image = Image.open(image)
    except:
        image.close()
        print("Unexpected error:", sys.exc_info()[0])
        raise

    if f is None:
        f = image.format

    try:
        exif_orientation = image._getexif()[274]
        if exif_orientation == 6:
            image = image.transpose(Image.ROTATE_270)
    except:
        pass

    ratio = float(image.size[0]) / width
    height = int(image.size[1] / ratio)
    size = (width, height)
    image.thumbnail(size, Image.ANTIALIAS)
    if max_height is None:
        pass
    elif(image.size[1] >= max_height):
        image = image.crop((0, 0, image.size[0], max_height))

    if t == 1:
        return image

    tmp_file = io.BytesIO()
    image.save(tmp_file, f)
    tmp_file.seek(0)
    return tmp_file

def get_bytes(image, width, max_height=None, f=None):
    return _thumbnail(image, width, max_height, f, t=0)

def get(image, width, max_height=None, f=None):
    return _thumbnail(image, width, max_height, f, t=1)
