def calculate_total_wait(attempts, timeout):
	return attempts * timeout

total = calculate_total_wait(3, 15)
print(f"Total wait: {total} seconds")
