services = ["ssh", "https", "dns"]

for service in services:
	if service == "https":
		print(f"{service}: web traffic")
	else:
		print(f"{service}: other service")
