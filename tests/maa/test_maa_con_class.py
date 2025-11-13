from nasrparse.records.maa import MAA_CON

from datetime import date

import unittest


class TestMAA_CON(unittest.TestCase):
    def setUp(self):
        self.maxDiff = None
        self.maa_con = MAA_CON(
            "2025/10/30", "APA001", "1", "", "WASHINGTON HUB FSS", "123.6", "N", "", ""
        )

    def tearDown(self):
        pass

    def test_repr(self):
        result = repr(self.maa_con)
        self.assertEqual(
            result,
            "MAA_CON ( "
            "EFF_DATE=datetime.date(2025, 10, 30), "
            "MAA_ID='APA001', "
            "FREQ_SEQ=1, "
            "FAC_ID=None, "
            "FAC_NAME='WASHINGTON HUB FSS', "
            "COMMERCIAL_FREQ='123.6', "
            "COMMERCIAL_CHART_FLAG=False, "
            "MIL_FREQ=None, "
            "MIL_CHART_FLAG=None"
            " )",
        ),

    def test_ordered_fields(self):
        result = self.maa_con.ordered_fields()
        self.assertListEqual(
            result,
            [
                "eff_date",
                "maa_id",
                "freq_seq",
                "fac_id",
                "fac_name",
                "commercial_freq",
                "commercial_chart_flag",
                "mil_freq",
                "mil_chart_flag",
            ],
        )

    def test_to_dict(self):
        result = self.maa_con.to_dict()
        self.assertDictEqual(
            result,
            {
                "eff_date": date(2025, 10, 30).strftime("%Y-%m-%d"),
                "maa_id": "APA001",
                "freq_seq": 1,
                "fac_id": None,
                "fac_name": "WASHINGTON HUB FSS",
                "commercial_freq": "123.6",
                "commercial_chart_flag": False,
                "mil_freq": None,
                "mil_chart_flag": None,
            },
        )

    def test_to_str(self):
        result = self.maa_con.to_str()
        self.assertEqual(
            result,
            "eff_date: 2025-10-30, "
            "maa_id: APA001, "
            "freq_seq: 1, "
            "fac_id: None, "
            "fac_name: WASHINGTON HUB FSS, "
            "commercial_freq: 123.6, "
            "commercial_chart_flag: False, "
            "mil_freq: None, "
            "mil_chart_flag: None",
        )
