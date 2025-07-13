from langgraph.graph import StateGraph
from state import AgentState
from graph.nodes import encode_face_node, ingest_node

workflow = StateGraph(AgentState)
workflow.add_node("ingest", ingest_node)
workflow.add_node("encode_face", encode_face_node)
workflow.add_edge("ingest", "encode_face")
