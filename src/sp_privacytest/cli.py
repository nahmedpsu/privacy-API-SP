"""Offline-only command line interface; intentionally has no run command."""

import argparse
import json
from pathlib import Path

from . import __version__
from .contracts import create_plan, validate_contract

MAX_CONTRACT_BYTES = 256 * 1024


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Offline contract scaffold. No API requests or privacy tests are executed."
    )
    parser.add_argument("--version", action="version", version=__version__)
    parser.add_argument("command", choices=("validate", "plan"))
    parser.add_argument("contract", type=Path)
    args = parser.parse_args(argv)
    try:
        with args.contract.open("rb") as stream:
            raw = stream.read(MAX_CONTRACT_BYTES + 1)
        if len(raw) > MAX_CONTRACT_BYTES:
            raise ValueError("Contract exceeds size limit.")
        contract = json.loads(raw)
    except (OSError, UnicodeError, ValueError, RecursionError):
        print(json.dumps({"status": "invalid", "reason": "unreadable_or_invalid_contract"}))
        return 2
    try:
        errors = validate_contract(contract)
    except RecursionError:
        print(json.dumps({"status": "invalid", "reason": "excessive_nesting"}))
        return 2
    if errors:
        print(json.dumps({"status": "invalid", "errors": errors}, indent=2))
        return 2
    if args.command == "validate":
        print(json.dumps({
            "status": "structurally_valid",
            "privacy_conformance_evaluated": False,
            "authorization_verified": False,
        }, indent=2))
    else:
        print(json.dumps(create_plan(contract), indent=2))
    return 0
