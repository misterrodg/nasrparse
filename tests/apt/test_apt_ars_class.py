from nasrparse.records.apt import APT_ARS
from nasrparse.records.types import ArrestDeviceCode, SiteTypeCode

from datetime import date

import unittest


class TestAPT_ARS(unittest.TestCase):
    def setUp(self):
        self.maxDiff = None
        self.apt_ars = APT_ARS(
            "2025/10/30",
            "00447.",
            "A",
            "AL",
            "MGM",
            "MONTGOMERY",
            "US",
            "10/28",
            "10",
            "BAK-12B",
        )

    def tearDown(self):
        pass

    def test_repr(self):
        result = repr(self.apt_ars)
        self.assertEqual(
            result,
            "APT_ARS ( "
            "EFF_DATE=datetime.date(2025, 10, 30), "
            "SITE_NO='00447.', "
            f"SITE_TYPE_CODE={SiteTypeCode.AIRPORT!r}, "
            "STATE_CODE='AL', "
            "ARPT_ID='MGM', "
            "CITY='MONTGOMERY', "
            "COUNTRY_CODE='US', "
            "RWY_ID='10/28', "
            "RWY_END_ID='10', "
            f"ARREST_DEVICE_CODE={ArrestDeviceCode.BAK_12B!r}"
            " )",
        )

    def test_ordered_fields(self):
        result = self.apt_ars.ordered_fields()
        self.assertListEqual(
            result,
            [
                "eff_date",
                "site_no",
                "site_type_code",
                "state_code",
                "arpt_id",
                "city",
                "country_code",
                "rwy_id",
                "rwy_end_id",
                "arrest_device_code",
            ],
        )

    def test_to_dict(self):
        result = self.apt_ars.to_dict()
        self.assertDictEqual(
            result,
            {
                "eff_date": date(2025, 10, 30).strftime("%Y-%m-%d"),
                "site_no": "00447.",
                "site_type_code": "A",
                "state_code": "AL",
                "arpt_id": "MGM",
                "city": "MONTGOMERY",
                "country_code": "US",
                "rwy_id": "10/28",
                "rwy_end_id": "10",
                "arrest_device_code": ArrestDeviceCode.BAK_12B.value,
            },
        )

    def test_to_str(self):
        result = self.apt_ars.to_str()
        self.assertEqual(
            result,
            "eff_date: 2025-10-30, "
            "site_no: 00447., "
            "site_type_code: A, "
            "state_code: AL, "
            "arpt_id: MGM, "
            "city: MONTGOMERY, "
            "country_code: US, "
            "rwy_id: 10/28, "
            "rwy_end_id: 10, "
            "arrest_device_code: BAK-12B",
        )
