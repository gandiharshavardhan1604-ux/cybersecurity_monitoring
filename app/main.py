from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from app.models.schemas import SecurityEvent
from app.database.db import get_db_connection
from app.agent.graph import security_graph


app = FastAPI(
    title="Cybersecurity Monitoring Agent",
    description="Agentic AI system for monitoring and analyzing security events",
    version="1.0.0"
)


# ==========================================
# Frontend Configuration
# ==========================================

app.mount(
    "/static",
    StaticFiles(directory="app/static"),
    name="static"
)

templates = Jinja2Templates(
    directory="app/templates"
)


# ==========================================
# Home
# ==========================================

@app.get("/")
def home():

    return {
        "message": "Cybersecurity Monitoring Agent is running"
    }


# ==========================================
# Health Check
# ==========================================

@app.get("/health")
def health():

    return {
        "status": "healthy"
    }


# ==========================================
# Dashboard
# ==========================================

@app.get("/dashboard", response_class=HTMLResponse)
def dashboard(request: Request):

    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={
            "request": request
        }
    )


# ==========================================
# Analyze Security Event
# ==========================================

@app.post("/analyze")
def analyze_event(event: SecurityEvent):

    # --------------------------------
    # 1. Save event to MySQL
    # --------------------------------

    db = get_db_connection()
    cursor = db.cursor()

    event_query = """
        INSERT INTO security_events
        (event_type, username, ip_address, message)
        VALUES (%s, %s, %s, %s)
    """

    event_values = (
        event.event_type,
        event.username,
        event.ip_address,
        event.message
    )

    cursor.execute(event_query, event_values)

    event_id = cursor.lastrowid

    db.commit()

    cursor.close()
    db.close()


    # --------------------------------
    # 2. Create LangGraph state
    # --------------------------------

    state = {
        "event_type": event.event_type,
        "username": event.username,
        "ip_address": event.ip_address,
        "message": event.message,

        "event_id": event_id,

        "risk_level": "",
        "suspicious": False,
        "threat": "",
        "reason": "",
        "recommended_action": "",

        "llm_analysis": ""
    }


    # --------------------------------
    # 3. Run LangGraph Agent
    # --------------------------------

    result = security_graph.invoke(state)


    # --------------------------------
    # 4. Return result
    # --------------------------------

    return {

        "event": event,

        "analysis": {

            "risk_level": result["risk_level"],

            "suspicious": result["suspicious"],

            "threat": result["threat"],

            "reason": result["reason"],

            "recommended_action":
                result["recommended_action"],

            "llm_analysis":
                result["llm_analysis"]
        },

        "event_id": event_id
    }


# ==========================================
# Get Recent Events
# ==========================================

@app.get("/events")
def get_events():

    db = get_db_connection()

    cursor = db.cursor(dictionary=True)

    query = """
        SELECT *
        FROM security_events
        ORDER BY id DESC
        LIMIT 50
    """

    cursor.execute(query)

    events = cursor.fetchall()

    cursor.close()

    db.close()

    return {
        "events": events
    }


# ==========================================
# Get Recent Alerts
# ==========================================

@app.get("/alerts")
def get_alerts():

    db = get_db_connection()

    cursor = db.cursor(dictionary=True)

    query = """
        SELECT *
        FROM security_alerts
        ORDER BY id DESC
        LIMIT 50
    """

    cursor.execute(query)

    alerts = cursor.fetchall()

    cursor.close()

    db.close()

    return {
        "alerts": alerts
    }


# ==========================================
# Dashboard Statistics
# ==========================================

@app.get("/dashboard/stats")
def get_dashboard_stats():

    db = get_db_connection()

    cursor = db.cursor(dictionary=True)


    # --------------------------------
    # Total Events
    # --------------------------------

    cursor.execute("""
        SELECT COUNT(*) AS total_events
        FROM security_events
    """)

    total_events = cursor.fetchone()["total_events"]


    # --------------------------------
    # Total Alerts
    # --------------------------------

    cursor.execute("""
        SELECT COUNT(*) AS total_alerts
        FROM security_alerts
    """)

    total_alerts = cursor.fetchone()["total_alerts"]


    # --------------------------------
    # Critical Alerts
    # --------------------------------

    cursor.execute("""
        SELECT COUNT(*) AS critical_alerts
        FROM security_alerts
        WHERE risk_level = 'CRITICAL'
    """)

    critical_alerts = cursor.fetchone()["critical_alerts"]


    # --------------------------------
    # High Alerts
    # --------------------------------

    cursor.execute("""
        SELECT COUNT(*) AS high_alerts
        FROM security_alerts
        WHERE risk_level = 'HIGH'
    """)

    high_alerts = cursor.fetchone()["high_alerts"]


    cursor.close()

    db.close()


    return {

        "total_events": total_events,

        "total_alerts": total_alerts,

        "critical_alerts": critical_alerts,

        "high_alerts": high_alerts
    }