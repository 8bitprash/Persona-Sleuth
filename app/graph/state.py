from typing import Optional, List
from pydantic import BaseModel

class AgentState(BaseModel):
    query_embedding: Optional[List[float]] = None
