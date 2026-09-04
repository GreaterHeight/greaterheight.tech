# Contact form integration

The static form is intentionally safe: it uses a `mailto:` fallback and does not claim that a submission has been delivered to a server.

For production lead capture, replace the form action with the approved serverless/API endpoint and add server-side validation, rate limiting, spam protection, logging policy, and notification routing.
