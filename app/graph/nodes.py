from services.face_embed import face_to_vector
from fastapi import UploadFile
import io

async def encode_face_node(state):
    if not state.get("is_image"):
        return state
    contents = await state["raw_input"].read()
    try:
        vec = face_to_vector(contents)
    except ValueError as e:
        state["error"] = str(e)
        return state
    state["query_embedding"] = vec
    return state
