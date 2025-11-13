from nasrparse.records.apt import APT_ATT
from nasrparse.records.types import SiteTypeCode

from datetime import date

import unittest


class TestAPT_ATT(unittest.TestCase):
    def setUp(self):
        self.maxDiff = None
        self.apt_att = APT_ATT(
            "2025/10/30",
            "00103.",
            "A",
            "AL",
            "0J0",
            "ABBEVILLE",
            "US",
            "1",
            "UNATNDD",
            "",
            "",
        )

    def tearDown(self):
        pass

    def test_repr(self):
        result = repr(self.apt_att)
        self.assertEqual(
            result,
            "APT_ATT ( "
            "EFF_DATE=datetime.date(2025, 10, 30), "
            "SITE_NO='00103.', "
            f"SITE_TYPE_CODE={SiteTypeCode.AIRPORT!r}, "
            "STATE_CODE='AL', "
            "ARPT_ID='0J0', "
            "CITY='ABBEVILLE', "
            "COUNTRY_CODE='US', "
            "SKED_SEQ_NO=1, "
            "MONTH='UNATNDD', "
            "DAY=None, "
            "HOUR=None"
            " )",
        ),

    def test_ordered_fields(self):
        result = self.apt_att.ordered_fields()
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
                "sked_seq_no",
                "month",
                "day",
                "hour",
            ],
        )

    def test_to_dict(self):
        result = self.apt_att.to_dict()
        self.assertDictEqual(
            result,
            {
                "eff_date": date(2025, 10, 30).strftime("%Y-%m-%d"),
                "site_no": "00103.",
                "site_type_code": SiteTypeCode.AIRPORT.value,
                "state_code": "AL",
                "arpt_id": "0J0",
                "city": "ABBEVILLE",
                "country_code": "US",
                "sked_seq_no": 1,
                "month": "UNATNDD",
                "day": None,
                "hour": None,
            },
        )

    def test_to_str(self):
        result = self.apt_att.to_str()
        self.assertEqual(
            result,
            "eff_date: 2025-10-30, "
            "site_no: 00103., "
            "site_type_code: A, "
            "state_code: AL, "
            "arpt_id: 0J0, "
            "city: ABBEVILLE, "
            "country_code: US, "
            "sked_seq_no: 1, "
            "month: UNATNDD, "
            "day: None, "
            "hour: None",
        )
