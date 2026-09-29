from typing import TypedDict

from langgraph.graph import StateGraph, END

from app.database.db import get_db_connection
from app.models.schemas import SecurityEvent
from app.analyzer.rules import analyze_security_event
from app.agent.llm_analyzer import analyze_with_llm


class SecurityState(TypedDict):
    event_type: str
    username: str
    ip_address: str
    message: str

    event_id: int

    risk_level: str
    suspicious: bool
    threat: str
    reason: str
    recommended_action: str

    llm_analysis: str


def analyze_event(state: SecurityState):

    # Create SecurityEvent object
    event = SecurityEvent(
        event_type=state["event_type"],
        username=state["username"],
        ip_address=state["ip_address"],
        message=state["message"]
    )

    # Use rule-based security detection
    analysis = analyze_security_event(event)

    return {
        "risk_level": analysis["risk_level"],
        "suspicious": analysis["suspicious"],
        "threat": analysis["threat"],
        "reason": analysis["reason"],
        "recommended_action": analysis["recommended_action"]
    }


def llm_analysis(state: SecurityState):

    # Create SecurityEvent object
    event = SecurityEvent(
        event_type=state["event_type"],
        username=state["username"],
        ip_address=state["ip_address"],
        message=state["message"]
    )

    # Prepare rule-based analysis
    rule_analysis = {
        "risk_level": state["risk_level"],
        "threat": state["threat"],
        "reason": state["reason"],
        "recommended_action": state["recommended_action"]
    }

    # Send event and rule analysis to Gemini
    analysis = analyze_with_llm(
        event,
        rule_analysis
    )

    return {
        "llm_analysis": analysis
    }


def decide_next_step(state: SecurityState):

    if state["risk_level"] in ["HIGH", "CRITICAL"]:
        return "alert"

    return "normal"


def normal_event(state: SecurityState):

    print("Normal security event detected.")

    return {}


def create_alert(state: SecurityState):

    print("Security alert required!")

    db = get_db_connection()
    cursor = db.cursor()

    query = """
        INSERT INTO security_alerts
        (
            event_id,
            risk_level,
            threat,
            reason,
            recommended_action,
            llm_analysis
        )
        VALUES (%s, %s, %s, %s, %s, %s)
    """

    values = (
        state["event_id"],
        state["risk_level"],
        state["threat"],
        state["reason"],
        state["recommended_action"],
        state["llm_analysis"]
    )

    cursor.execute(query, values)

    db.commit()

    cursor.close()
    db.close()

    print("Security alert saved to MySQL.")

    return {}


graph_builder = StateGraph(SecurityState)

graph_builder.add_node("analyze_event", analyze_event)
graph_builder.add_node("llm_analysis", llm_analysis)
graph_builder.add_node("normal_event", normal_event)
graph_builder.add_node("create_alert", create_alert)

graph_builder.set_entry_point("analyze_event")

graph_builder.add_edge(
    "analyze_event",
    "llm_analysis"
)

graph_builder.add_conditional_edges(
    "llm_analysis",
    decide_next_step,
    {
        "normal": "normal_event",
        "alert": "create_alert"
    }
)

graph_builder.add_edge("normal_event", END)
graph_builder.add_edge("create_alert", END)

security_graph = graph_builder.compile()