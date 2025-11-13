from nasrparse.records.wxl import WXL_SVC
from nasrparse.records.types import WeatherServiceCode

from datetime import date

import unittest


class TestWXL_SVC(unittest.TestCase):
    def setUp(self):
        self.maxDiff = None
        self.wxl_svc = WXL_SVC(
            "2025/10/02",
            "JYO",
            "LEESBURG",
            "VA",
            "US",
            "NOTAM",
            "",
        )

    def tearDown(self):
        pass

    def test_repr(self):
        result = repr(self.wxl_svc)
        self.assertEqual(
            result,
            "WXL_SVC ( "
            "EFF_DATE=datetime.date(2025, 10, 2), "
            "WEA_ID='JYO', "
            "CITY='LEESBURG', "
            "STATE_CODE='VA', "
            "COUNTRY_CODE='US', "
            f"WEA_SVC_TYPE_CODE={WeatherServiceCode.NOTICE_TO_AIRMEN!r}, "
            "WEA_AFFECT_AREA=None"
            " )",
        ),

    def test_ordered_fields(self):
        result = self.wxl_svc.ordered_fields()
        self.assertListEqual(
            result,
            [
                "eff_date",
                "wea_id",
                "city",
                "state_code",
                "country_code",
                "wea_svc_type_code",
                "wea_affect_area",
            ],
        )

    def test_to_dict(self):
        result = self.wxl_svc.to_dict()
        self.assertDictEqual(
            result,
            {
                "eff_date": date(2025, 10, 2).strftime("%Y-%m-%d"),
                "wea_id": "JYO",
                "city": "LEESBURG",
                "state_code": "VA",
                "country_code": "US",
                "wea_svc_type_code": WeatherServiceCode.NOTICE_TO_AIRMEN.value,
                "wea_affect_area": None,
            },
        )

    def test_to_str(self):
        result = self.wxl_svc.to_str()
        self.assertEqual(
            result,
            "eff_date: 2025-10-02, "
            "wea_id: JYO, "
            "city: LEESBURG, "
            "state_code: VA, "
            "country_code: US, "
            "wea_svc_type_code: NOTAM, "
            "wea_affect_area: None",
        )
