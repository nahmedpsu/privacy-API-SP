# Planned privacy-conformance test families

These are prospective, generalized test families, not implemented tests or disclosed vulnerabilities. They contain no live routes, internal source excerpts, requirement-document identifiers or operational data.

The owner must approve applicability, expected decisions and required evidence before execution. Departments are not assumed to be isolated unless policy requires it, and consent is not assumed to be the legal basis for every processing operation.

| ID | Family | Planned assertion and evidence |
|---|---|---|
| IBR-01 | Authentication coverage | Compare authenticated and no-credential requests; protected data must follow the approved access rule. |
| IBR-02 | Invalid-token handling | Owner-approved expired/malformed/invalid cases must not authorize protected operations; retain minimized denial evidence. |
| IBR-03 | MFA completion | Compare access before and after legitimate completion of the required authentication flow. |
| IBR-04 | MFA-response minimization | Check that responses do not expose material that defeats the approved independent-factor design; never export challenge values. |
| IBR-05 | Account disablement | On a research account only, verify cessation of access within the owner-approved revocation window. |
| IBR-06 | Role reassignment | Compare access using old/new credentials after an approved research-account entitlement change. |
| IBR-07 | Record-level scope | Returned records must satisfy the independently approved rule; include legitimate access controls. |
| IBR-08 | Request-filter scope | Omitting/changing permitted query filters must not broaden the caller's authorized record set. |
| IBR-09 | Field minimization | Compare nested field/value disclosures with approved release rules; null fields are not automatically leaks. |
| IBR-10 | Export consistency | Compare record and field scope across supported JSON, spreadsheet and PDF representations; uncertain parsing is inconclusive. |
| IBR-11 | External-call authorization | Correlate permitted proxy operations with downstream observations; local denial alone does not prove no upstream request. |
| IBR-12 | Denied-access audit | Correlate denied requests with owner-required audit events after an approved ingestion allowance. |
| IBR-13 | Successful-access audit | Check required read/export audit events, including applicable cached paths. |
| IBR-14 | Cache isolation | Cache reuse must not broaden permitted output when principals have different effective views. |
| IBR-15 | Error-response minimization | Bounded benign validation errors must not disclose information prohibited by the approved error policy. |
| IBR-16 | Conditional consent | Check only actual consent-governed workflows; justified non-applicability differs from a missing required mechanism. |
| IBR-17 | Session lifecycle | Check distinct logout, expiry and idle-timeout semantics on research accounts. |
| IBR-18 | Evidence provenance | Classify operational, fallback/mock, unknown or unavailable paths; this is an evidence gate, not a control score. |

## Outcome rules

- **Pass:** Adequate evidence supports every mandatory assertion.
- **Fail:** Attributable evidence contradicts an approved requirement.
- **Blocked:** A prerequisite, permission or implementation capability prevents the check.
- **Inconclusive:** Execution occurred, but evidence is inadequate or ambiguous.
- **Not applicable:** The requirement genuinely does not apply, with a recorded justification.

Retain assertion-level outcomes. A valid contradiction takes precedence; otherwise unresolved mandatory assertions prevent a pass. A harness defect is not a confirmed target-system defect.

Eighteen families do not mean eighteen independent samples or known defects. Missing access, audit visibility or real data-path provenance must remain visible in reporting.
