"""Plugin to create "gentoo" hypothesis profile, disabling health checks"""

__version__ = "0"


def _hypothesis_setup_hook():
    import hypothesis

    hypothesis.settings.register_profile(
        "gentoo", suppress_health_check=list(hypothesis.HealthCheck)
    )
