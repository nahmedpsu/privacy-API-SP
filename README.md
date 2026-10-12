# SP-PrivacyTest

Requirements-traceable API privacy-conformance testing for social protection information systems.

**Status: research scaffold, version 0.1.0.dev0.** This repository currently provides offline contract validation and blocked execution-plan generation. It does not implement a live MIS adapter, execute privacy tests, connect to a registry, or establish any security or legal-compliance claim.

## Purpose

The project will connect owner-approved privacy requirements with record/field expectations, identity-state transitions, export checks, audit correlation and minimized evidence. The intended evaluation is an authorized case study involving KP Pakistan's Integrated Beneficiary Registry (IBR); permission, ethics decisions, deployment details and results are not asserted here.

The research protocol specifies 17 privacy-control families plus one evidence-provenance gate. Existing API and authorization tools already provide substantial functionality; the proposed contribution is a reusable domain workflow and its measured utility, not the invention of authorization testing.

## Quick start

Requires Python 3.11 or later. Run these commands from a checkout:

```sh
python -m venv .venv
# Linux/macOS:
. .venv/bin/activate
# Windows PowerShell alternative: .venv\Scripts\Activate.ps1
python -m pip install -e .
sp-privacytest validate examples/illustrative-contract.json
sp-privacytest plan examples/illustrative-contract.json
python -m unittest discover -s tests -v
```

The example is an invented configuration fixture for development, not a beneficiary dataset or evaluation result. The `plan` command emits a JSON plan with `status: "blocked"` and `reason: "live_adapter_not_implemented"`; it sends no network requests. A successful CLI exit means the offline operation completed, not that any privacy control passed.

## Implemented and planned

| Component | Current status |
|---|---|
| Strict JSON contract schema | Implemented; structural validation only |
| Offline validation CLI | Implemented |
| Offline, blocked plan generation | Implemented |
| Automated development tests | Implemented; no operational evidence |
| Seventeen control families and provenance gate | Documented, not executed |
| Live IBR/MIS adapter and authentication | Not implemented |
| Operational record/field assertions | Not implemented |
| State-transition, export and audit checks | Not implemented |
| Customized Schemathesis comparison harness | Protocol only |
| Owner-authorized evaluation and independent rerun | Not performed |

## Repository map

```text
src/sp_privacytest/       Offline CLI, validation and adapter interface
src/sp_privacytest/schemas/  Packaged JSON contract schema
examples/                Clearly labelled non-operational configuration
tests/                   Offline development tests
docs/test-matrix.md      Eighteen planned test families
docs/comparative-protocol.md  Three-arm evaluation protocol
docs/data-governance.md  Authorization and evidence boundaries
docs/development.md      Implementation roadmap and known limitations
.github/workflows/       Offline CI tests only
```

## Evaluation design

- **A: SP-PrivacyTest:** Proposed domain-specific contracts and evidence workflow.
- **B: Customized Schemathesis:** Independent checks and a bounded execution harness using the same approved requirements.
- **C: Existing practice:** The operator's documented manual/script workflow, if one exists.

The primary comparison is A–B; A–C addresses practical utility. Comparable workloads, policy and evidence access must be fixed before the evaluation, and timing must be reported alongside conclusive coverage. See the [comparative protocol](docs/comparative-protocol.md).

## Safety and data

Never commit credentials, tokens, identifiers, beneficiary records, raw responses, operational logs, deployment configuration, or an IBR source archive. `.gitignore` reduces accidental inclusion but is not a security boundary, and schema validation is not a sensitive-data scanner.

No synthetic fixture or development test in this repository will count as primary operational evaluation evidence. The planned study requires separate, owner-authorized operational data and approved access; public software availability does not authorize testing any protected system.

## Maintainer and attribution

Repository maintainer: [nahmedpsu](https://github.com/nahmedpsu). Development uses AI assistance; all code, research claims and any eventual manuscript require appropriate human verification. Git authorship identifies the repository contributor and is not a claim that operational evaluation has occurred.

## License and citation

The newly authored starter software and documentation are distributed under the [MIT License](LICENSE.txt). This license does not grant rights to third-party software, IBR source code, institutional documents or operational data, none of which are included.

There is no published SoftwareX article, release DOI or completed validation associated with this scaffold. Until a formal release is archived, identify this repository and the exact commit when referring to the software.
