# ruff: noqa: D103

import pytest

from summit_sphere.tests.test_peaks.factories import PeakFactory, RegionFactory


@pytest.fixture
def peak():
    return PeakFactory.build()


@pytest.fixture
def region():
    return RegionFactory.build()
