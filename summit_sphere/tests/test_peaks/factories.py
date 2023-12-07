import factory.fuzzy
from factory.django import DjangoModelFactory

from summit_sphere.peaks.models import Peak, Region


class RegionFactory(DjangoModelFactory):
    class Meta:
        model = Region

    name = factory.Sequence(lambda n: "Region %d" % n)


class PeakFactory(DjangoModelFactory):
    class Meta:
        model = Peak

    name = factory.Sequence(lambda n: "Peak %d" % n)
    unicode_name = factory.SelfAttribute("name")
    elevation = factory.fuzzy.FuzzyDecimal(low=600, high=2700, precision=1)
    latitude = factory.Faker("latitude")
    longitude = factory.Faker("longitude")
    country_code = "PL"
    region = factory.SubFactory(RegionFactory)
