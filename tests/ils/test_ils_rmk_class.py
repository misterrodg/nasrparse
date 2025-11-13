from nasrparse.records.ils import ILS_RMK
from nasrparse.records.types import SiteTypeCode, SystemTypeCode

from datetime import date

import unittest


class TestILS_RMK(unittest.TestCase):
    def setUp(self):
        self.maxDiff = None
        self.ils_rmk = ILS_RMK(
            "2025/10/30",
            "25847.1",
            "A",
            "VA",
            "JYO",
            "LEESBURG",
            "US",
            "17",
            "JYO",
            "LD",
            "ILS",
            "",
            "GENERAL_REMARK",
            "2",
            "ILS CLASSIFICATION CODE IE.",
        )

    def tearDown(self):
        pass

    def test_repr(self):
        result = repr(self.ils_rmk)
        self.assertEqual(
            result,
            "ILS_RMK ( "
            "EFF_DATE=datetime.date(2025, 10, 30), "
            "SITE_NO='25847.1', "
            f"SITE_TYPE_CODE={SiteTypeCode.AIRPORT!r}, "
            "STATE_CODE='VA', "
            "ARPT_ID='JYO', "
            "CITY='LEESBURG', "
            "COUNTRY_CODE='US', "
            "RWY_END_ID='17', "
            "ILS_LOC_ID='JYO', "
            f"SYSTEM_TYPE_CODE={SystemTypeCode.ILS_DME!r}, "
            "TAB_NAME='ILS', "
            "ILS_COMP_TYPE_CODE=None, "
            "REF_COL_NAME='GENERAL_REMARK', "
            "REF_COL_SEQ_NO=2, "
            "REMARK='ILS CLASSIFICATION CODE IE.'"
            " )",
        ),

    def test_ordered_fields(self):
        result = self.ils_rmk.ordered_fields()
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
                "rwy_end_id",
                "ils_loc_id",
                "system_type_code",
                "tab_name",
                "ils_comp_type_code",
                "ref_col_name",
                "ref_col_seq_no",
                "remark",
            ],
        )

    def test_to_dict(self):
        result = self.ils_rmk.to_dict()
        self.assertDictEqual(
            result,
            {
                "eff_date": date(2025, 10, 30).strftime("%Y-%m-%d"),
                "site_no": "25847.1",
                "site_type_code": SiteTypeCode.AIRPORT.value,
                "state_code": "VA",
                "arpt_id": "JYO",
                "city": "LEESBURG",
                "country_code": "US",
                "rwy_end_id": "17",
                "ils_loc_id": "JYO",
                "system_type_code": SystemTypeCode.ILS_DME.value,
                "tab_name": "ILS",
                "ils_comp_type_code": None,
                "ref_col_name": "GENERAL_REMARK",
                "ref_col_seq_no": 2,
                "remark": "ILS CLASSIFICATION CODE IE.",
            },
        )

    def test_to_str(self):
        result = self.ils_rmk.to_str()
        self.assertEqual(
            result,
            "eff_date: 2025-10-30, "
            "site_no: 25847.1, "
            "site_type_code: A, "
            "state_code: VA, "
            "arpt_id: JYO, "
            "city: LEESBURG, "
            "country_code: US, "
            "rwy_end_id: 17, "
            "ils_loc_id: JYO, "
            "system_type_code: LD, "
            "tab_name: ILS, "
            "ils_comp_type_code: None, "
            "ref_col_name: GENERAL_REMARK, "
            "ref_col_seq_no: 2, "
            "remark: ILS CLASSIFICATION CODE IE.",
        )
