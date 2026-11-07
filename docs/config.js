// Public deployment configuration only. No API keys or access tokens.
// Render serves frontend and API from the same origin. GitHub Pages stays demo-only until configured.
window.H4H_API_BASE = window.location.hostname.endsWith('.onrender.com') ? window.location.origin : '';
