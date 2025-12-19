

import csv
import random
from datetime import datetime, timedelta

# -----------------------------
# CONFIGURATION
# -----------------------------
TOTAL_LOGS = 2000
OUTPUT_FILE = "data/training_logs.csv"

NORMAL_RATIO = 0.70
SUSPICIOUS_RATIO = 0.20
ATTACK_RATIO = 0.10

ENDPOINTS = [
    "/api/login",
    "/api/users",
    "/api/orders",
    "/api/products",
    "/api/admin"
]

HTTP_METHODS = ["GET", "POST", "PUT", "DELETE"]

USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)",
    "curl/7.68.0",
    "python-requests/2.28.1",
    "sqlmap/1.7"
]

THREAT_TYPES = {
    "suspicious": ["scanner", "unknown_agent"],
    "attack": ["brute_force", "sql_injection", "port_scan"]
}

# -----------------------------
# HELPER FUNCTIONS
# -----------------------------

def random_ip():
    return f"{random.randint(1, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(1, 255)}"


def random_timestamp():
    start_time = datetime.now() - timedelta(days=1)
    random_seconds = random.randint(0, 86400)
    return (start_time + timedelta(seconds=random_seconds)).strftime("%Y-%m-%d %H:%M:%S")


# -----------------------------
# LOG GENERATION
# -----------------------------

logs = []

normal_count = int(TOTAL_LOGS * NORMAL_RATIO)
suspicious_count = int(TOTAL_LOGS * SUSPICIOUS_RATIO)
attack_count = TOTAL_LOGS - normal_count - suspicious_count

# NORMAL TRAFFIC
for _ in range(normal_count):
    logs.append({
        "timestamp": random_timestamp(),
        "ip_address": random_ip(),
        "endpoint": random.choice(ENDPOINTS),
        "http_method": random.choice(HTTP_METHODS),
        "status_code": random.choice([200, 201, 204]),
        "user_agent": random.choice(USER_AGENTS[:2]),
        "response_time": random.randint(50, 300),
        "is_threat": False,
        "threat_type": "",
        "severity": "low"
    })

# SUSPICIOUS TRAFFIC
for _ in range(suspicious_count):
    logs.append({
        "timestamp": random_timestamp(),
        "ip_address": random_ip(),
        "endpoint": random.choice(ENDPOINTS),
        "http_method": random.choice(HTTP_METHODS),
        "status_code": random.choice([401, 403, 404]),
        "user_agent": random.choice(USER_AGENTS[2:4]),
        "response_time": random.randint(300, 800),
        "is_threat": True,
        "threat_type": random.choice(THREAT_TYPES["suspicious"]),
        "severity": "medium"
    })

# CLEAR ATTACKS
for _ in range(attack_count):
    logs.append({
        "timestamp": random_timestamp(),
        "ip_address": random_ip(),
        "endpoint": "/api/login",
        "http_method": "POST",
        "status_code": random.choice([401, 429, 500]),
        "user_agent": random.choice(USER_AGENTS[3:]),
        "response_time": random.randint(800, 2000),
        "is_threat": True,
        "threat_type": random.choice(THREAT_TYPES["attack"]),
        "severity": "high"
    })

random.shuffle(logs)

# -----------------------------
# SAVE TO CSV
# -----------------------------

with open(OUTPUT_FILE, mode="w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=logs[0].keys())
    writer.writeheader()
    writer.writerows(logs)

print(f"[INFO] Generated {len(logs)} log entries and saved to {OUTPUT_FILE}")
