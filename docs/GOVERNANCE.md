# Governance and Quality Assurance

## Human authority

A human owner remains the final authority. External messages, repository mutations, payments, purchases, handling sensitive information, and destructive operations require explicit approval.

## Agent passports

Every production clone must declare:

- stable name and owner;
- purpose and permitted capabilities;
- allowed data sources and destinations;
- spending and rate limits;
- escalation contact;
- version and change history;
- shutdown procedure.

## Quality gates

Changes require a pull request, passing automated checks, no committed secrets, tests for new behavior, documented risk decisions, and rollback instructions for production changes.

## Data rules

Collect the minimum information required. Separate public, internal, confidential, and regulated data. Never use confidential customer or corporate material as training data without documented authorization.
