# CMS Threat Model

## Protected assets
Content, media, translations, source records, publishing schedules, revision history, tenant metadata and moderation evidence.

## Principal threats
- Cross-tenant content disclosure or modification
- Unauthorised publication or rollback
- Stored script injection and malicious uploads
- Copyright, source or attribution misrepresentation
- Sensitive child, credential or payment data entering content
- Revision-history tampering
- Translation drift between English and Tamil
- Scheduled-publishing abuse and cache poisoning

## Required controls
Authentication, server-authoritative tenant scope, least privilege, workflow approval, immutable revisions, output encoding, sanitisation, malware scanning, signed uploads, source attribution, audit logging, soft deletion, backup and recovery testing.
