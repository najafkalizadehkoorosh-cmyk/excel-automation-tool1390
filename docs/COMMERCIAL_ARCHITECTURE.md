# Commercial Architecture

## Objective

Keep the current public MIT-licensed project useful as the open-source core while reserving genuinely new commercial work for a separate distribution unit.

## Current open-source core

The public repository contains the desktop data-processing engine, GUI, CLI, presets, quality reporting, tests, and build workflows. The repository is currently distributed under the MIT License.

## Commercial boundary

Do not add proprietary restrictions to code that is already published under MIT.

Future commercial-only work should be new code or assets created after this boundary is established, for example:

- premium workflow packs created as new assets;
- customer-specific templates and rule bundles;
- optional commercial support materials;
- future hosted services or account features, if demand justifies them;
- distribution-specific packaging or support tooling.

Any commercial component that links to, imports, or redistributes the MIT core must preserve the MIT license obligations for the core and clearly distinguish the commercial component. Obtain appropriate legal review before making licensing claims.

## Recommended repository split

When the GitHub connection can create a second repository, use:

- `excel-automation-tool1390` — public MIT core.
- `excel-automation-tool-pro` — private/commercial additions, subject to seller/account eligibility and final licensing review.

Until that second repository is available, keep commercial-only code out of the public repository.

## Release model

### Free

- public MIT core;
- single-file cleanup;
- basic quality inspection;
- basic transformations;
- basic presets;
- local desktop workflow.

### Pro candidate

- commercial workflow packs;
- advanced configurable rules;
- higher-volume orchestration;
- reusable customer templates;
- commercial support.

Premium features should be selected from validated demand rather than assumed demand.

## Payment gate

No payment provider is enabled in the current project. Do not collect payment data in this repository. Before selling, verify the payment/distribution provider's eligibility rules, age requirements, identity requirements, taxes, refunds, and supported seller country.

## Security rule

Never commit passwords, private tokens, API keys, payment credentials, or customer spreadsheets. Use provider dashboards or GitHub Secrets/environment variables where credentials are genuinely required.

## Decision record

The public MIT repository is intentionally not being relicensed in place. This avoids changing rights already granted to existing recipients of the MIT-licensed code.
