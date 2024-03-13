
class StateChoices:
    ENABLED = "enabled"
    DISABLED = "disabled"

    choices = (
        (ENABLED, ENABLED),
        (DISABLED, DISABLED),
    )


class EnvironmentChoices:
    GLOBAL = "global"
    ENVIRONMENT_SPECIFIC = "environment-specific"
    APPLICATION_SPECIFIC = "application-specific"

    choices = (
        (GLOBAL, GLOBAL),
        (ENVIRONMENT_SPECIFIC, ENVIRONMENT_SPECIFIC),
        (APPLICATION_SPECIFIC, APPLICATION_SPECIFIC),
    )
