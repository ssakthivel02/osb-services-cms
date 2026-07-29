# ADR 0001: Server-authoritative content governance

## Decision
Tenant scope, workflow state, publication approval, revision identity, source attribution, media safety and rollback state are enforced by trusted server-side controls. Client-supplied tenant, role, approval, scan or publication claims are never authoritative.

## Consequences
Every state transition is versioned and audited. Sensitive content requires dual approval. Public delivery exposes only approved revisions and signed media references.
