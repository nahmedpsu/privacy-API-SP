"""Local structural validation and plan generation, without network activity."""

import json
from importlib.resources import files

from jsonschema import Draft202012Validator


def schema() -> dict:
    resource = files("sp_privacytest").joinpath("schemas/contract.schema.json")
    return json.loads(resource.read_text(encoding="utf-8"))


def validate_contract(contract: object) -> list[str]:
    """Return generic structural errors without echoing potentially sensitive values."""
    errors = Draft202012Validator(schema()).iter_errors(contract)
    # Do not expose paths: an unexpected key could itself contain sensitive text.
    return sorted(f"Contract schema violation: {error.validator}" for error in errors)


def create_plan(contract: object) -> dict:
    """Return an explicitly blocked local plan, never a control-conformance verdict."""
    errors = validate_contract(contract)
    if errors:
        raise ValueError("Contract failed structural validation.")
    return {
        "contract_id": contract["contract_id"],
        "family_id": contract["family_id"],
        "stage": "offline_plan",
        "status": "blocked",
        "reason": "live_adapter_not_implemented",
        "network_requests_sent": 0,
        "assertions_executed": 0,
        "operational_evidence": False,
        "evaluation_eligible": False,
    }
