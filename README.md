# 🛡️ Cybersecurity Monitoring Agent

> **An Agentic AI-powered security monitoring system that analyzes security events, detects suspicious activity, assesses risk, and generates actionable security alerts.**

![Python](https://img.shields.io/badge/Python-3.14-blue?logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-0.141.1-009688?logo=fastapi)
![LangGraph](https://img.shields.io/badge/LangGraph-Agentic%20AI-orange)
![Google Gemini](https://img.shields.io/badge/Google%20Gemini-LLM-4285F4?logo=google)
![MySQL](https://img.shields.io/badge/MySQL-8.0.46-4479A1?logo=mysql)
![License](https://img.shields.io/badge/License-MIT-green)

---

## 📌 Overview

**Cybersecurity Monitoring Agent** is an Agentic AI-based security monitoring application designed to analyze security events and identify potentially suspicious activities.

The system combines:

* 🔍 Rule-based threat detection
* 🤖 Large Language Model analysis
* 🧠 LangGraph-based agent workflow
* ⚡ FastAPI backend
* 🗄️ MySQL database
* 📊 Real-time security dashboard

Security events can be submitted through the dashboard. The system analyzes each event, determines its risk level, identifies potential threats, generates recommended actions, and stores security information in MySQL.

---

## 🎯 Objectives

The main objectives of this project are to:

* Monitor security-related events.
* Detect suspicious activity automatically.
* Identify common cybersecurity threats.
* Assign appropriate risk levels.
* Generate security recommendations.
* Use AI to provide additional event analysis.
* Store events and alerts in a relational database.
* Provide a centralized monitoring dashboard.

---

# 🚀 Key Features

### 🔐 Security Event Monitoring

The system accepts security events containing:

* Event type
* Username
* IP address
* Security message

Example:

```text
Event Type: login_failed
Username: admin
IP Address: 10.0.0.99
Message: Failed login attempt
```

---

### 🧠 Rule-Based Threat Detection

The detection engine identifies several common security patterns, including:

| Threat              | Detection                                        |
| ------------------- | ------------------------------------------------ |
| Brute-Force Attack  | Multiple failed login attempts                   |
| SQL Injection       | SQL injection patterns                           |
| Malware Activity    | Malware, ransomware, trojan indicators           |
| Unauthorized Access | Unauthorized login/access indicators             |
| Port Scanning       | Network scanning indicators                      |
| Command Execution   | Suspicious PowerShell/CMD/reverse shell patterns |
| Account Lockout     | Account lockout indicators                       |

---

### 🤖 Agentic AI Analysis

The project uses **LangGraph** to organize the security analysis workflow.

The agent:

1. Receives the security event.
2. Performs rule-based analysis.
3. Sends the event and rule analysis to the LLM.
4. Generates an additional AI-based security assessment.
5. Determines whether an alert is required.
6. Stores high-risk alerts in MySQL.

If the LLM service is unavailable, the system automatically falls back to rule-based analysis.

---

### ⚠️ Risk Classification

Security events are classified into different risk levels:

| Risk Level  | Meaning                                                     |
| ----------- | ----------------------------------------------------------- |
| 🟢 LOW      | No known suspicious activity                                |
| 🟡 MEDIUM   | Activity requiring monitoring                               |
| 🟠 HIGH     | Potential security threat                                   |
| 🔴 CRITICAL | Serious security activity requiring immediate investigation |

---

### 📊 Security Dashboard

The web dashboard provides:

* Total security events
* Total alerts
* Critical alerts
* High alerts
* Event analysis interface
* AI analysis results
* Recent security alerts
* Complete security event history

---

### 🗄️ MySQL Database

The system stores security information in MySQL.

Main tables:

```text
security_events
security_alerts
```

### `security_events`

Stores incoming security events.

```text
id
event_type
username
ip_address
message
created_at
```

### `security_alerts`

Stores detected security threats.

```text
id
event_id
risk_level
threat
reason
recommended_action
llm_analysis
created_at
```

---

# 🏗️ System Architecture

```text
                    ┌──────────────────────┐
                    │   Security Event     │
                    │      / Dashboard     │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │      FastAPI         │
                    │       Backend        │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │    LangGraph Agent   │
                    └──────────┬───────────┘
                               │
                    ┌──────────▼───────────┐
                    │  Rule-Based Analyzer │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │    Gemini LLM        │
                    │   AI Analysis        │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │   Risk Assessment    │
                    │  & Alert Decision    │
                    └──────────┬───────────┘
                               │
                    ┌──────────▼───────────┐
                    │       MySQL          │
                    │ Events & Alerts      │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │  Security Dashboard  │
                    └──────────────────────┘
```

---

# 🔄 Agent Workflow

The LangGraph workflow follows this process:

```text
                    Security Event
                          │
                          ▼
                  ┌───────────────┐
                  │ Analyze Event │
                  └───────┬───────┘
                          │
                          ▼
                  ┌───────────────┐
                  │  LLM Analysis │
                  └───────┬───────┘
                          │
                          ▼
                  ┌────────────────┐
                  │ Risk Decision  │
                  └───────┬────────┘
                          │
                ┌─────────┴─────────┐
                │                   │
                ▼                   ▼
          Normal Event          High/Critical
                │                   │
                ▼                   ▼
               END            Create Alert
                                    │
                                    ▼
                                   END
```

---

# 🛠️ Technology Stack

## Backend

* **Python**
* **FastAPI**
* **Uvicorn**

## Agentic AI

* **LangGraph**
* **LangChain**
* **Google Gemini**
* **LLM-based security analysis**

## Database

* **MySQL 8.0**

## Frontend

* **HTML5**
* **CSS3**
* **JavaScript**

## Development Tools

* **Visual Studio Code**
* **Git**
* **GitHub**
* **PowerShell**

---

# 📁 Project Structure

```text
cybersecurity-monitoring-agent/
│
├── app/
│   │
│   ├── agent/
│   │   ├── __init__.py
│   │   ├── graph.py
│   │   └── llm_analyzer.py
│   │
│   ├── analyzer/
│   │   ├── __init__.py
│   │   └── rules.py
│   │
│   ├── database/
│   │   ├── __init__.py
│   │   └── db.py
│   │
│   ├── models/
│   │   ├── __init__.py
│   │   └── schemas.py
│   │
│   ├── static/
│   │   ├── script.js
│   │   └── style.css
│   │
│   ├── templates/
│   │   └── index.html
│   │
│   ├── __init__.py
│   └── main.py
│
├── .gitignore
├── README.md
├── requirements.txt
└── .env
```

> **Note:** `.env` is intentionally excluded from Git because it contains private credentials and API keys.

---

# ⚙️ Installation

## 1. Clone the Repository

```bash
git clone https://github.com/gandiharshavardhan1604-ux/cybersecurity_monitoring.git
```

Navigate into the project:

```bash
cd cybersecurity_monitoring
```

---

## 2. Create a Virtual Environment

### Windows

```powershell
python -m venv venv
```

Activate it:

```powershell
venv\Scripts\activate
```

---

## 3. Install Dependencies

```powershell
pip install -r requirements.txt
```

---

# 🗄️ Database Configuration

Make sure MySQL Server is installed and running.

Create the database:

```sql
CREATE DATABASE cybersecurity_agent;
```

Select the database:

```sql
USE cybersecurity_agent;
```

Create the security events table:

```sql
CREATE TABLE security_events (
    id INT AUTO_INCREMENT PRIMARY KEY,
    event_type VARCHAR(100) NOT NULL,
    username VARCHAR(100),
    ip_address VARCHAR(45) NOT NULL,
    message TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

Create the security alerts table:

```sql
CREATE TABLE security_alerts (
    id INT AUTO_INCREMENT PRIMARY KEY,
    event_id INT NOT NULL,
    risk_level VARCHAR(20) NOT NULL,
    threat VARCHAR(255),
    reason TEXT,
    recommended_action TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    llm_analysis TEXT,
    FOREIGN KEY (event_id) REFERENCES security_events(id)
);
```

---

# 🔑 Environment Variables

Create a `.env` file in the project root.

```env
DB_HOST=localhost
DB_USER=root
DB_PASSWORD=YOUR_MYSQL_PASSWORD
DB_NAME=cybersecurity_agent

GEMINI_API_KEY=YOUR_GEMINI_API_KEY
GEMINI_MODEL=gemini-3.8-flash
```

### ⚠️ Security Notice

Never commit your `.env` file to GitHub.

The `.gitignore` file already excludes it:

```text
.env
venv/
__pycache__/
*.pyc
```

---

# ▶️ Running the Application

Start the FastAPI server:

```powershell
uvicorn app.main:app --reload
```

The API will run at:

```text
http://127.0.0.1:8000
```

Open the dashboard:

```text
http://127.0.0.1:8000/dashboard
```

---

# 🔌 API Endpoints

| Method | Endpoint           | Description                   |
| ------ | ------------------ | ----------------------------- |
| GET    | `/`                | Application status            |
| GET    | `/health`          | Health check                  |
| GET    | `/dashboard`       | Security dashboard            |
| POST   | `/analyze`         | Analyze a security event      |
| GET    | `/events`          | Retrieve security events      |
| GET    | `/alerts`          | Retrieve security alerts      |
| GET    | `/dashboard/stats` | Retrieve dashboard statistics |

---

# 🧪 Example Security Event

### Request

```http
POST /analyze
```

```json
{
    "event_type": "login_failed",
    "username": "admin",
    "ip_address": "10.0.0.99",
    "message": "Failed login attempt"
}
```

### Example Analysis

```json
{
    "risk_level": "HIGH",
    "suspicious": true,
    "threat": "Possible Brute-Force Attack",
    "reason": "Multiple failed login attempts detected.",
    "recommended_action": "Investigate the source IP and consider temporarily blocking it."
}
```

---

# 🔍 Supported Detection Examples

### Brute-Force Detection

```text
Event Type:
login_failed

Message:
Failed login attempt
```

Repeated attempts from the same IP can increase the risk level.

### SQL Injection

```text
Message:
Possible SQL injection: UNION SELECT detected
```

### Malware

```text
Event Type:
malware_detected

Message:
Ransomware detected on system
```

### Unauthorized Access

```text
Message:
Unauthorized access detected
```

### Port Scanning

```text
Message:
Multiple ports scanned from external IP
```

### Suspicious Command Execution

```text
Message:
PowerShell encoded command detected
```

---

# 🤖 AI Analysis

The LLM receives the security event together with the rule-based analysis.

It is instructed to provide:

1. Threat assessment
2. Explanation of suspicious behavior
3. Recommended security action

The system is designed to avoid relying exclusively on the LLM. Rule-based detection provides a deterministic baseline, while the LLM adds contextual analysis.

If the LLM service is unavailable, the application continues operating using the rule-based security analysis.

---

# 🛡️ Security Considerations

This project is designed as an educational cybersecurity monitoring system.

Recommended production improvements include:

* Authentication and authorization
* HTTPS/TLS
* API rate limiting
* Input validation
* Secure secret management
* Centralized logging
* Database connection pooling
* Role-based access control
* Alert deduplication
* IP reputation analysis
* SIEM integration
* Audit logging
* Production-grade LLM error handling

---

# 🚧 Future Enhancements

Planned improvements include:

* [ ] Real-time event streaming
* [ ] WebSocket-based live alerts
* [ ] Advanced threat correlation
* [ ] IP reputation lookup
* [ ] GeoIP analysis
* [ ] Authentication and user management
* [ ] Role-based dashboard access
* [ ] Alert acknowledgment
* [ ] Alert severity filtering
* [ ] Event search and filtering
* [ ] Pagination
* [ ] Security analytics charts
* [ ] Email notifications
* [ ] Telegram/WhatsApp notifications
* [ ] SIEM integration
* [ ] Docker deployment
* [ ] Automated security report generation

---

# 📈 Project Workflow

```text
User / Security Source
          │
          ▼
    Security Event
          │
          ▼
      FastAPI API
          │
          ▼
    Store Event in DB
          │
          ▼
     LangGraph Agent
          │
          ├───────────────┐
          ▼               ▼
   Rule Analyzer      Gemini LLM
          │               │
          └───────┬───────┘
                  ▼
           Risk Assessment
                  │
          ┌───────┴───────┐
          ▼               ▼
        Normal          Suspicious
          │               │
          ▼               ▼
         END        Create Alert
                          │
                          ▼
                    MySQL Storage
                          │
                          ▼
                  Security Dashboard
```

---

# 🎓 Project Type

**Project:** Cybersecurity Monitoring Agent

**Category:** Agentic AI / Cybersecurity

**Primary Language:** Python

**Architecture:** FastAPI + LangGraph + MySQL + Gemini

**Purpose:** Security event monitoring, threat detection, risk assessment, and AI-assisted alert generation.

---

# 👨‍💻 Author

**Gandi Harsha Vardhan**

AI-focused Computer Science Undergraduate

* GitHub: [@gandiharshavardhan1604-ux](https://github.com/gandiharshavardhan1604-ux)

---

# 📄 License

This project is licensed under the **MIT License**.

See the `LICENSE` file for details.

---

## ⭐ Acknowledgement

This project was developed as an **Agentic AI cybersecurity monitoring application**, combining deterministic security rules with LLM-assisted analysis and an interactive monitoring dashboard.

If you find the project useful, consider giving the repository a ⭐ on GitHub.
