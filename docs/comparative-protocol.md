# Prospective comparative evaluation protocol

This document describes intended work, not completed implementation or evaluation. No operational approvals, sample sizes, privacy violations or performance results are asserted.

## Study arms and contribution

| Arm | Workflow | Intended comparison |
|---|---|---|
| A | SP-PrivacyTest contracts, adapter and evidence reporting | Proposed domain-specific workflow |
| B | Schemathesis with independent custom assertions and an approved bounded harness | Primary technical comparison, A–B |
| C | Operator's documented current manual/script procedure | Secondary practical comparison, A–C |

Schemathesis supports custom response and run-level checks; its documentation includes response-identity and audit-header examples ([Schemathesis extension guide](https://schemathesis.readthedocs.io/en/stable/guides/extending/)). Accordingly, B must be competently configured rather than treated as an uncustomizable schema-only tester.

If C does not exist, report it unavailable. If A uses Schemathesis internally, describe A–B as a comparison of added domain functionality and integration, not independent execution engines.

## Common inputs and scope

An owner-approved, tool-neutral specification will define each requirement, endpoint/method, principal entitlement, authentication state, operational cohort alias, record/field rules, transition, output representation and required evidence. All arms receive equal policy, credential entitlement and evidence access; none uses A's output as the reference oracle.

Assertions are implemented independently. Neutral schema/transport/parsing utilities may be shared with costs and common-mode error risks disclosed; reviewers must be able to inspect original owner-held evidence.

Before main execution, freeze:

- **Eligible scope P:** All planned applicable privacy-control instances.
- **Common scope M_AB / M_AC:** Instances each compared arm is configured to attempt, determined before main-run outcomes.
- **Workload blocks:** Coherent endpoint workflows or transition/evidence tasks, not individual HTTP calls treated as independent labor samples.
- **Evaluation partition:** Owner-selected instances withheld from development and pilot tuning, without claiming previously inspected code is unseen.

Missing capability is blocked with a reason, not a system failure or non-applicability. Keep unsupported cases visible against P and report common-scope size; do not intersect only successful cases afterward.

## Baseline adequacy and safe execution

Permit B custom Python checks, orchestration and local evidence parsers, recording their effort. A reviewer independent of A's implementation must assess B against the approved specification before freezing all arm versions and dependencies.

The matched run uses bounded, predetermined requests and transitions, not unrestricted fuzzing. Pilot the actual pinned-version harness and request-control behavior before main execution; this document does not supply or validate that harness.

All arms follow the same approved rate ceiling, record limit and stop procedure. Count authentication, retries, polling and setup traffic separately where they differ; equivalent semantics do not require byte-identical requests.

Execute arms sequentially and balance order across comparable blocks using a prespecified rotation, such as A–B–C, B–C–A and C–A–B. Verify/reset account state, token age, cohort version, cache condition, audit timing and upstream state between runs. Unsafe or impossible resets invalidate paired comparability, not the original run accounting.

State changes are limited to approved research identities. Do not modify beneficiary entitlements, payments or production records, inject defects, disable safeguards or assume authorization to contact downstream institutions.

## Independent evidence review

Two reviewers uninvolved in the compared assertions will adjudicate findings, cross-arm disagreements and a prespecified sample of agreements. Conceal arm labels where practicable; retain original and resolved decisions and use a third reviewer or documented owner adjudication for disagreements.

Apply an independent evidence-provenance gate equally across all arms. Mock or unknown paths cannot establish assertions that require operational provenance, although adequate local evidence may establish a local denial.

Keep native arm outputs, mapped outcomes, provenance and adjudicated conclusions distinct. Deduplicate confirmed findings by root cause and scope, retaining each arm's detection; the union of detected findings is not a complete defect inventory.

## Measures and denominators

| Measure | Definition and reporting rule |
|---|---|
| Primary common-scope coverage | Each arm's pass+fail instances divided by the same frozen M_AB or M_AC count; report percentage-point difference. |
| Eligible-scope coverage | Each arm's pass+fail instances divided by P; blocked/inconclusive cases remain in the denominator. |
| Primary matched-block effort | Comparator minus A active person-minutes, with planned/completed instances and conclusive evidence yield for each block. |
| First-use effort | Shared preparation, arm-specific integration/check authoring, supervision and review, itemized without double counting. |
| Repeat-run effort | Actual rerun labor and troubleshooting, separate from first-use cost and general product development. |
| Finding precision | Confirmed unique findings / (confirmed + rejected unique findings); unresolved counts alongside; undefined at zero denominator. |
| Finding overlap | Shared and arm-specific confirmed root causes on matched scope; other-scope findings separate. |
| Unexpected denial | Confirmed target denials among conclusive expected-allow instances; distinguish harness authentication failures. |
| Audit completeness | Required events supported by adequate audit evidence / required events in the approved workload; inaccessible logs remain unresolved. |
| Rerun agreement | Matching conclusive outcomes / comparable instances conclusive in both runs, with paired coverage and state stability disclosed. |
| Operational burden | Requests, elapsed runtime, waiting, latency and timeouts; not production-service overhead. |

Report A–B and A–C separately. Faster execution does not demonstrate improvement if it supplies less conclusive evidence; show incomplete blocks and attrition beside any comparable-completion subset.

Use descriptive counts and paired block summaries. Repeated requests, routes and records from one purposively selected deployment are dependent; no powered superiority or population-level significance claim is planned. Do not report recall, specificity or F1 without an independently established defect reference set, and do not invent sensitivity estimates if no defects are found.

## Reproducibility and execution prerequisites

Before execution, document owner and ethics determinations, selected endpoints/records/entitlements, policy revisions, partitions and manifests, assessor roles, baseline adequacy, repetition count, order, review sampling, resets/tolerances, safety bounds and pinned versions. These fields are not completed by the public repository.

Subject to rights and owner approval, release the evaluated toolkit, B's custom harness, safe manifests, outcome mappings and analysis procedures. Keep restricted records and logs inside the authorized environment and identify reproduction limits explicitly.

## Related foundations

Machine-readable authorization matrices and business-data-aware authorization are already described by [OWASP's automation guidance](https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Testing_Automation_Cheat_Sheet.html). Social security interoperability and privacy safeguards are jointly emphasized in the [ILO–ISSA–OECD paper prepared for the February 2025 G20 discussions](https://www.ilo.org/sites/default/files/2025-02/20150206_G20_EWG_Social%20Security%20Digitalization%20Paper_ILO_ISSA_OECD%20(002).pdf).

The study will assess a reusable domain workflow and its measured utility. These prior sources support the motivation, not a claim of absolute novelty or journal acceptance.
