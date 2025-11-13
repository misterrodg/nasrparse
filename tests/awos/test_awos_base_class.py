from nasrparse.records.awos import AWOS_BASE
from nasrparse.records.types import HemisCode, MethodCode, SiteTypeCode

from datetime import date

import unittest


class TestAWOS_BASE(unittest.TestCase):
    def setUp(self):
        self.maxDiff = None
        self.awos_base = AWOS_BASE(
            "2025/10/30",
            "BCB",
            "AWOS-3",
            "VA",
            "BLACKSBURG",
            "US",
            "1991/10/16",
            "N",
            "37",
            "12",
            "28.8221",
            "N",
            "37.20800613",
            "80",
            "24",
            "45.675",
            "W",
            "-80.4126875",
            "2100.5",
            "",
            "540-231-4837",
            "",
            "25644.",
            "A",
            "",
        )

    def tearDown(self):
        pass

    def test_repr(self):
        result = repr(self.awos_base)
        self.assertEqual(
            result,
            "AWOS_BASE ( "
            "EFF_DATE=datetime.date(2025, 10, 30), "
            "ASOS_AWOS_ID='BCB', "
            "ASOS_AWOS_TYPE='AWOS-3', "
            "STATE_CODE='VA', "
            "CITY='BLACKSBURG', "
            "COUNTRY_CODE='US', "
            "COMMISSIONED_DATE=datetime.date(1991, 10, 16), "
            "NAVAID_FLAG=False, "
            "LAT_DEG=37, "
            "LAT_MIN=12, "
            "LAT_SEC=28.8221, "
            f"LAT_HEMIS={HemisCode.NORTH!r}, "
            "LAT_DECIMAL=37.20800613, "
            "LON_DEG=80, "
            "LON_MIN=24, "
            "LON_SEC=45.675, "
            f"LON_HEMIS={HemisCode.WEST!r}, "
            "LON_DECIMAL=-80.4126875, "
            "ELEV=2100.5, "
            f"SURVEY_METHOD_CODE={MethodCode.NULL!r}, "
            "PHONE_NO='540-231-4837', "
            "SECOND_PHONE_NO=None, "
            "SITE_NO='25644.', "
            f"SITE_TYPE_CODE={SiteTypeCode.AIRPORT!r}, "
            "REMARK=None"
            " )",
        ),

    def test_ordered_fields(self):
        result = self.awos_base.ordered_fields()
        self.assertListEqual(
            result,
            [
                "eff_date",
                "asos_awos_id",
                "asos_awos_type",
                "state_code",
                "city",
                "country_code",
                "commissioned_date",
                "navaid_flag",
                "lat_deg",
                "lat_min",
                "lat_sec",
                "lat_hemis",
                "lat_decimal",
                "lon_deg",
                "lon_min",
                "lon_sec",
                "lon_hemis",
                "lon_decimal",
                "elev",
                "survey_method_code",
                "phone_no",
                "second_phone_no",
                "site_no",
                "site_type_code",
                "remark",
            ],
        )

    def test_to_dict(self):
        result = self.awos_base.to_dict()
        self.assertDictEqual(
            result,
            {
                "eff_date": date(2025, 10, 30).strftime("%Y-%m-%d"),
                "asos_awos_id": "BCB",
                "asos_awos_type": "AWOS-3",
                "state_code": "VA",
                "city": "BLACKSBURG",
                "country_code": "US",
                "commissioned_date": date(1991, 10, 16).strftime("%Y-%m-%d"),
                "navaid_flag": False,
                "lat_deg": 37,
                "lat_min": 12,
                "lat_sec": 28.8221,
                "lat_hemis": HemisCode.NORTH.value,
                "lat_decimal": 37.20800613,
                "lon_deg": 80,
                "lon_min": 24,
                "lon_sec": 45.675,
                "lon_hemis": HemisCode.WEST.value,
                "lon_decimal": -80.4126875,
                "elev": 2100.5,
                "survey_method_code": MethodCode.NULL.value,
                "phone_no": "540-231-4837",
                "second_phone_no": None,
                "site_no": "25644.",
                "site_type_code": SiteTypeCode.AIRPORT.value,
                "remark": None,
            },
        )

    def test_to_str(self):
        result = self.awos_base.to_str()
        self.assertEqual(
            result,
            "eff_date: 2025-10-30, "
            "asos_awos_id: BCB, "
            "asos_awos_type: AWOS-3, "
            "state_code: VA, "
            "city: BLACKSBURG, "
            "country_code: US, "
            "commissioned_date: 1991-10-16, "
            "navaid_flag: False, "
            "lat_deg: 37, "
            "lat_min: 12, "
            "lat_sec: 28.8221, "
            "lat_hemis: N, "
            "lat_decimal: 37.20800613, "
            "lon_deg: 80, "
            "lon_min: 24, "
            "lon_sec: 45.675, "
            "lon_hemis: W, "
            "lon_decimal: -80.4126875, "
            "elev: 2100.5, "
            "survey_method_code: None, "
            "phone_no: 540-231-4837, "
            "second_phone_no: None, "
            "site_no: 25644., "
            "site_type_code: A, "
            "remark: None",
        )
