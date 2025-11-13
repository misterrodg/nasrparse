from nasrparse.records.fss import FSS_RMK

from datetime import date

import unittest


class TestFSS_RMK(unittest.TestCase):
    def setUp(self):
        self.maxDiff = None
        self.fss_rmk = FSS_RMK(
            "2025/10/30",
            "ENA",
            "KENAI",
            "KENAI",
            "AK",
            "US",
            "GENERAL_REMARK",
            "12",
            "LAA WHEN ATCT CLSD.",
        )

    def tearDown(self):
        pass

    def test_repr(self):
        result = repr(self.fss_rmk)
        self.assertEqual(
            result,
            "FSS_RMK ( "
            "EFF_DATE=datetime.date(2025, 10, 30), "
            "FSS_ID='ENA', "
            "NAME='KENAI', "
            "CITY='KENAI', "
            "STATE_CODE='AK', "
            "COUNTRY_CODE='US', "
            "REF_COL_NAME='GENERAL_REMARK', "
            "REF_COL_SEQ_NO=12, "
            "REMARK='LAA WHEN ATCT CLSD.'"
            " )",
        ),

    def test_ordered_fields(self):
        result = self.fss_rmk.ordered_fields()
        self.assertListEqual(
            result,
            [
                "eff_date",
                "fss_id",
                "name",
                "city",
                "state_code",
                "country_code",
                "ref_col_name",
                "ref_col_seq_no",
                "remark",
            ],
        )

    def test_to_dict(self):
        result = self.fss_rmk.to_dict()
        self.assertDictEqual(
            result,
            {
                "eff_date": date(2025, 10, 30).strftime("%Y-%m-%d"),
                "fss_id": "ENA",
                "name": "KENAI",
                "city": "KENAI",
                "state_code": "AK",
                "country_code": "US",
                "ref_col_name": "GENERAL_REMARK",
                "ref_col_seq_no": 12,
                "remark": "LAA WHEN ATCT CLSD.",
            },
        )

    def test_to_str(self):
        result = self.fss_rmk.to_str()
        self.assertEqual(
            result,
            "eff_date: 2025-10-30, "
            "fss_id: ENA, "
            "name: KENAI, "
            "city: KENAI, "
            "state_code: AK, "
            "country_code: US, "
            "ref_col_name: GENERAL_REMARK, "
            "ref_col_seq_no: 12, "
            "remark: LAA WHEN ATCT CLSD.",
        )
