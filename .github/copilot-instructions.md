# Copilot instructions

Build small, testable, provider-neutral modules. Preserve the human approval boundary.

- Never add real credentials, private records, or production data.
- Treat external writes, financial actions, sensitive-data handling, and destructive operations as high risk.
- Require explicit human approval before high-risk execution.
- Prefer typed task/result contracts and adapter interfaces.
- Add regression tests for every behavior change.
- Use pull requests; do not bypass failing checks.
- Explain security, privacy, cost, and rollback implications.
- Do not claim an integration works unless it has been tested with evidence.
