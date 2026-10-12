"""Development fixture tests only. These are not operational privacy evaluations."""

from contextlib import redirect_stdout
from copy import deepcopy
from io import StringIO
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

from jsonschema import Draft202012Validator
from sp_privacytest.adapters import UnavailableAdapter
from sp_privacytest.cli import main, MAX_CONTRACT_BYTES
from sp_privacytest.contracts import create_plan, schema, validate_contract

EXAMPLE = Path(__file__).resolve().parents[1] / "examples/illustrative-contract.json"


class ScaffoldTests(unittest.TestCase):
    def setUp(self):
        self.contract = json.loads(EXAMPLE.read_text(encoding="utf-8"))

    def test_schema_is_valid(self):
        Draft202012Validator.check_schema(schema())

    def test_example_is_structurally_valid(self):
        self.assertEqual(validate_contract(self.contract), [])

    def test_all_families_have_valid_identifiers(self):
        for number in range(1, 19):
            self.contract["family_id"] = f"IBR-{number:02}"
            self.assertEqual(validate_contract(self.contract), [])

    def test_out_of_range_family_rejected(self):
        for value in ["IBR-00", "IBR-19", "IBR-1", "arbitrary"]:
            self.contract["family_id"] = value
            self.assertTrue(validate_contract(self.contract))

    def test_required_fields_rejected_when_missing(self):
        for key in schema()["required"]:
            value = deepcopy(self.contract)
            del value[key]
            self.assertTrue(validate_contract(value), key)

    def test_unknown_and_secret_fields_rejected_without_echo(self):
        self.contract["password"] = "development-fixture-not-a-real-secret"
        errors = validate_contract(self.contract)
        self.assertTrue(errors)
        self.assertNotIn("development-fixture", str(errors))

    def test_nested_headers_rejected(self):
        self.contract["endpoint"]["headers"] = {"Authorization": "fixture"}
        self.assertTrue(validate_contract(self.contract))

    def test_external_calls_cannot_be_enabled(self):
        self.contract["external_call_permission"] = True
        self.assertTrue(validate_contract(self.contract))

    def test_absolute_paths_and_queries_rejected(self):
        for path in ["https://example.invalid/api", "//example.invalid", "/api?token=x"]:
            self.contract["endpoint"]["path"] = path
            self.assertTrue(validate_contract(self.contract))

    def test_non_object_rejected(self):
        for value in [None, [], 1, "text"]:
            self.assertTrue(validate_contract(value))

    def test_plan_is_blocked_and_not_evidence(self):
        plan = create_plan(self.contract)
        self.assertEqual(plan["status"], "blocked")
        self.assertEqual(plan["network_requests_sent"], 0)
        self.assertEqual(plan["assertions_executed"], 0)
        self.assertFalse(plan["evaluation_eligible"])
        self.assertFalse(plan["operational_evidence"])

    def test_invalid_plan_rejected(self):
        with self.assertRaises(ValueError):
            create_plan({})

    def test_adapter_cannot_execute(self):
        with self.assertRaises(NotImplementedError):
            UnavailableAdapter().execute(self.contract)

    def test_cli_commands_without_network(self):
        with patch("socket.socket", side_effect=AssertionError("Network prohibited")):
            for command in ["validate", "plan"]:
                output = StringIO()
                with redirect_stdout(output):
                    self.assertEqual(main([command, str(EXAMPLE)]), 0)
                self.assertIsInstance(json.loads(output.getvalue()), dict)

    def test_invalid_input_has_nonzero_exit(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "fixture.json"
            for content in ["{broken", "null", "{}", "x" * (MAX_CONTRACT_BYTES + 1)]:
                path.write_text(content, encoding="utf-8")
                with redirect_stdout(StringIO()):
                    self.assertEqual(main(["validate", str(path)]), 2)

    def test_missing_file_has_nonzero_exit(self):
        with tempfile.TemporaryDirectory() as directory:
            with redirect_stdout(StringIO()):
                self.assertEqual(main(["validate", str(Path(directory) / "absent.json")]), 2)


if __name__ == "__main__":
    unittest.main()
