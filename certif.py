from tutor import hooks

hooks.Filters.ENV_PATCHES.add_item(
    (
        "common-env-features",
        """
'CERTIFICATES_HTML_VIEW': true,
"""
    )
)
