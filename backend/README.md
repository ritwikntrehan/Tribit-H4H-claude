# Optional Claude server for Stage 4

The GitHub Pages website works without this server. The backend is **not deployed**.

To run locally:

```bash
cd backend
python -m pip install -r requirements.txt
export ANTHROPIC_API_KEY='your-key-here'
export ALLOWED_ORIGIN='http://localhost:8000'
uvicorn app:app --reload
```

`POST /api/draft` accepts `{"jurisdiction":"Westminster, CA","fields":{"property.address":{"value":"..."}}}` and returns a draft narrative. The server reads the API key from its environment and calls Claude. Never commit a key, store it in a static site's JavaScript, or enter it into the public GitHub Pages page.

Before production deployment: add authentication, request rate limits, audit logging with sensitive-data minimization, privacy/retention controls, a server-side versioned rule pack, and structured output validation. CORS is not authentication. Deploy the backend to a private server and configure the frontend with its HTTPS endpoint only after these controls are in place. Verify the model identifier against the Anthropic account's available models.

This is narrative assistance, not PDF form filling or a Westminster approval decision.

## Claude extraction integration

The server also exposes `POST /api/extract` with `{"pages":[{"filename":"synthetic-deed.txt","page":1,"text":"APN: 123-456-78"}]}`. It returns source-linked candidates for explicit human review. The server validates field IDs and verifies that each supporting quotation occurs in the supplied page text. This is not proof that the underlying document is genuine or current.

In `docs/index.html`, set `CLAUDE_API_BASE` to your deployed backend's HTTPS origin. Do not put `ANTHROPIC_API_KEY` in this file. Until the backend is deployed and the origin is configured, the Claude button is intentionally disabled. The browser sends extracted text, not the original PDF bytes, only after an explicit confirmation.

This endpoint is a development scaffold, not a production-safe service. Add authentication, rate limiting, abuse protection, access controls, logging/privacy policies, and data-processing approval before accepting actual property/title records. The backend currently has no authentication. The website's CORS origin restriction does not protect the endpoint against non-browser clients.
