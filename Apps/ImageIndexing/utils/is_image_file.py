def is_image_file(filename, extensions=['.jpg', '.jpeg', '.tiff', '.png']):
    return any(filename.endswith(e) for e in extensions)
