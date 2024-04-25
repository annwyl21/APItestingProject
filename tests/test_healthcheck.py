import logging as logger
import pytest

@pytest.mark.healthcheck
def test_healthcheck_1():
    logger.info("First Test Health Check 1")
