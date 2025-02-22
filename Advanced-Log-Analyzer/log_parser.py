# log_parser.py

import re
from datetime import datetime

# For demonstration, assume log lines follow this format:
# "YYYY-MM-DD HH:MM:SS IP_ADDRESS message"
# Example: "2025-02-22 10:00:00 192.168.1.1 Failed login attempt"

LOG_LINE_REGEX = re.compile(r'(?P<timestamp>\S+\s+\S+)\s+(?P<ip>\d+\.\d+\.\d+\.\d+)\s+(?P<message>.*)')

def parse_log_line(line):
    """
    Parse a single line of the log file and return a dictionary of its components.
    """
    match = LOG_LINE_REGEX.match(line)
    if match:
        try:
            timestamp = datetime.strptime(match.group("timestamp"), "%Y-%m-%d %H:%M:%S")
        except ValueError:
            timestamp = None
        return {
            "timestamp": timestamp,
            "ip": match.group("ip"),
            "message": match.group("message").strip()
        }
    return None

def parse_log_file(logpath):
    """
    Parse an entire log file and return a list of log entries.
    """
    entries = []
    try:
        with open(logpath, "r") as f:
            for line in f:
                entry = parse_log_line(line)
                if entry:
                    entries.append(entry)
    except FileNotFoundError:
        print(f"Log file {logpath} not found.")
    return entries
