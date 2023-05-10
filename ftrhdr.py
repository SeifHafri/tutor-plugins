from tutor import hooks

hooks.Filters.ENV_PATCHES.add_item(
    (
        "mfe-dockerfile-post-npm-install",
        """
# npm package
RUN npm install '@edx/frontend-component-header@git+https://github.com/SeifHafri/frontend-component-footer.git'
""",
    )
)

