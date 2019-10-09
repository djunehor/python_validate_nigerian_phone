import unittest
import random

from valid_nigerian_phone import NigerianPhone


class TestCase(unittest.TestCase):
    def test_full_country_phone(self):
        test_cases = ['+2348135087966', '2348135087966', '08135087966', '8135087966', '04221542', '+234 1 456 7854', '0425 5832']
        self.app = NigerianPhone('+2348135087966')
        assert self.app.is_valid() == True

    def test_full_country_phone_without_plus(self):
        self.app = NigerianPhone('2348135087966')
        assert self.app.is_valid() == True

    def test_phone_without_country_code(self):
        self.app = NigerianPhone('08135087966')
        assert self.app.is_valid() == True

    def test_is_phone(self):
        self.app = NigerianPhone('2348135087966')
        assert self.app.is_valid_phone == True

    def test_is_land_line(self):
        self.app = NigerianPhone('+234 1 456 7854')
        assert self.app.is_valid_land_line == True

    def test_network(self):
        self.app = NigerianPhone('+2348135087966')
        assert self.app.get_network() == 'mtn'

    def test_prefix(self):
        self.app = NigerianPhone('+2348135087966')
        assert self.app.get_network_by_prefix('0703') == 'mtn'

    def test_get_area_code_by_name(self):
        self.app = NigerianPhone('+2348135087966')
        assert self.app.get_area_code_by_name('Enugu') == '42'


if __name__ == "__main__":
    unittest.main()