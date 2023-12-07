# ruff: noqa: D103

import pytest
from django.db import connection
from django.test.utils import CaptureQueriesContext
from rest_framework.test import APIClient


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def capture_queries():
    with CaptureQueriesContext(connection) as context:
        yield context
