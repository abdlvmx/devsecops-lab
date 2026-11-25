services = [
    {"name": "http", "port": 80, "encrypted": False},
    {"name": "https", "port": 443, "encrypted": True},
    {"name": "ssh", "port": 22, "encrypted": True},
    {"name": "telnet", "port": 23, "encrypted": False},
]

unencrypted_count = 0

for service in services:
    if service["encrypted"]:
        print(f"OK: {service['name']} on port {service['port']} is encrypted")
    else:
        print(f"REVIEW: {service['name']} on port {service['port']} is unencrypted")
        unencrypted_count += 1

print(f"Unencrypted services found: {unencrypted_count}")
