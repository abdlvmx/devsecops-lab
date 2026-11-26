import runpy
import unittest
from contextlib import redirect_stdout
from io import StringIO
from pathlib import Path
from tempfile import TemporaryDirectory

module = runpy.run_path("service-info.py")
is_valid_port = module["is_valid_port"]
validate_service = module["validate_service"]
main = module["main"]

class IsValidPortTests(unittest.TestCase):
    def test_valid_ports(self):
        for port in (1, 443, 65535):
            with self.subTest(port=port):
                self.assertTrue(is_valid_port(port))

    def test_ports_outside_range(self):
        for port in (0, 70000, -1):
            with self.subTest(port=port):
                self.assertFalse(is_valid_port(port))

    def test_boolean_is_not_a_port(self):
        self.assertFalse(is_valid_port(True))


class ValidateServiceTests(unittest.TestCase):
    def test_valid_service(self):
        service = {"name": "https", "port": 443, "encrypted": True}
        self.assertIsNone(validate_service(service, 1))

    def test_non_object_is_rejected(self):
        self.assertEqual(
            validate_service("not an object", 1),
            "ERROR: service #1 must be a JSON object",
        )

    def test_missing_key_is_reported(self):
        service = {"name": "https", "port": 443}
        self.assertEqual(
            validate_service(service, 1),
            "ERROR: service #1 is missing keys: encrypted",
        )

    def test_wrong_field_type_is_reported(self):
        service = {"name": "https", "port": "443", "encrypted": True}
        self.assertEqual(
            validate_service(service, 1),
            "ERROR: service #1 field 'port' must be of type int",
        )

    def test_out_of_range_port_is_reported(self):
        service = {"name": "https", "port": 70000, "encrypted": True}
        self.assertEqual(
            validate_service(service, 1),
            "ERROR: service #1 port must be between 1 and 65535",
        )

class MainFileErrorTests(unittest.TestCase):
    def test_missing_file_prints_error_and_exits_with_one(self):
        with TemporaryDirectory() as temp_dir:
            missing_path = Path(temp_dir) / "missing.json"
            output = StringIO()

            with redirect_stdout(output):
                with self.assertRaises(SystemExit) as error:
                    main(str(missing_path))

            self.assertEqual(error.exception.code, 1)
            self.assertEqual(output.getvalue().strip(), f"ERROR: {missing_path} was not found",)

    def test_invalid_json_prints_error_and_exits_with_one(self):
        with TemporaryDirectory() as temp_dir:
            invalid_path = Path(temp_dir) / "invalid.json"
            invalid_path.write_text("[\n", encoding="utf-8")
            output = StringIO()

            with redirect_stdout(output):
                with self.assertRaises(SystemExit) as error:
                    main(str(invalid_path))

            self.assertEqual(error.exception.code, 1)
            self.assertEqual(output.getvalue().strip(), "ERROR: Invalid JSON on line 2")

if __name__ == "__main__":
    unittest.main()
