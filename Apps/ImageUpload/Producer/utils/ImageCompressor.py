import os
from loguru import logger
from PIL import Image


def get_size_format(b, factor=1024, suffix="B"):
    """
    Scale bytes to its proper byte format
    e.g:
        1253656 => '1.20MB'
        1253656678 => '1.17GB'
    """
    for unit in ["", "K", "M", "G", "T", "P", "E", "Z"]:
        if b < factor:
            return f"{b:.2f}{unit}{suffix}"
        b /= factor
    return f"{b:.2f}Y{suffix}"


def compress_img(image_name, new_size_ratio=0.5, width=None, height=None):
    # load the image to memory
    img = Image.open(image_name)
    # print the original image shape
    original_size = img.size
    logger.info(f"[*] Image shape:{img.size}")
    # get the original image size in bytes
    image_size = os.path.getsize(image_name)
    # print the size before compression/resizing
    logger.info(f"[*] Size before compression:{get_size_format(image_size)}")
    if new_size_ratio < 1.0:
        # if resizing ratio is below 1.0, then multiply width & height with this ratio to reduce image size
        img = img.resize((int(img.size[0] * new_size_ratio), int(img.size[1] * new_size_ratio)), Image.ANTIALIAS)
        # print new image shape
        logger.info(f"[*] Image shape:{img.size}")
        return img, new_size_ratio,original_size ,img.size
    elif width and height:
        # if width and height are set, resize with them instead
        img = img.resize((width, height), Image.ANTIALIAS)
        # print new image shape
        logger.info(f"[*] Image shape:{img.size}")
        return img, new_size_ratio, original_size, img.size
