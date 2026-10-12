# Development roadmap and known limitations

The current scaffold implements only structural contract validation and blocked plan output. This document is a plan, not a list of delivered operational features.

## Next implementation stages

- **Contract semantics:** Resolve approved policy references and define assertion-level evidence requirements; add cross-field validation beyond the initial schema.
- **Controlled adapter:** Implement operator-approved authentication, allowlists, rate/record ceilings, timeouts and explicit stop controls; retain raw evidence locally.
- **Assertions:** Implement and unit-test each family with transparent development fixtures before authorized operational evaluation.
- **Evidence engine:** Add provenance, local record/field checking, format normalization and owner-audit correlation; preserve blocked/inconclusive outcomes.
- **Comparator:** Independently implement customized Schemathesis checks against the neutral specification and document baseline adequacy.
- **Evaluation:** Freeze protocols and software, obtain required determinations, run matched workloads, adjudicate and reproduce.
- **Research release:** Archive the evaluated version and supply verified results, limitations, data availability and software citation.

## Current limitations

The schema rejects unknown fields, arbitrary remote schemas and absolute endpoint URLs, but it is not a sensitive-data detector or authorization mechanism. Alias fields may still be misused; structural validation does not verify their content, policy correctness or permissions.

The schema includes future HTTP methods and output formats as vocabulary, not executable capability. External calls are fixed to false in this scaffold; changing that requires a future reviewed design and separate owner authorization.

No live adapter, assertions, record ingestion, token handling, downstream access, format extraction or audit correlation is implemented. Do not interpret the blocked plan as a failed privacy test, or development CI as evidence of SoftwareX readiness.

## Reproducible development

Direct build/runtime dependencies are pinned in `pyproject.toml`; transitive dependencies are not yet locked. CI declares supported Python versions, but an actual operational release will require an environment-specific lockfile, exact adapter/configuration versions and documented verification.

Run `python -m unittest discover -s tests -v` after installation. The development suite includes schema rejection, unavailable-adapter behavior, safe output and offline CLI checks; it uses no beneficiary data.
