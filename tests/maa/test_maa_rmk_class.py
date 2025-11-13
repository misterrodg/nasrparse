from nasrparse.records.maa import MAA_RMK

from datetime import date

import unittest


class TestMAA_RMK(unittest.TestCase):
    def setUp(self):
        self.maxDiff = None
        self.maa_rmk = MAA_RMK(
            "2025/10/30",
            "LVA001",
            "MISC_ACTIVITY_AREA",
            "GENERAL_REMARK",
            "1",
            "POWERED PARACHUTE OPERATIONS IN THE PURCELLVILLE, VIRGINIA AREA, MOST GENERALLY ON WEEKENDS. THE AREA IS 307 DEGREES AND 8 NM NORTHWEST OF LEESBURG EXECUTIVE AIRPORT.",
        )

    def tearDown(self):
        pass

    def test_repr(self):
        result = repr(self.maa_rmk)
        self.assertEqual(
            result,
            "MAA_RMK ( "
            "EFF_DATE=datetime.date(2025, 10, 30), "
            "MAA_ID='LVA001', "
            "TAB_NAME='MISC_ACTIVITY_AREA', "
            "REF_COL_NAME='GENERAL_REMARK', "
            "REF_COL_SEQ_NO=1, "
            "REMARK='POWERED PARACHUTE OPERATIONS IN THE PURCELLVILLE, VIRGINIA AREA, MOST GENERALLY ON WEEKENDS. THE AREA IS 307 DEGREES AND 8 NM NORTHWEST OF LEESBURG EXECUTIVE AIRPORT.'"
            " )",
        ),

    def test_ordered_fields(self):
        result = self.maa_rmk.ordered_fields()
        self.assertListEqual(
            result,
            [
                "eff_date",
                "maa_id",
                "tab_name",
                "ref_col_name",
                "ref_col_seq_no",
                "remark",
            ],
        )

    def test_to_dict(self):
        result = self.maa_rmk.to_dict()
        self.assertDictEqual(
            result,
            {
                "eff_date": date(2025, 10, 30).strftime("%Y-%m-%d"),
                "maa_id": "LVA001",
                "tab_name": "MISC_ACTIVITY_AREA",
                "ref_col_name": "GENERAL_REMARK",
                "ref_col_seq_no": 1,
                "remark": "POWERED PARACHUTE OPERATIONS IN THE PURCELLVILLE, VIRGINIA AREA, MOST GENERALLY ON WEEKENDS. THE AREA IS 307 DEGREES AND 8 NM NORTHWEST OF LEESBURG EXECUTIVE AIRPORT.",
            },
        )

    def test_to_str(self):
        result = self.maa_rmk.to_str()
        self.assertEqual(
            result,
            "eff_date: 2025-10-30, "
            "maa_id: LVA001, "
            "tab_name: MISC_ACTIVITY_AREA, "
            "ref_col_name: GENERAL_REMARK, "
            "ref_col_seq_no: 1, "
            "remark: POWERED PARACHUTE OPERATIONS IN THE PURCELLVILLE, VIRGINIA AREA, MOST GENERALLY ON WEEKENDS. THE AREA IS 307 DEGREES AND 8 NM NORTHWEST OF LEESBURG EXECUTIVE AIRPORT.",
        )
