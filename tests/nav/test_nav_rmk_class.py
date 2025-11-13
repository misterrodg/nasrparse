from nasrparse.records.nav import NAV_RMK
from nasrparse.records.types import PointCode

from datetime import date

import unittest


class TestNAV_RMK(unittest.TestCase):
    def setUp(self):
        self.maxDiff = None
        self.nav_rmk = NAV_RMK(
            "2025/10/30",
            "AML",
            "VOR/DME",
            "VA",
            "HERNDON",
            "US",
            "NAVIGATION_AID",
            "GENERAL_REMARK",
            "3",
            "VOR UNUSBL 055-092 BLW 4500 FT; 093-115; 116-210 BLW 4500 FT.",
        )

    def tearDown(self):
        pass

    def test_repr(self):
        result = repr(self.nav_rmk)
        self.assertEqual(
            result,
            "NAV_RMK ( "
            "EFF_DATE=datetime.date(2025, 10, 30), "
            "NAV_ID='AML', "
            f"NAV_TYPE={PointCode.VOR_DME!r}, "
            "STATE_CODE='VA', "
            "CITY='HERNDON', "
            "COUNTRY_CODE='US', "
            "TAB_NAME='NAVIGATION_AID', "
            "REF_COL_NAME='GENERAL_REMARK', "
            "REF_COL_SEQ_NO=3, "
            "REMARK='VOR UNUSBL 055-092 BLW 4500 FT; 093-115; 116-210 BLW 4500 FT.'"
            " )",
        ),

    def test_ordered_fields(self):
        result = self.nav_rmk.ordered_fields()
        self.assertListEqual(
            result,
            [
                "eff_date",
                "nav_id",
                "nav_type",
                "state_code",
                "city",
                "country_code",
                "tab_name",
                "ref_col_name",
                "ref_col_seq_no",
                "remark",
            ],
        )

    def test_to_dict(self):
        result = self.nav_rmk.to_dict()
        self.assertDictEqual(
            result,
            {
                "eff_date": date(2025, 10, 30).strftime("%Y-%m-%d"),
                "nav_id": "AML",
                f"nav_type": PointCode.VOR_DME.value,
                "state_code": "VA",
                "city": "HERNDON",
                "country_code": "US",
                "tab_name": "NAVIGATION_AID",
                "ref_col_name": "GENERAL_REMARK",
                "ref_col_seq_no": 3,
                "remark": "VOR UNUSBL 055-092 BLW 4500 FT; 093-115; 116-210 BLW 4500 FT.",
            },
        )

    def test_to_str(self):
        result = self.nav_rmk.to_str()
        self.assertEqual(
            result,
            "eff_date: 2025-10-30, "
            "nav_id: AML, "
            "nav_type: VOR/DME, "
            "state_code: VA, "
            "city: HERNDON, "
            "country_code: US, "
            "tab_name: NAVIGATION_AID, "
            "ref_col_name: GENERAL_REMARK, "
            "ref_col_seq_no: 3, "
            "remark: VOR UNUSBL 055-092 BLW 4500 FT; 093-115; 116-210 BLW 4500 FT.",
        )
