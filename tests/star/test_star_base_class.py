from nasrparse.records.star import STAR_BASE

from datetime import date

import unittest


class TestSTAR_BASE(unittest.TestCase):
    def setUp(self):
        self.maxDiff = None
        self.star_base = STAR_BASE(
            "2025/10/02",
            "ALWYZ.FRDMM6",
            "ZDC",
            "FRDMM",
            "SIX",
            "2024/05/16",
            "Y",
            "ADW DAA DCA",
        )

    def tearDown(self):
        pass

    def test_repr(self):
        result = repr(self.star_base)
        self.assertEqual(
            result,
            "STAR_BASE ( "
            "EFF_DATE=datetime.date(2025, 10, 2), "
            "STAR_COMPUTER_CODE='ALWYZ.FRDMM6', "
            "ARTCC='ZDC', "
            "ARRIVAL_NAME='FRDMM', "
            "AMENDMENT_NO='SIX', "
            "STAR_AMEND_EFF_DATE=datetime.date(2024, 5, 16), "
            "RNAV_FLAG=True, "
            "SERVED_ARPT='ADW DAA DCA'"
            " )",
        ),

    def test_ordered_fields(self):
        result = self.star_base.ordered_fields()
        self.assertListEqual(
            result,
            [
                "eff_date",
                "star_computer_code",
                "artcc",
                "arrival_name",
                "amendment_no",
                "star_amend_eff_date",
                "rnav_flag",
                "served_arpt",
            ],
        )

    def test_to_dict(self):
        result = self.star_base.to_dict()
        self.assertDictEqual(
            result,
            {
                "eff_date": date(2025, 10, 2).strftime("%Y-%m-%d"),
                "star_computer_code": "ALWYZ.FRDMM6",
                "artcc": "ZDC",
                "arrival_name": "FRDMM",
                "amendment_no": "SIX",
                "star_amend_eff_date": date(2024, 5, 16).strftime("%Y-%m-%d"),
                "rnav_flag": True,
                "served_arpt": "ADW DAA DCA",
            },
        )

    def test_to_str(self):
        result = self.star_base.to_str()
        self.assertEqual(
            result,
            "eff_date: 2025-10-02, "
            "star_computer_code: ALWYZ.FRDMM6, "
            "artcc: ZDC, "
            "arrival_name: FRDMM, "
            "amendment_no: SIX, "
            "star_amend_eff_date: 2024-05-16, "
            "rnav_flag: True, "
            "served_arpt: ADW DAA DCA",
        )
