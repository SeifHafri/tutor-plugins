from tutor import hooks

hooks.Filters.ENV_PATCHES.add_item(
  (
    "openedx-lms-development-settings",
     'CORS_ORIGIN_WHITELIST.append("http://localhost:2023")',
     
     
  ),
)

