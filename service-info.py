import json

def is_valid_port(port):
    return type(port) is int and 1 <= port <= 65535

def validate_service(service, index):
    if not isinstance(service, dict):
        return f"ERROR: service #{index} must be a JSON object"

    required_keys = {"name", "port", "encrypted"}
    missing_keys = required_keys - service.keys()

    if missing_keys:
        return (
            f"ERROR: service #{index} is missing keys: "
            f"{', '.join(sorted(missing_keys))}"
        )

    expected_types = {
        "name": str,
        "port": int,
        "encrypted": bool,
    }

    for field, expected_type in expected_types.items():
        if type(service[field]) is not expected_type:
            return f"ERROR: service #{index} field '{field}' must be of type {expected_type.__name__}"

    if not is_valid_port(service["port"]):
        return f"ERROR: service #{index} port must be between 1 and 65535"

    return None

def main():
    try:
        with open("services.json", encoding="utf-8") as file:
            services = json.load(file)
    except FileNotFoundError:
        print("ERROR: services.json was not found")
        raise SystemExit(1)
    except json.JSONDecodeError as error:
        print(f"ERROR: Invalid JSON on line {error.lineno}")
        raise SystemExit(1)

    if not isinstance(services, list):
        print("ERROR: expected a JSON list of services")
        raise SystemExit(1)

    unencrypted_count = 0

    for index, service in enumerate(services, start=1):
        error = validate_service(service, index)
        if error is not None:
            print(error)
            raise SystemExit(1)

        if service["encrypted"]:
            print(f"OK: {service['name']} on port {service['port']} is encrypted")
        else:
            print(f"REVIEW: {service['name']} on port {service['port']} is unencrypted")
            unencrypted_count += 1

    print(f"Unencrypted services found: {unencrypted_count}")

if __name__ == "__main__":
    main()
