from nasrparse.records.dp import DP_RTE
from nasrparse.records.types import PointCode

from datetime import date

import unittest


class TestDP_RTE(unittest.TestCase):
    def setUp(self):
        self.maxDiff = None
        self.dp_rte = DP_RTE(
            "2025/10/02",
            "ARSENAL",
            "ZDC",
            "ARSNL5.CSN",
            "BODY",
            "SHRLI-CSN",
            "1",
            "",
            "10",
            "CSN",
            "",
            "VORTAC",
            "SHRLI",
            "HEF/34L, HEF/34R",
        )

    def tearDown(self):
        pass

    def test_repr(self):
        result = repr(self.dp_rte)
        self.assertEqual(
            result,
            "DP_RTE ( "
            "EFF_DATE=datetime.date(2025, 10, 2), "
            "DP_COMPUTER_CODE='ARSENAL', "
            "DP_NAME='ZDC', "
            "ARTCC='ARSNL5.CSN', "
            "ROUTE_PORTION_TYPE='BODY', "
            "ROUTE_NAME='SHRLI-CSN', "
            "BODY_SEQ='1', "
            "TRANSITION_COMPUTER_CODE=None, "
            "POINT_SEQ=10, "
            "POINT='CSN', "
            "ICAO_REGION_CODE=None, "
            f"POINT_TYPE={PointCode.VORTAC!r}, "
            "NEXT_POINT='SHRLI', "
            "ARPT_RWY_ASSOC='HEF/34L, HEF/34R'"
            " )",
        ),

    def test_ordered_fields(self):
        result = self.dp_rte.ordered_fields()
        self.assertListEqual(
            result,
            [
                "eff_date",
                "dp_computer_code",
                "dp_name",
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
        result = self.dp_rte.to_dict()
        self.assertDictEqual(
            result,
            {
                "eff_date": date(2025, 10, 2).strftime("%Y-%m-%d"),
                "dp_computer_code": "ARSENAL",
                "dp_name": "ZDC",
                "artcc": "ARSNL5.CSN",
                "route_portion_type": "BODY",
                "route_name": "SHRLI-CSN",
                "body_seq": "1",
                "transition_computer_code": None,
                "point_seq": 10,
                "point": "CSN",
                "icao_region_code": None,
                "point_type": PointCode.VORTAC.value,
                "next_point": "SHRLI",
                "arpt_rwy_assoc": "HEF/34L, HEF/34R",
            },
        )

    def test_to_str(self):
        result = self.dp_rte.to_str()
        self.assertEqual(
            result,
            "eff_date: 2025-10-02, "
            "dp_computer_code: ARSENAL, "
            "dp_name: ZDC, "
            "artcc: ARSNL5.CSN, "
            "route_portion_type: BODY, "
            "route_name: SHRLI-CSN, "
            "body_seq: 1, "
            "transition_computer_code: None, "
            "point_seq: 10, "
            "point: CSN, "
            "icao_region_code: None, "
            "point_type: VORTAC, "
            "next_point: SHRLI, "
            "arpt_rwy_assoc: HEF/34L, HEF/34R",
        )
