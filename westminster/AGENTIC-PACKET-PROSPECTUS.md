# Prospectus: agentic planning application packet generation

**Project:** Tribit-H4H. **Target user:** Habitat OC development/project manager. **Initial jurisdiction:** Westminster, California. **Prototype typology:** six new attached affordable-ownership townhomes, hypothetical until a real parcel is provided. **Product promise:** turn uploaded documents **or** one consolidated project intake page / JSON file into an auditable **draft** planning submission packet for human approval. No automated filing.

## 1. User experience

A project manager opens a project, chooses Westminster and the development type, then:
1. **Upload-first:** drops in deed, title report, parcel/zoning information, survey, plans, project narrative, architect contact sheet, affordability commitments and any city correspondence (PDF/DOCX/images).
2. **Form-first:** fills one consolidated intake page, which saves the same canonical JSON schema. A manager may also import a JSON file directly.
3. The app extracts facts from documents, marks each fact with its source filename, page and extraction confidence, and merges them into the intake model. Conflicting facts are never silently overwritten.
4. The app asks targeted questions only for required missing facts, confirms which application pathway applies, and shows a document requirements matrix.
5. The manager clicks **Generate draft packet**. The app populates city forms where technically feasible, writes the narrative, creates an exhibit index, generates a checklist, and collects provided technical attachments **without inventing them**.
6. The manager sees a side-by-side review of each field and its provenance, approves/edits facts, obtains real owner/professional signatures, and exports a ZIP/PDF set. **The manager files it personally.**

## 2. Architecture: workflow engine with bounded agents

```text
Uploaded files ──> ingestion / OCR / text extraction ──> evidence records ──┐
                                                                            ├──> canonical Project JSON
One intake page / imported JSON ──> schema validation ──────────────────────┘
                         |
              conflicts / missing facts queue
                         |
             jurisdiction rule registry (versioned)
                         |
              requirements + pathway evaluator
                         |
               document / form field mapping
                         |
          draft forms + narrative + exhibit index
                         |
         deterministic validation and QA agent
                         |
       human review / signature / export only
```

**Agents are task-specific, not autonomous decision makers:**
- **Intake agent:** classifies uploads, extracts factual values, records evidence citations and conflicts.
- **Pathway agent:** recommends likely city filing path based on zoning/project facts, **requires confirmation** when zoning or statutes are ambiguous.
- **Requirements agent:** builds a conditional checklist from versioned city rules; explains why each document is needed.
- **Drafting agent:** writes narrative text from verified facts and fills mapped form fields; does not manufacture drawings, studies, title reports, signatures, seals or official determinations.
- **QA agent:** compares every output value against source evidence, validates cross-form consistency, and blocks export readiness on critical omissions.

A deterministic orchestrator controls state transitions; agents cannot submit applications or approve themselves.

## 3. Canonical project model

See [schema/project.schema.json](schema/project.schema.json) and [examples/six-townhomes.example.json](examples/six-townhomes.example.json). Every important field has a status and provenance. Distinguish **user-confirmed**, **document-extracted**, **unverified**, **conflicting**, and **missing**. Store documents as secure object references; the public GitHub repository contains no real applicant/owner documents.

The consolidated entry page should have sections for **Property**, **Applicant & owner**, **Project scope**, **Housing/affordability**, **Site & plans**, **Entitlements**, **Attachments**, and **Review**. An upload may prefill a field, but a person can override it and the system records the override and reason.

## 4. City requirements as versioned data

Do not put the city's rules exclusively in a model prompt. Maintain a **rule pack** with:
- official source URL, document title, publication/retrieval date, and source page;
- rule ID, field/document requirement, applicability condition and reason;
- required / conditional / not applicable / needs staff confirmation;
- exact city form version and field mapping;
- review status and reviewer.

For example, Westminster's Development Review packet PL-101 calls for owner authorization, title/ownership documentation, residential questionnaire and other attachments. Source: https://www.westminster-ca.gov/home/showpublisheddocument/536/637544150393130000

**Known discrepancy to flag:** the zoning code states Development Review applies to new residential projects with 3+ units, while the city's ADU webpage states 4+. Source: https://ecode360.com/43536828 ; https://www.westminster-ca.gov/departments/community-development/planning-division/accessory-dwelling-units. Never silently select one threshold for borderline cases.

## 5. Implementation approach

**Suggested stack:** Python FastAPI backend; Pydantic/JSON Schema validation; a web frontend with schema-driven forms (React/Next.js is optional); object storage for private documents; PostgreSQL for projects, evidence and audit events; PDF parsing with PyMuPDF/pdfplumber; OCR only for scanned files; PDF form filling with pypdf where AcroForm fields exist; otherwise template overlay or an explicit human-fill fallback. Use LLM structured output for extraction and narrative, but deterministic code for rule evaluation, field mapping and validations.

**Data objects:** `Project`, `Document`, `Evidence`, `Fact`, `Requirement`, `FormTemplate`, `FormFieldMapping`, `DraftArtifact`, `ValidationFinding`, `ApprovalEvent`.

**API sketch:** `POST /projects`; `POST /projects/{id}/documents`; `PATCH /projects/{id}/facts`; `GET /projects/{id}/requirements`; `POST /projects/{id}/drafts`; `GET /projects/{id}/review`; `POST /projects/{id}/export`. No `/submit` endpoint.

**Security:** real ownership and title records can contain personal information. Encrypt at rest/in transit, restrict access by project role, redact logs, implement retention/deletion, scan uploads, and never send private documents to an unapproved model provider. GitHub stores only templates, rules and synthetic examples.

## 6. Milestones and acceptance criteria

**Phase A, rules and forms:** Obtain current Westminster forms and confirm planning filing route, fees, plan-set requirements and actual form fillability. Build reviewed field map and conditional requirements table. Acceptance: each required item has an official source and applicability reason.

**Phase B, canonical intake:** Implement JSON Schema and a single intake form; support document uploads and field provenance. Acceptance: upload and manual entry converge to identical validated JSON; contradictory APNs are flagged.

**Phase C, generation:** Populate PL-101 where feasible; generate project description, exhibits index and completeness report. Acceptance: no invented values or signatures; every output field links to an input fact or is visibly marked blank.

**Phase D, review/export:** Human review interface, corrections, versioning, signed-off draft export. Acceptance: unresolved critical findings prevent 'ready for human filing'; export includes an audit manifest.

**Phase E, real pilot:** Test with a consenting Habitat project manager and sanitized sample documents; compare to a manually assembled packet. Measure field accuracy, reviewer correction time, missing-document recall and time to draft. Do not claim city acceptance until a real city review occurs.

## 7. Deliberate exclusions

Do not initially automate permit submission, construction drawings, engineering calculations, legal determinations, environmental studies, owner signatures, fee payment or every Orange County jurisdiction. The high-leverage MVP is reliable **packet assembly**, not a general-purpose municipal agent.

## 8. Principal risks

- Stale city forms, fees and zoning (mitigate with source timestamps and revalidation).
- Hallucinated facts (mitigate with evidence-backed extraction and fail-closed QA).
- Wrong entitlement pathway (mitigate with explicit staff confirmation).
- Sensitive property/owner data (mitigate with private storage and access controls).
- PDFs that cannot be reliably auto-filled (mitigate with verified template mappings and manual fallback).
- Conditional studies/agency signoffs mistaken for optional (mitigate with human review and conditional rules).
