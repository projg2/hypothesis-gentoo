"""Plugin to create "gentoo" hypothesis profile, disabling health checks"""

__version__ = "2"


def _hypothesis_setup_hook() -> None:
    import hypothesis

    hypothesis.settings.register_profile(
        "gentoo", suppress_health_check=list(hypothesis.HealthCheck)
    )
