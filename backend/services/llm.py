from google import genai
import os

client = genai.Client(api_key=os.getenv("Gemini_API_KEY"))

def explain_topology(data: dict) -> dict:
    """
    Explain an SDN topology using Gemini LLM.
    Accepts either:
      - {"topology": "tree,2"}
      - {"nodes": 4, "links": 3}
    Returns a structured dict with the explanation.
    """

    topo = data.get("topology")
    nodes = data.get("nodes")
    links = data.get("links")

    # Build prompt dynamically
    if topo:
        prompt = f"You are a network engineer. Explain this SDN topology clearly: {topo}"
    elif nodes and links:
        prompt = f"You are a network engineer. Explain this SDN topology clearly:\nNodes: {nodes}\nLinks: {links}"
    else:
        prompt = "You are a network engineer. Explain the given SDN topology clearly."

    # Call Gemini
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    # Return structured output
    return {
        "topology": topo if topo else f"nodes={nodes}, links={links}",
        "explanation": response.text.strip()
    }
