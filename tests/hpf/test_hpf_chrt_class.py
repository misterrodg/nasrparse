from nasrparse.records.hpf import HPF_CHRT

from datetime import date

import unittest


class TestHPF_CHRT(unittest.TestCase):
    def setUp(self):
        self.maxDiff = None
        self.hpf_chrt = HPF_CHRT(
            "2025/10/30", "HYPER INT*MD*K6", "1", "MD", "US", "STAR"
        )

    def tearDown(self):
        pass

    def test_repr(self):
        result = repr(self.hpf_chrt)
        self.assertEqual(
            result,
            "HPF_CHRT ( "
            "EFF_DATE=datetime.date(2025, 10, 30), "
            "HP_NAME='HYPER INT*MD*K6', "
            "HP_NO=1, "
            "STATE_CODE='MD', "
            "COUNTRY_CODE='US', "
            "CHARTING_TYPE_DESC='STAR'"
            " )",
        ),

    def test_ordered_fields(self):
        result = self.hpf_chrt.ordered_fields()
        self.assertListEqual(
            result,
            [
                "eff_date",
                "hp_name",
                "hp_no",
                "state_code",
                "country_code",
                "charting_type_desc",
            ],
        )

    def test_to_dict(self):
        result = self.hpf_chrt.to_dict()
        self.assertDictEqual(
            result,
            {
                "eff_date": date(2025, 10, 30).strftime("%Y-%m-%d"),
                "hp_name": "HYPER INT*MD*K6",
                "hp_no": 1,
                "state_code": "MD",
                "country_code": "US",
                "charting_type_desc": "STAR",
            },
        )

    def test_to_str(self):
        result = self.hpf_chrt.to_str()
        self.assertEqual(
            result,
            "eff_date: 2025-10-30, "
            "hp_name: HYPER INT*MD*K6, "
            "hp_no: 1, "
            "state_code: MD, "
            "country_code: US, "
            "charting_type_desc: STAR",
        )
