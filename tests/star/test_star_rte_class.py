from nasrparse.records.star import STAR_RTE
from nasrparse.records.types import PointCode

from datetime import date

import unittest


class TestSTAR_RTE(unittest.TestCase):
    def setUp(self):
        self.maxDiff = None
        self.star_rte = STAR_RTE(
            "2025/10/02",
            "ALWYZ.FRDMM6",
            "ZDC",
            "BODY",
            "ALWYZ-FERGI",
            "1",
            "",
            "10",
            "FERGI",
            "K6",
            "RP   ",
            "TGTHR",
            "DCA/15, DCA/19, DCA/22",
        )

    def tearDown(self):
        pass

    def test_repr(self):
        result = repr(self.star_rte)
        self.assertEqual(
            result,
            "STAR_RTE ( "
            "EFF_DATE=datetime.date(2025, 10, 2), "
            "STAR_COMPUTER_CODE='ALWYZ.FRDMM6', "
            "ARTCC='ZDC', "
            "ROUTE_PORTION_TYPE='BODY', "
            "ROUTE_NAME='ALWYZ-FERGI', "
            "BODY_SEQ=1, "
            "TRANSITION_COMPUTER_CODE=None, "
            "POINT_SEQ=10, "
            "POINT='FERGI', "
            "ICAO_REGION_CODE='K6', "
            f"POINT_TYPE={PointCode.REPORTING_POINT!r}, "
            "NEXT_POINT='TGTHR', "
            "ARPT_RWY_ASSOC='DCA/15, DCA/19, DCA/22'"
            " )",
        ),

    def test_ordered_fields(self):
        result = self.star_rte.ordered_fields()
        self.assertListEqual(
            result,
            [
                "eff_date",
                "star_computer_code",
                "artcc",
                "route_portion_type",
                "route_name",
                "body_seq",
                "transition_computer_code",
                "point_seq",
                "point",
                "icao_region_code",
                "point_type",
                "next_point",
                "arpt_rwy_assoc",
            ],
        )

    def test_to_dict(self):
        result = self.star_rte.to_dict()
        self.assertDictEqual(
            result,
            {
                "eff_date": date(2025, 10, 2).strftime("%Y-%m-%d"),
                "star_computer_code": "ALWYZ.FRDMM6",
                "artcc": "ZDC",
                "route_portion_type": "BODY",
                "route_name": "ALWYZ-FERGI",
                "body_seq": 1,
                "transition_computer_code": None,
                "point_seq": 10,
                "point": "FERGI",
                "icao_region_code": "K6",
                "point_type": PointCode.REPORTING_POINT.value,
                "next_point": "TGTHR",
                "arpt_rwy_assoc": "DCA/15, DCA/19, DCA/22",
            },
        )

    def test_to_str(self):
        result = self.star_rte.to_str()
        self.assertEqual(
            result,
            "eff_date: 2025-10-02, "
            "star_computer_code: ALWYZ.FRDMM6, "
            "artcc: ZDC, "
            "route_portion_type: BODY, "
            "route_name: ALWYZ-FERGI, "
            "body_seq: 1, "
            "transition_computer_code: None, "
            "point_seq: 10, "
            "point: FERGI, "
            "icao_region_code: K6, "
            "point_type: RP, "
            "next_point: TGTHR, "
            "arpt_rwy_assoc: DCA/15, DCA/19, DCA/22",
        )
