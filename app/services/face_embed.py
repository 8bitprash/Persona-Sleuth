from deepface import DeepFace
import numpy as np

def face_to_vector(image_bytes: bytes) -> list[float]:
    """
    Raises ValueError if no face detected.
    """
    embedding_objs = DeepFace.represent(
        img_path=image_bytes,
        model_name="Facenet512",
        enforce_detection=True
    )
    if not embedding_objs:
        raise ValueError("No face detected")
    return embedding_objs[0]["embedding"]
