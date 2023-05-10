from tutor import hooks

hooks.Filters.ENV_PATCHES.add_item(
    (
        "lms-env-features",
        """
"SESSION_COOKIE_DOMAIN": "local.overhang.io"
"""
    )
)

