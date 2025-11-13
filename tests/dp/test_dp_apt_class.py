from nasrparse.records.dp import DP_APT

from datetime import date

import unittest


class TestDP_APT(unittest.TestCase):
    def setUp(self):
        self.maxDiff = None
        self.dp_apt = DP_APT(
            "2025/10/02", "ARSENAL", "ZDC", "ARSNL5.CSN", "SHRLI-CSN", "1", "HEF", "34L"
        )

    def tearDown(self):
        pass

    def test_repr(self):
        result = repr(self.dp_apt)
        self.assertEqual(
            result,
            "DP_APT ( "
            "EFF_DATE=datetime.date(2025, 10, 2), "
            "DP_COMPUTER_CODE='ARSENAL', "
            "DP_NAME='ZDC', "
            "ARTCC='ARSNL5.CSN', "
            "BODY_NAME='SHRLI-CSN', "
            "BODY_SEQ='1', "
            "ARPT_ID='HEF', "
            "RWY_END_ID='34L'"
            " )",
        ),

    def test_ordered_fields(self):
        result = self.dp_apt.ordered_fields()
        self.assertListEqual(
            result,
            [
                "eff_date",
                "dp_computer_code",
                "dp_name",
                "artcc",
                "body_name",
                "body_seq",
                "arpt_id",
                "rwy_end_id",
            ],
        )

    def test_to_dict(self):
        result = self.dp_apt.to_dict()
        self.assertDictEqual(
            result,
            {
                "eff_date": date(2025, 10, 2).strftime("%Y-%m-%d"),
                "dp_computer_code": "ARSENAL",
                "dp_name": "ZDC",
                "artcc": "ARSNL5.CSN",
                "body_name": "SHRLI-CSN",
                "body_seq": "1",
                "arpt_id": "HEF",
                "rwy_end_id": "34L",
            },
        )

    def test_to_str(self):
        result = self.dp_apt.to_str()
        self.assertEqual(
            result,
            "eff_date: 2025-10-02, "
            "dp_computer_code: ARSENAL, "
            "dp_name: ZDC, "
            "artcc: ARSNL5.CSN, "
            "body_name: SHRLI-CSN, "
            "body_seq: 1, "
            "arpt_id: HEF, "
            "rwy_end_id: 34L",
        )
