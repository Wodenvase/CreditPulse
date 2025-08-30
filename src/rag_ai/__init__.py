import random

# Simulated knowledge base
knowledge_base = [
    {"bond_id": "ACME2025", "event": "Downgrade", "details": "Moody's downgraded Acme Corp to A- in 2024."},
    {"bond_id": "ACME2025", "event": "Spread Widening", "details": "Spread widened by 30bps after Q2 earnings."},
    {"bond_id": "XYZ2030", "event": "Upgrade", "details": "S&P upgraded XYZ Inc. to AA in 2023."},
    {"bond_id": "XYZ2030", "event": "Regulatory", "details": "New capital requirements introduced for sector in 2024."},
]

def retrieve_insights(bond_data):
    """
    Retrieve relevant insights from the knowledge base for a given bond.
    """
    bond_id = bond_data.get("bond_id")
    relevant = [item for item in knowledge_base if item["bond_id"] == bond_id]
    if not relevant:
        return "No recent events or insights found for this bond."
    # Simulate LLM-generated explanation
    explanations = []
    for item in relevant:
        explanation = generate_llm_explanation(item)
        explanations.append(explanation)
    return explanations

def generate_llm_explanation(event):
    """
    Simulate LLM-generated human-like explanation for an event.
    """
    templates = [
        f"Recent event: {event['event']}. Details: {event['details']}",
        f"Insight: {event['details']} (Event: {event['event']})",
        f"Update for bond: {event['event']} - {event['details']}"
    ]
    return random.choice(templates)