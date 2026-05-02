# Security Policy

## Supported Versions

| Version | Supported |
| ------- | --------- |
| latest (main) | Yes |

## Reporting a Vulnerability

**Do not open a public GitHub issue for security vulnerabilities.**

Please report security issues by emailing the maintainers directly. Include as much detail as possible:

- A description of the vulnerability and its potential impact
- Steps to reproduce or proof-of-concept
- Affected components (backend, frontend, Docker config, etc.)
- Any suggested mitigations

You can expect an acknowledgement within **48 hours** and a status update within **7 days**.

## Scope

This policy covers vulnerabilities in the FARM template itself. Issues in upstream dependencies (FastAPI, Next.js, MongoDB, Clerk, etc.) should be reported to their respective maintainers.

## Security Considerations for Users

When deploying a project based on this template:

- **Never commit `.env` files.** Use `.env.example` as a reference only.
- Rotate all secrets (Mongo credentials, Clerk keys) before going to production.
- Restrict `BACKEND_CORS_ORIGINS` to known origins — do not use `*` in production.
- Run containers as non-root users in production deployments.
- Keep dependencies up to date; use `uv lock --upgrade` (backend) and `bun update` (frontend) regularly.
- Enable MongoDB authentication and restrict network access to the database port.
