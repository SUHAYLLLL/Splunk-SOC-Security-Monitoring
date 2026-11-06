
import csv
import random
from datetime import datetime, timedelta, timezone

random.seed(42)

OUTPUT_FILE = "data/security_logs.csv"
START_TIME = datetime(2026, 11, 6, 9, 0, tzinfo=timezone.utc)

users = ["admin", "james", "sarah", "michael", "emma"]
normal_ips = ["192.0.2.10", "192.0.2.20", "192.0.2.30"]
suspicious_ip = "203.0.113.50"

events = []

# Generate normal authentication activity
for i in range(170):
    timestamp = START_TIME + timedelta(seconds=i * 20)

    events.append({
        "timestamp": timestamp.isoformat(),
        "username": random.choice(users),
        "source_ip": random.choice(normal_ips),
        "event_type": random.choices(
            ["LOGIN_SUCCESS", "LOGIN_FAILED"],
            weights=[85, 15]
        )[0],
        "system": "corporate-portal"
    })

# Generate a simulated brute-force attack
for i in range(30):
    timestamp = START_TIME + timedelta(hours=2, seconds=i * 2)

    events.append({
        "timestamp": timestamp.isoformat(),
        "username": "admin",
        "source_ip": suspicious_ip,
        "event_type": "LOGIN_FAILED",
        "system": "corporate-portal"
    })

# Sort events chronologically
events.sort(key=lambda event: event["timestamp"])

# Export events to CSV
with open(OUTPUT_FILE, "w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(
        file,
        fieldnames=[
            "timestamp",
            "username",
            "source_ip",
            "event_type",
            "system"
        ]
    )
    writer.writeheader()
    writer.writerows(events)

print(f"Generated {len(events)} security events.")
print(f"Saved to {OUTPUT_FILE}")
