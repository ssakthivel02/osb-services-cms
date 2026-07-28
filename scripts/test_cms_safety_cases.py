def accepted(request):
    forbidden = {
        'tenant_override',
        'publish_without_approval',
        'bypass_malware_scan',
        'erase_revision_history',
        'unsigned_upload',
        'sensitive_content_without_dual_approval',
        'public_unapproved_revision'
    }
    return not any(request.get(key) for key in forbidden)

cases = [
    {'tenant_override': True},
    {'publish_without_approval': True},
    {'bypass_malware_scan': True},
    {'erase_revision_history': True},
    {'unsigned_upload': True},
    {'sensitive_content_without_dual_approval': True},
    {'public_unapproved_revision': True},
]
assert all(accepted(case) is False for case in cases)
assert accepted({'tenant_override': False, 'publish_without_approval': False}) is True
print('CMS safety cases passed')
