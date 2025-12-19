                                                    #Fake LOG  (log_generator.py)

import random  # Importing the random module to randomly select IPs, ports, and statuses
import time    # Importing the time module to get the current timestamp

#List of sample IP addresses to simulate network activity
ips = ["192.168.1.23", "10.0.0.5", "192.168.1.10", "172.16.0.8"]

            #List of common network ports to simulate connections
ports = [22, 80, 443, 8080, 3306]

                    #Function to generate a single network log entry
def generate_log():
    ip = random.choice(ips)                   # Randomly select an IP address from the list
    port = random.choice(ports)               # Randomly select a port from the list
    status = random.choice(["SUCCESS", "FAILED"])  # Randomly select the connection status
    # Return a formatted log line: timestamp | IP | PORT | STATUS
    return f"{time.time()} | IP={ip} | PORT={port} | STATUS={status}"

# Open a file named "network_logs.log" in write mode
with open("network_logs.log", "w") as file:
    # Generate 100 log entries and write each to the file
    for _ in range(2000):
        file.write(generate_log() + "\n")

# Print a message indicating that the log file has been created
print("Log file generated.")


