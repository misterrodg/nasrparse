from nasrparse.records.apt import APT_RMK
from nasrparse.records.types import SiteTypeCode

from datetime import date

import unittest


class TestAPT_RMK(unittest.TestCase):
    def setUp(self):
        self.maxDiff = None
        self.apt_rmk = APT_RMK(
            "2025/10/30",
            "00103.",
            "A",
            "AL",
            "0J0",
            "ABBEVILLE",
            "US",
            "E111",
            "AIRPORT",
            "ASP_ANLYS_DTRM_CODE",
            "",
            "1",
            "EXISTED PRIOR TO MAY 15, 1959.",
        )

    def tearDown(self):
        pass

    def test_repr(self):
        result = repr(self.apt_rmk)
        self.assertEqual(
            result,
            "APT_RMK ( "
            "EFF_DATE=datetime.date(2025, 10, 30), "
            "SITE_NO='00103.', "
            f"SITE_TYPE_CODE={SiteTypeCode.AIRPORT!r}, "
            "STATE_CODE='AL', "
            "ARPT_ID='0J0', "
            "CITY='ABBEVILLE', "
            "COUNTRY_CODE='US', "
            "LEGACY_ELEMENT_NUMBER='E111', "
            "TAB_NAME='AIRPORT', "
            "REF_COL_NAME='ASP_ANLYS_DTRM_CODE', "
            "ELEMENT=None, "
            "REF_COL_SEQ_NO=1, "
            "REMARK='EXISTED PRIOR TO MAY 15, 1959.'"
            " )",
        ),

    def test_ordered_fields(self):
        result = self.apt_rmk.ordered_fields()
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
                "legacy_element_number",
                "tab_name",
                "ref_col_name",
                "element",
                "ref_col_seq_no",
                "remark",
            ],
        )

    def test_to_dict(self):
        result = self.apt_rmk.to_dict()
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
                "legacy_element_number": "E111",
                "tab_name": "AIRPORT",
                "ref_col_name": "ASP_ANLYS_DTRM_CODE",
                "element": None,
                "ref_col_seq_no": 1,
                "remark": "EXISTED PRIOR TO MAY 15, 1959.",
            },
        )

    def test_to_str(self):
        result = self.apt_rmk.to_str()
        self.assertEqual(
            result,
            "eff_date: 2025-10-30, "
            "site_no: 00103., "
            "site_type_code: A, "
            "state_code: AL, "
            "arpt_id: 0J0, "
            "city: ABBEVILLE, "
            "country_code: US, "
            "legacy_element_number: E111, "
            "tab_name: AIRPORT, "
            "ref_col_name: ASP_ANLYS_DTRM_CODE, "
            "element: None, "
            "ref_col_seq_no: 1, "
            "remark: EXISTED PRIOR TO MAY 15, 1959.",
        )
