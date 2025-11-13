from nasrparse.records.star import STAR_APT

from datetime import date

import unittest


class TestSTAR_APT(unittest.TestCase):
    def setUp(self):
        self.maxDiff = None
        self.star_apt = STAR_APT(
            "2025/10/02",
            "ALWYZ.FRDMM6",
            "ZDC",
            "ALWYZ-FERGI",
            "1",
            "DCA",
            "19",
        )

    def tearDown(self):
        pass

    def test_repr(self):
        result = repr(self.star_apt)
        self.assertEqual(
            result,
            "STAR_APT ( "
            "EFF_DATE=datetime.date(2025, 10, 2), "
            "STAR_COMPUTER_CODE='ALWYZ.FRDMM6', "
            "ARTCC='ZDC', "
            "BODY_NAME='ALWYZ-FERGI', "
            "BODY_SEQ=1, "
            "ARPT_ID='DCA', "
            "RWY_END_ID='19'"
            " )",
        ),

    def test_ordered_fields(self):
        result = self.star_apt.ordered_fields()
        self.assertListEqual(
            result,
            [
                "eff_date",
                "star_computer_code",
                "artcc",
                "body_name",
                "body_seq",
                "arpt_id",
                "rwy_end_id",
            ],
        )

    def test_to_dict(self):
        result = self.star_apt.to_dict()
        self.assertDictEqual(
            result,
            {
                "eff_date": date(2025, 10, 2).strftime("%Y-%m-%d"),
                "star_computer_code": "ALWYZ.FRDMM6",
                "artcc": "ZDC",
                "body_name": "ALWYZ-FERGI",
                "body_seq": 1,
                "arpt_id": "DCA",
                "rwy_end_id": "19",
            },
        )

    def test_to_str(self):
        result = self.star_apt.to_str()
        self.assertEqual(
            result,
            "eff_date: 2025-10-02, "
            "star_computer_code: ALWYZ.FRDMM6, "
            "artcc: ZDC, "
            "body_name: ALWYZ-FERGI, "
            "body_seq: 1, "
            "arpt_id: DCA, "
            "rwy_end_id: 19",
        )
