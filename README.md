# Tribit-H4H

AI-assisted preparation of planning and permitting application packages for Habitat for Humanity and other nonprofit affordable-housing project managers.

## Intended workflow

1. Select the jurisdiction and applicable planning/permitting application pathway.
2. Collect project facts and supporting documents, retaining source provenance.
3. Map the city's published application fields and attachment requirements to the project information.
4. Draft the application forms, assemble attachments, and generate a completeness and discrepancy report.
5. A human project manager verifies every material statement, resolves flagged gaps, approves and signs, then submits the package themselves.

**No automated submission.** Missing information must be flagged rather than invented. Published city checklists, fee schedules, and legal requirements must be revalidated against official sources before use.

## MVP scope

Start with one Orange County jurisdiction, provisionally Westminster, CA, and one representative nonprofit residential development application. Confirm the appropriate application pathway and current packet with city staff before implementation. ADU workflows are secondary.

## Repository contents

- `LANE2-ORIGINAL.md`: original Lane 2 challenge brief.
- `scenarios.json`: synthetic design scenarios.
- `data/DATA-SOURCES.md`: sourced California law, HCD, and Orange County research leads, with verification caveats.
- `data/oc-cities.json`: starter city inventory.
- `data/timeline.json`: illustrative, assumption-labeled development timeline.
- `docs/REVIEW-CHECKLIST.md`: preliminary human review checklist.

This repository currently contains research and project framing, **not** a working form-generation engine or verified city-specific application package.

## Attribution and licensing

The Lane 2 source files were copied from [Claude Impact Lab UCI, Lane 2: Clear it](https://github.com/travcjohnson/claude-impact-lab-uci/tree/main/lanes/2-clear-it). The original repository states that its challenge brief and lane descriptions are dedicated to the public domain under CC0 1.0, and its code is MIT-licensed. The original license notice is retained in `LICENSE`. Third-party documents and datasets linked in the research catalog retain their respective terms.
