from fastapi import FastAPI,Body
from routers import device, link
from db.session import engine
from db.base import Base
from services.ssh import trigger_mininet
from services.llm import explain_topology
import models


Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to Network Dashboard API"}

# Existing routers
app.include_router(device.router)
app.include_router(link.router)

# New endpoint: Trigger Mininet
@app.post("/trigger-topology", tags=["Orchestration"])
def trigger(topo: str = Body(default="single,2")):
    """
    Trigger Mininet with a given topology string.
    Example: "tree,2" or "linear,3"
    """
    output = trigger_mininet(topo)
    return {"status": "success", "topology": topo, "output": output}

# New endpoint: Explain Topology
@app.post("/explain-topology", tags=["LLM"])
def explain(data: dict = Body(...)):
    """
    Explain a topology using LLM.
    Accepts either {"topology": "tree,2"} or {"nodes": ..., "links": ...}
    """
    response = explain_topology(data)
    return {"status": "success", "explanation": response}

# Optional Chat endpoint
@app.post("/chat", tags=["LLM"])
def chat(message: str = Body(..., embed=True)):
    """
    Natural language orchestration.
    Example: "Build tree,2" or "Explain linear,3"
    """
    if "build" in message.lower():
        topo = message.lower().replace("build", "").strip()
        output = trigger_mininet(topo)
        return {
            "status": "success",
            "action": "build_topology",
            "topology": topo,
            "output": output
        }

    elif "explain" in message.lower():
        topo = message.lower().replace("explain", "").strip()
        response = explain_topology({"topology": topo})
        return {
            "status": "success",
            "action": "explain_topology",
            "topology": topo,
            "explanation": response
        }

    else:
        response = explain_topology({"topology": message})
        return {
            "status": "success",
            "action": "chat",
            "message": response
        }

