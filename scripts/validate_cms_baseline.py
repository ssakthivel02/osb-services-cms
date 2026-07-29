import json
from pathlib import Path

root = Path(__file__).resolve().parents[1]
cms = json.loads((root / 'config/cms-policy.json').read_text())
media = json.loads((root / 'config/media-policy.json').read_text())

assert cms['apiPrefix'].startswith('/api/v1/')
assert {'en-GB', 'ta-IN'} <= set(cms['requiredLocales'])
assert cms['authenticationRequired'] is True
assert cms['tenantIsolation'] is True
assert cms['serverAuthoritativeTenantScope'] is True
assert cms['approvalRequiredForPublish'] is True
assert cms['dualApprovalForSensitiveContent'] is True
assert cms['immutableRevisionHistory'] is True
assert cms['accessibilityReviewRequired'] is True
assert media['malwareScanRequired'] is True
assert media['metadataStrippingRequired'] is True
assert media['altTextRequiredForImages'] is True
assert media['transcriptRequiredForAudioVideo'] is True
print('CMS baseline validation passed')
