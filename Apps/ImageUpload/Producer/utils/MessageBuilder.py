def BuildMessage(
        file_path: str,
        original_size: tuple,
        new_size: tuple,
        new_size_ratio: float,
        b64_image):
    return {
        "file_path": file_path,
        "original_size": original_size,
        "new_size": new_size,
        "new_size_ratio": new_size_ratio,
        "b64_image": b64_image
    }
