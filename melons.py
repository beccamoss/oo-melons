"""Classes for melon orders."""
from random import randint
import datetime

class AbstractMelonOrder(object):
    """Parent class for subclasses to inherit shared attributes and methods"""

    def __init__(self, species, qty, country_code=None):
        self.species = species
        self.qty = qty
        self.shipped = False
        if country_code:
            self.country_code = country_code

    def get_base_price(self):
        base_price = randint(5, 9)
        order_time = datetime.datetime.now()
        if datetime.date.weekday(order_time) in range (0, 5) and order_time.hour in range(8, 12):
            base_price += 4

        return base_price

    def get_total(self):
        """Calculate price, including tax."""

        base_price = self.get_base_price()

        if self.species == "Christmas melons":
            base_price = base_price * 1.5

        total = (1 + self.tax) * self.qty * base_price
        return total

    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True


class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""

    order_type = "domestic"
    tax = 0.08


class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""

    order_type = "international"
    tax = 0.17

    def __init__(self, species, qty, country_code):
        """instantiates by calling parent dunder init"""
        super(InternationalMelonOrder, self).__init__(species, qty, country_code)

    def get_total(self):
        total = super(InternationalMelonOrder, self).get_total()
        if self.qty < 10:
            total += 3
        return total

    def get_country_code(self):
        """Return the country code."""

        return self.country_code


class GovernmentMelonOrder(AbstractMelonOrder):
    """A melon order from the US Government"""

    tax = 0.0
    order_type = "us_government"
    passed_inspection = False

    def mark_inspection(self, passed):
        if passed:
            self.passed_inspection = True
