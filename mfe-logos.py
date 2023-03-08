from tutor import hooks

hooks.Filters.ENV_PATCHES.add_item(
    (
        "openedx-lms-development-settings",
        """
MFE_CONFIG["LOGO_URL"] = "http://local.overhang.io:8000/theming/asset/images/logo.png"
MFE_CONFIG["LOGO_TRADEMARK_URL"] = "http://local.overhang.io:8000/theming/asset/images/white-logo.png"
MFE_CONFIG["LOGO_WHITE_URL"] = "http://local.overhang.io:8000/theming/asset/images/white-logo.png"
MFE_CONFIG["FAVICON_URL"] = "http://local.overhang.io:8000/theming/asset/images/favicon.ico"
"""
    ),
 
)

