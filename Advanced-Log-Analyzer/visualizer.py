# visualizer.py

import matplotlib.pyplot as plt

def generate_report(threats):
    """
    Generate a simple visual report of detected threats.
    This function plots the count of threats per source IP and saves the figure.
    """
    if not threats:
        print("No threats to report visually.")
        return

    ip_counts = {}
    for threat in threats:
        # Extract IP from the threat string ("IP - message")
        ip = threat.split(" - ")[0]
        ip_counts[ip] = ip_counts.get(ip, 0) + 1

    ips = list(ip_counts.keys())
    counts = list(ip_counts.values())

    plt.figure(figsize=(8, 6))
    plt.bar(ips, counts, color='red')
    plt.xlabel("IP Address")
    plt.ylabel("Threat Count")
    plt.title("Threats by Source IP")
    plt.tight_layout()
    plt.savefig("threat_report.png")
    plt.show()
    print("Visual report saved as 'threat_report.png'.")
