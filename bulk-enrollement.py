from tutor import hooks

hooks.Filters.ENV_PATCHES.add_item(
    (
        "lms-env-features",
        """
"ENABLE_BULK_ENROLLMENT_VIEW": true
"""
    )
)
