from nasrparse.records.hpf import HPF_BASE
from nasrparse.records.types import DirectionCode, PointCode

from datetime import date

import unittest


class TestHPF_BASE(unittest.TestCase):
    def setUp(self):
        self.maxDiff = None
        self.hpf_base = HPF_BASE(
            "2025/10/30",
            "HYPER INT*MD*K6",
            "1",
            "MD",
            "US",
            "HYPER",
            "K6",
            "MRB",
            "VORTAC",
            "NE",
            "65",
            "RAD",
            "245",
            "L",
            "",
        )

    def tearDown(self):
        pass

    def test_repr(self):
        result = repr(self.hpf_base)
        self.assertEqual(
            result,
            "HPF_BASE ( "
            "EFF_DATE=datetime.date(2025, 10, 30), "
            "HP_NAME='HYPER INT*MD*K6', "
            "HP_NO=1, "
            "STATE_CODE='MD', "
            "COUNTRY_CODE='US', "
            "FIX_ID='HYPER', "
            "ICAO_REGION_CODE='K6', "
            "NAV_ID='MRB', "
            f"NAV_TYPE={PointCode.VORTAC!r}, "
            f"HOLD_DIRECTION={DirectionCode.NORTH_EAST!r}, "
            "HOLD_DEG_OR_CRS='65', "
            "AZIMUTH='RAD', "
            "COURSE_INBOUND_DEG=245, "
            "TURN_DIRECTION='L', "
            "LEG_LENGTH_DIST=None"
            " )",
        ),

    def test_ordered_fields(self):
        result = self.hpf_base.ordered_fields()
        self.assertListEqual(
            result,
            [
                "eff_date",
                "hp_name",
                "hp_no",
                "state_code",
                "country_code",
                "fix_id",
                "icao_region_code",
                "nav_id",
                "nav_type",
                "hold_direction",
                "hold_deg_or_crs",
                "azimuth",
                "course_inbound_deg",
                "turn_direction",
                "leg_length_dist",
            ],
        )

    def test_to_dict(self):
        result = self.hpf_base.to_dict()
        self.assertDictEqual(
            result,
            {
                "eff_date": date(2025, 10, 30).strftime("%Y-%m-%d"),
                "hp_name": "HYPER INT*MD*K6",
                "hp_no": 1,
                "state_code": "MD",
                "country_code": "US",
                "fix_id": "HYPER",
                "icao_region_code": "K6",
                "nav_id": "MRB",
                "nav_type": PointCode.VORTAC.value,
                "hold_direction": DirectionCode.NORTH_EAST.value,
                "hold_deg_or_crs": "65",
                "azimuth": "RAD",
                "course_inbound_deg": 245,
                "turn_direction": "L",
                "leg_length_dist": None,
            },
        )

    def test_to_str(self):
        result = self.hpf_base.to_str()
        self.assertEqual(
            result,
            "eff_date: 2025-10-30, "
            "hp_name: HYPER INT*MD*K6, "
            "hp_no: 1, "
            "state_code: MD, "
            "country_code: US, "
            "fix_id: HYPER, "
            "icao_region_code: K6, "
            "nav_id: MRB, "
            "nav_type: VORTAC, "
            "hold_direction: NE, "
            "hold_deg_or_crs: 65, "
            "azimuth: RAD, "
            "course_inbound_deg: 245, "
            "turn_direction: L, "
            "leg_length_dist: None",
        )
