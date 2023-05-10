from tutor import hooks

hooks.Filters.ENV_PATCHES.add_item(
    (
        "common-env-features",
        "'ENABLE_OPENBADGES' : true",
),
(
	"openedx-lms-common-settings",
        """
        "'BADGR_USERNAME': is_hafri@esi.dz "
        "'BADGR_PASSWORD': 04032001Seif "
        "'BADGR_TOKENS_CACHE_KEY' = secret-test-cache-key"
        "'BADGR_BASE_URL': https://badgr.io/"
        "'BADGR_ISSUER_SLUG': Seif Hafri "
	"'BADGR_ENABLE_NOTIFICATIONS': true"
	"""
),


    ),
