# Stage 1: Westminster form and rules mapping

This is the **first implementation increment**, completed as source-controlled data rather than changing the public website prematurely.

- [`development-review.v0.1.json`](development-review.v0.1.json) maps the primary PL-101 fields, application attachments, source links and Development Review decision criteria.
- The schema uses stable IDs like `property.apn` and `owner.name` so upload extraction, the intake page and official PDF mapping can share one canonical field.
- A requirement can be **required**, **conditional** or **needs_confirmation**. All entries remain subject to current-form verification and Planning Division confirmation.
- A draft is not ready if a critical field is missing or conflicting. A packet marked *complete candidate* is **not** a city completeness determination.
- The four approval findings in Municipal Code §17.520.020 require supporting evidence and review; the app must not report an approval probability.

## Verified sources

- [Development Review application PL-101](https://www.westminster-ca.gov/home/showpublisheddocument/536/637544150393130000)
- [Current forms index](https://www.westminster-ca.gov/departments/community-development/planning-division/applications-forms-and-permits)
- [Applicability: WMC 17.520.010](https://ecode360.com/43536851): new residential projects of 3+ units
- [Filing and review: WMC 17.520.015](https://ecode360.com/43536855): additional materials can be requested
- [Findings: WMC 17.520.020](https://ecode360.com/43536807): health/safety, code/design, General Plan, public facilities
- [City process](https://www.westminster-ca.gov/departments/community-development/planning-division/development-review-process)

## Before Stage 2

1. Verify each field against the current official packet, including later-page signatures, questionnaires and exhibit specifications.
2. Confirm conditional checklist triggers for the six-townhome scenario, especially subdivision, affordability and replacement housing.
3. Confirm the actual submission channel and document versions with Westminster Planning.
4. Only then generate the intake UI from this rule pack.

**Note:** This first map covers the primary form's visible fields and a high-level document inventory. It is not yet a page-by-page transcription of every supplemental form or an automated zoning-compliance engine.
