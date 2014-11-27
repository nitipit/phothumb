#!/usr/bin/env python

from PIL import Image, ImageFile
from StringIO import StringIO
import sys


def thumbnail(
        image,
        thumb_width=200,
        thumb_max_height=None,
        thumb_format=None):

    # Image.load() wont raise an error if image is truncated
    ImageFile.LOAD_TRUNCATED_IMAGES = True
    # there are some images with exif blocks > 64kB
    ImageFile.MAXBLOCK = 2**20

    if type(image) == 'file':
        image = Image.open(image)
    else:
        try:
            image.format
        except:
            image.close()
            print "Unexpected error:", sys.exc_info()[0]
            raise

    if thumb_format is None:
        thumb_format = image.format

    try:
        exif_orientation = image._getexif()[274]
        if exif_orientation == 6:
            image = image.transpose(Image.ROTATE_270)
    except:
        pass

    thumb_ratio = float(image.size[0]) / thumb_width
    thumb_height = int(image.size[1] / thumb_ratio)
    thumb_size = (thumb_width, thumb_height)
    image.thumbnail(thumb_size, Image.ANTIALIAS)
    if thumb_max_height is None:
        pass
    elif(image.size[1] >= thumb_max_height):
        image = image.crop((0, 0, image.size[0], thumb_max_height))

    tmp_file = StringIO()
    image.save(tmp_file, thumb_format)
    tmp_file.seek(0)
    return tmp_file
