from nasrparse.records.hpf import HPF_RMK

from datetime import date

import unittest


class TestHPF_RMK(unittest.TestCase):
    def setUp(self):
        self.maxDiff = None
        self.hpf_rmk = HPF_RMK(
            "2025/10/30",
            "HYPER INT*MD*K6",
            "1",
            "MD",
            "US",
            "HOLDING_PATTERN",
            "GENERAL_REMARK",
            "1",
            "CHART 210K ICON.",
        )

    def tearDown(self):
        pass

    def test_repr(self):
        result = repr(self.hpf_rmk)
        self.assertEqual(
            result,
            "HPF_RMK ( "
            "EFF_DATE=datetime.date(2025, 10, 30), "
            "HP_NAME='HYPER INT*MD*K6', "
            "HP_NO=1, "
            "STATE_CODE='MD', "
            "COUNTRY_CODE='US', "
            "TAB_NAME='HOLDING_PATTERN', "
            "REF_COL_NAME='GENERAL_REMARK', "
            "REF_COL_SEQ_NO=1, "
            "REMARK='CHART 210K ICON.'"
            " )",
        ),

    def test_ordered_fields(self):
        result = self.hpf_rmk.ordered_fields()
        self.assertListEqual(
            result,
            [
                "eff_date",
                "hp_name",
                "hp_no",
                "state_code",
                "country_code",
                "tab_name",
                "ref_col_name",
                "ref_col_seq_no",
                "remark",
            ],
        )

    def test_to_dict(self):
        result = self.hpf_rmk.to_dict()
        self.assertDictEqual(
            result,
            {
                "eff_date": date(2025, 10, 30).strftime("%Y-%m-%d"),
                "hp_name": "HYPER INT*MD*K6",
                "hp_no": 1,
                "state_code": "MD",
                "country_code": "US",
                "tab_name": "HOLDING_PATTERN",
                "ref_col_name": "GENERAL_REMARK",
                "ref_col_seq_no": 1,
                "remark": "CHART 210K ICON.",
            },
        )

    def test_to_str(self):
        result = self.hpf_rmk.to_str()
        self.assertEqual(
            result,
            "eff_date: 2025-10-30, "
            "hp_name: HYPER INT*MD*K6, "
            "hp_no: 1, "
            "state_code: MD, "
            "country_code: US, "
            "tab_name: HOLDING_PATTERN, "
            "ref_col_name: GENERAL_REMARK, "
            "ref_col_seq_no: 1, "
            "remark: CHART 210K ICON.",
        )
