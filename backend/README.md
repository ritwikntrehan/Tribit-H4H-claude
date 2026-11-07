# Render-ready Claude extraction API

The GitHub Pages frontend remains static. The Node 20 service in `server.js` is the active Render deployment target defined in the repository-root `render.yaml`. Older Python prototype files (`app.py`, `requirements.txt`) remain for reference but are **not** used by Render.

Deploy with the Render Blueprint, set `ANTHROPIC_API_KEY` as a secret, and confirm `CLAUDE_MODEL` is supported by your Anthropic account. Render generates `H4H_ACCESS_TOKEN`. Do not commit either secret to GitHub or place it in public frontend code.

`GET /health` reports service configuration. `POST /api/extract` accepts `{"pages":[{"filename":"deed.pdf","page":1,"text":"..."}]}` with `X-H4H-Token`. Results are unverified candidate fields with source filenames and pages, not confirmed facts.

The service does not store documents or submit applications. The shared access token is suitable only for controlled pilots, not production user management. Before using confidential Habitat records, implement individual authentication, server-side rate limits, access audit logs, retention/privacy policy, and organizational approval. CORS is not authentication.
