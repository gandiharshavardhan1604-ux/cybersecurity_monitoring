failed_login_attempts = {}


def analyze_security_event(event):

    event_type = event.event_type.lower()
    message = event.message.lower()

    # --------------------------------------------------
    # 1. Track failed login attempts
    # --------------------------------------------------

    if event_type == "login_failed":

        ip = event.ip_address

        if ip not in failed_login_attempts:
            failed_login_attempts[ip] = 0

        failed_login_attempts[ip] += 1

        attempts = failed_login_attempts[ip]

        # Brute-force detection
        if attempts >= 5:

            return {
                "risk_level": "HIGH",
                "suspicious": True,
                "threat": "Possible Brute-Force Attack",
                "reason": f"{attempts} failed login attempts detected from {ip}.",
                "recommended_action": "Investigate the source IP and consider temporarily blocking it."
            }

        return {
            "risk_level": "MEDIUM",
            "suspicious": True,
            "threat": "Failed Login Attempt",
            "reason": f"Failed login attempt detected. Attempt number: {attempts}.",
            "recommended_action": "Monitor further login attempts."
        }

    # --------------------------------------------------
    # 2. SQL Injection detection
    # --------------------------------------------------

    sql_patterns = [
        "sql injection",
        "union select",
        "' or 1=1",
        "\" or 1=1",
        "drop table",
        "insert into",
        "delete from",
        "select * from"
    ]

    for pattern in sql_patterns:

        if pattern in message:

            return {
                "risk_level": "HIGH",
                "suspicious": True,
                "threat": "Possible SQL Injection",
                "reason": f"The event contains a possible SQL injection pattern: {pattern}.",
                "recommended_action": "Investigate the request and validate input handling."
            }

    # --------------------------------------------------
    # 3. Malware detection
    # --------------------------------------------------

    malware_patterns = [
        "malware",
        "virus detected",
        "trojan",
        "ransomware",
        "worm detected"
    ]

    for pattern in malware_patterns:

        if pattern in message:

            return {
                "risk_level": "CRITICAL",
                "suspicious": True,
                "threat": "Possible Malware Activity",
                "reason": f"The event indicates possible malware activity: {pattern}.",
                "recommended_action": "Investigate the affected system immediately."
            }

    # --------------------------------------------------
    # 4. Unauthorized access detection
    # --------------------------------------------------

    unauthorized_patterns = [
        "unauthorized access",
        "access denied",
        "privilege escalation",
        "permission denied",
        "unauthorized login"
    ]

    for pattern in unauthorized_patterns:

        if pattern in message:

            return {
                "risk_level": "HIGH",
                "suspicious": True,
                "threat": "Possible Unauthorized Access",
                "reason": f"The event contains a possible unauthorized access indicator: {pattern}.",
                "recommended_action": "Verify the user's permissions and investigate the activity."
            }

    # --------------------------------------------------
    # 5. Port scanning detection
    # --------------------------------------------------

    port_scan_patterns = [
        "port scan",
        "port scanning",
        "multiple ports scanned",
        "network scan",
        "nmap scan"
    ]

    for pattern in port_scan_patterns:

        if pattern in message:

            return {
                "risk_level": "HIGH",
                "suspicious": True,
                "threat": "Possible Port Scanning",
                "reason": f"The event indicates possible network scanning: {pattern}.",
                "recommended_action": "Investigate the source IP and review network activity."
            }

    # --------------------------------------------------
    # 6. Suspicious command detection
    # --------------------------------------------------

    command_patterns = [
        "powershell encoded",
        "cmd.exe",
        "reverse shell",
        "command injection",
        "suspicious command"
    ]

    for pattern in command_patterns:

        if pattern in message:

            return {
                "risk_level": "HIGH",
                "suspicious": True,
                "threat": "Possible Command Execution Attack",
                "reason": f"The event contains a suspicious command execution pattern: {pattern}.",
                "recommended_action": "Investigate the command and verify whether the activity was authorized."
            }

    # --------------------------------------------------
    # 7. Account lockout
    # --------------------------------------------------

    if "account locked" in message or "account lockout" in message:

        return {
            "risk_level": "MEDIUM",
            "suspicious": True,
            "threat": "Account Lockout",
            "reason": "The user account was locked, which may indicate repeated failed authentication attempts.",
            "recommended_action": "Review authentication logs and verify whether the lockout was legitimate."
        }

    # --------------------------------------------------
    # 8. Normal event
    # --------------------------------------------------

    return {
        "risk_level": "LOW",
        "suspicious": False,
        "threat": "No Known Threat",
        "reason": "No suspicious pattern was detected.",
        "recommended_action": "No immediate action required."
    }