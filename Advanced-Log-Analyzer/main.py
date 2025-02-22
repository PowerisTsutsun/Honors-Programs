# main.py

import argparse
import time
from log_parser import parse_log_file, parse_log_line
from threat_detector import detect_threats
from visualizer import generate_report
from alert_manager import send_alert
from utils import tail_f

def batch_mode(logpath, alert_enabled):
    print("Running in batch mode...")
    log_entries = parse_log_file(logpath)
    threats = detect_threats(log_entries)
    if threats:
        print("Threats detected:")
        for threat in threats:
            print(f" - {threat}")
            if alert_enabled:
                send_alert(threat)
    else:
        print("No threats detected.")
    generate_report(threats)

def realtime_mode(logpath, alert_enabled):
    print("Running in realtime mode...")
    # Continuously monitor the log file for new lines
    for line in tail_f(logpath):
        log_entry = parse_log_line(line)
        if log_entry:
            threats = detect_threats([log_entry])
            if threats:
                for threat in threats:
                    print(f"Real-time threat detected: {threat}")
                    if alert_enabled:
                        send_alert(threat)
                    
def main():
    parser = argparse.ArgumentParser(description="Advanced Log Analysis and Threat Detection Tool")
    parser.add_argument("--logpath", required=True, help="Path to the log file to analyze")
    parser.add_argument("--mode", choices=["batch", "realtime"], default="batch", help="Operation mode: batch or realtime")
    parser.add_argument("--alert", action="store_true", help="Enable alert notifications")
    args = parser.parse_args()
    
    if args.mode == "batch":
        batch_mode(args.logpath, args.alert)
    elif args.mode == "realtime":
        realtime_mode(args.logpath, args.alert)

if __name__ == "__main__":
    main()
