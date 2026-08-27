# Free / Pro Product Plan

## Free edition

Purpose: let a user prove value quickly with no payment or account requirement.

- Single-file CSV/XLSX/XLSM cleanup.
- Basic quality inspection.
- Core deterministic transformations.
- General Cleanup preset.
- Basic batch/merge workflows.
- Local-first processing.

## Pro edition (candidate)

Purpose: charge for repeatable business workflows, not for basic file compatibility.

Candidate paid capabilities:

1. Advanced workflow packs for recurring business exports.
2. Larger-volume batch orchestration and queueing.
3. Reusable custom rules/templates.
4. Advanced quality rules and richer reports.
5. Commercial support materials.

## Pricing hypothesis

Do not present a fixed price as validated. Initial experiments may test:

- $5/month
- $10/month
- small one-time purchase

The first target is $50/month, not a guarantee.

## Entitlement design

The product should not rely on a secret embedded in the executable as a security boundary. A local license file may control access to new commercial functionality, but it is only an access mechanism and must not be treated as cryptographic proof against reverse engineering.

When a lawful payment/distribution provider is selected, use its supported entitlement mechanism or signed license tokens. Never hard-code private signing keys into the desktop executable.

## No payment yet

This repository intentionally contains no payment provider, payment credential, or account backend.
