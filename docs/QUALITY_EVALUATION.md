# CMS Quality Evaluation

Required evidence:
- Cross-tenant reads and writes are rejected.
- Draft, review, approval, scheduling, publication, retirement and rollback are exercised.
- Stored-script, malformed markup and malicious upload fixtures are blocked.
- Every published item has source, ownership, revision and approval evidence.
- English and Tamil content is reviewed for semantic parity and readability.
- Images have alt text and audio/video has transcripts.
- Cache invalidation and scheduled publishing are deterministic and audited.
- Soft-delete recovery, backup, restore and disaster recovery tests pass.
- Load tests cover publication bursts and media processing.

A green policy validator is necessary but is not production evidence.
