from nasrparse.records.maa import MAA_BASE
from nasrparse.records.types import DirectionCode, MAATypeCode, PointCode

from datetime import date

import unittest


class TestMAA_BASE(unittest.TestCase):
    def setUp(self):
        self.maxDiff = None
        self.maa_base = MAA_BASE(
            "2025/10/30",
            "SVA001",
            "SPACE LAUNCH",
            "",
            "",
            "",
            "",
            "VA",
            "",
            "37-51-02.1300N",
            "075-28-15.9300W",
            "",
            "WAL",
            "5",
            "S ",
            "MID-ATLANTIC REGIONAL SPACEPORT AT WALLOPS FLIGHT FACILITY",
            "",
            "",
            "",
            "SPACE LAUNCH AND REENTRY OPERATIONS ARE CONDUCTED AT VARIOUS TIMES WITHIN AREA. VERTICAL LAUNCH AND REENTRY ACTIVITIES ARE CONDUCTED FROM LAUNCH PADS LOCATED ABOUT 5 NM SOUTH OF KWAL AIRPORT.",
            "",
            "KZDC",
            "",
            "",
        )

    def tearDown(self):
        pass

    def test_repr(self):
        result = repr(self.maa_base)
        self.assertEqual(
            result,
            "MAA_BASE ( "
            "EFF_DATE=datetime.date(2025, 10, 30), "
            "MAA_ID='SVA001', "
            f"MAA_TYPE_NAME={MAATypeCode.SPACE_LAUNCH!r}, "
            "NAV_ID=None, "
            f"NAV_TYPE={PointCode.NULL!r}, "
            "NAV_RADIAL=None, "
            "NAV_DISTANCE=None, "
            "STATE_CODE='VA', "
            "CITY=None, "
            "LATITUDE=37.850591666666666, "
            "LONGITUDE=-75.47109166666667, "
            "ARPT_IDS=[], "
            "NEAREST_ARPT='WAL', "
            "NEAREST_ARPT_DIST=5.0, "
            f"NEAREST_ARPT_DIR={DirectionCode.SOUTH!r}, "
            "MAA_NAME='MID-ATLANTIC REGIONAL SPACEPORT AT WALLOPS FLIGHT FACILITY', "
            "MAX_ALT=None, "
            "MIN_ALT=None, "
            "MAA_RADIUS=None, "
            "DESCRIPTION='SPACE LAUNCH AND REENTRY OPERATIONS ARE CONDUCTED AT VARIOUS TIMES WITHIN AREA. VERTICAL LAUNCH AND REENTRY ACTIVITIES ARE CONDUCTED FROM LAUNCH PADS LOCATED ABOUT 5 NM SOUTH OF KWAL AIRPORT.', "
            "MAA_USE=None, "
            "CHECK_NOTAMS='KZDC', "
            "TIME_OF_USE=None, "
            "USER_GROUP_NAME=None"
            " )",
        ),

    def test_ordered_fields(self):
        result = self.maa_base.ordered_fields()
        self.assertListEqual(
            result,
            [
                "eff_date",
                "maa_id",
                "maa_type_name",
                "nav_id",
                "nav_type",
                "nav_radial",
                "nav_distance",
                "state_code",
                "city",
                "latitude",
                "longitude",
                "arpt_ids",
                "nearest_arpt",
                "nearest_arpt_dist",
                "nearest_arpt_dir",
                "maa_name",
                "max_alt",
                "min_alt",
                "maa_radius",
                "description",
                "maa_use",
                "check_notams",
                "time_of_use",
                "user_group_name",
            ],
        )

    def test_to_dict(self):
        result = self.maa_base.to_dict()
        self.assertDictEqual(
            result,
            {
                "eff_date": date(2025, 10, 30).strftime("%Y-%m-%d"),
                "maa_id": "SVA001",
                "maa_type_name": "SPACE LAUNCH",
                "nav_id": None,
                "nav_type": PointCode.NULL.value,
                "nav_radial": None,
                "nav_distance": None,
                "state_code": "VA",
                "city": None,
                "latitude": 37.850591666666666,
                "longitude": -75.47109166666667,
                "arpt_ids": None,
                "nearest_arpt": "WAL",
                "nearest_arpt_dist": 5.0,
                "nearest_arpt_dir": DirectionCode.SOUTH.value,
                "maa_name": "MID-ATLANTIC REGIONAL SPACEPORT AT WALLOPS FLIGHT FACILITY",
                "max_alt": None,
                "min_alt": None,
                "maa_radius": None,
                "description": "SPACE LAUNCH AND REENTRY OPERATIONS ARE CONDUCTED AT VARIOUS TIMES WITHIN AREA. VERTICAL LAUNCH AND REENTRY ACTIVITIES ARE CONDUCTED FROM LAUNCH PADS LOCATED ABOUT 5 NM SOUTH OF KWAL AIRPORT.",
                "maa_use": None,
                "check_notams": "KZDC",
                "time_of_use": None,
                "user_group_name": None,
            },
        )

    def test_to_str(self):
        result = self.maa_base.to_str()
        self.assertEqual(
            result,
            "eff_date: 2025-10-30, "
            "maa_id: SVA001, "
            "maa_type_name: SPACE LAUNCH, "
            "nav_id: None, "
            "nav_type: None, "
            "nav_radial: None, "
            "nav_distance: None, "
            "state_code: VA, "
            "city: None, "
            "latitude: 37.850591666666666, "
            "longitude: -75.47109166666667, "
            "arpt_ids: None, "
            "nearest_arpt: WAL, "
            "nearest_arpt_dist: 5.0, "
            "nearest_arpt_dir: S, "
            "maa_name: MID-ATLANTIC REGIONAL SPACEPORT AT WALLOPS FLIGHT FACILITY, "
            "max_alt: None, "
            "min_alt: None, "
            "maa_radius: None, "
            "description: SPACE LAUNCH AND REENTRY OPERATIONS ARE CONDUCTED AT VARIOUS TIMES WITHIN AREA. VERTICAL LAUNCH AND REENTRY ACTIVITIES ARE CONDUCTED FROM LAUNCH PADS LOCATED ABOUT 5 NM SOUTH OF KWAL AIRPORT., "
            "maa_use: None, "
            "check_notams: KZDC, "
            "time_of_use: None, "
            "user_group_name: None",
        )
