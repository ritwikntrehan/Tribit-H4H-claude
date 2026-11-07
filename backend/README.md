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
