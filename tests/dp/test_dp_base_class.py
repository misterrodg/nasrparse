from nasrparse.records.dp import DP_BASE

from datetime import date

import unittest


class TestDP_BASE(unittest.TestCase):
    def setUp(self):
        self.maxDiff = None
        self.dp_base = DP_BASE(
            "2025/10/02",
            "ARSNL5.CSN",
            "ARSENAL",
            "ZDC",
            "FIVE",
            "2016/07/21",
            "N",
            "SID",
            "HEF",
        )

    def tearDown(self):
        pass

    def test_repr(self):
        result = repr(self.dp_base)
        self.assertEqual(
            result,
            "DP_BASE ( "
            "EFF_DATE=datetime.date(2025, 10, 2), "
            "DP_COMPUTER_CODE='ARSNL5.CSN', "
            "DP_NAME='ARSENAL', "
            "ARTCC='ZDC', "
            "AMENDMENT_NO='FIVE', "
            "DP_AMEND_EFF_DATE=datetime.date(2016, 7, 21), "
            "RNAV_FLAG=False, "
            "GRAPHICAL_DP_TYPE='SID', "
            "SERVED_ARPT='HEF'"
            " )",
        ),

    def test_ordered_fields(self):
        result = self.dp_base.ordered_fields()
        self.assertListEqual(
            result,
            [
                "eff_date",
                "dp_computer_code",
                "dp_name",
                "artcc",
                "amendment_no",
                "dp_amend_eff_date",
                "rnav_flag",
                "graphical_dp_type",
                "served_arpt",
            ],
        )

    def test_to_dict(self):
        result = self.dp_base.to_dict()
        self.assertDictEqual(
            result,
            {
                "eff_date": date(2025, 10, 2).strftime("%Y-%m-%d"),
                "dp_computer_code": "ARSNL5.CSN",
                "dp_name": "ARSENAL",
                "artcc": "ZDC",
                "amendment_no": "FIVE",
                "dp_amend_eff_date": date(2016, 7, 21).strftime("%Y-%m-%d"),
                "rnav_flag": False,
                "graphical_dp_type": "SID",
                "served_arpt": "HEF",
            },
        )

    def test_to_str(self):
        result = self.dp_base.to_str()
        self.assertEqual(
            result,
            "eff_date: 2025-10-02, "
            "dp_computer_code: ARSNL5.CSN, "
            "dp_name: ARSENAL, "
            "artcc: ZDC, "
            "amendment_no: FIVE, "
            "dp_amend_eff_date: 2016-07-21, "
            "rnav_flag: False, "
            "graphical_dp_type: SID, "
            "served_arpt: HEF",
        )
