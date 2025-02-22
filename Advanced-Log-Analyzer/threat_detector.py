# threat_detector.py

def detect_threats(log_entries):
    """
    Analyze log entries and return a list of detected threats.
    For demonstration, any log message containing 'failed login' or 'unauthorized' is flagged as a threat.
    """
    threats = []
    for entry in log_entries:
        message = entry.get("message", "").lower()
        if "failed login" in message or "unauthorized" in message:
            threat = f"{entry.get('ip')} - {entry.get('message')}"
            threats.append(threat)
    return threats
