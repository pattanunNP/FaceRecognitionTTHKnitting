from pydantic import BaseModel


class ImageRecognitionEvent(BaseModel):

    file_path: str
    original_size: tuple
    new_size: tuple
    new_size_ratio: float
    image: str
    timestamp: float
