from nasrparse.records.nav import NAV_CKPT
from nasrparse.records.types import (
    AirGroundCode,
    PointCode,
)

from datetime import date

import unittest


class TestNAV_CKPT(unittest.TestCase):
    def setUp(self):
        self.maxDiff = None
        self.nav_ckpt = NAV_CKPT(
            "2025/10/30",
            "SBY",
            "VORTAC",
            "MD",
            "SALISBURY",
            "US",
            "",
            "221",
            "G",
            "0.7 NM RUNUP PAD RY 5.",
            "SBY",
            "MD",
        )

    def tearDown(self):
        pass

    def test_repr(self):
        result = repr(self.nav_ckpt)
        self.assertEqual(
            result,
            "NAV_CKPT ( "
            "EFF_DATE=datetime.date(2025, 10, 30), "
            "NAV_ID='SBY', "
            f"NAV_TYPE={PointCode.VORTAC!r}, "
            "STATE_CODE='MD', "
            "CITY='SALISBURY', "
            "COUNTRY_CODE='US', "
            "ALTITUDE=None, "
            "BRG=221, "
            f"AIR_GND_CODE={AirGroundCode.GROUND!r}, "
            "CHK_DESC='0.7 NM RUNUP PAD RY 5.', "
            "ARPT_ID='SBY', "
            "STATE_CHK_CODE='MD'"
            " )",
        ),

    def test_ordered_fields(self):
        result = self.nav_ckpt.ordered_fields()
        self.assertListEqual(
            result,
            [
                "eff_date",
                "nav_id",
                "nav_type",
                "state_code",
                "city",
                "country_code",
                "altitude",
                "brg",
                "air_gnd_code",
                "chk_desc",
                "arpt_id",
                "state_chk_code",
            ],
        )

    def test_to_dict(self):
        result = self.nav_ckpt.to_dict()
        self.assertDictEqual(
            result,
            {
                "eff_date": date(2025, 10, 30).strftime("%Y-%m-%d"),
                "nav_id": "SBY",
                "nav_type": PointCode.VORTAC.value,
                "state_code": "MD",
                "city": "SALISBURY",
                "country_code": "US",
                "altitude": None,
                "brg": 221,
                "air_gnd_code": AirGroundCode.GROUND.value,
                "chk_desc": "0.7 NM RUNUP PAD RY 5.",
                "arpt_id": "SBY",
                "state_chk_code": "MD",
            },
        )

    def test_to_str(self):
        result = self.nav_ckpt.to_str()
        self.assertEqual(
            result,
            "eff_date: 2025-10-30, "
            "nav_id: SBY, "
            "nav_type: VORTAC, "
            "state_code: MD, "
            "city: SALISBURY, "
            "country_code: US, "
            "altitude: None, "
            "brg: 221, "
            "air_gnd_code: G, "
            "chk_desc: 0.7 NM RUNUP PAD RY 5., "
            "arpt_id: SBY, "
            "state_chk_code: MD",
        )
