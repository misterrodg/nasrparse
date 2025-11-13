from nasrparse.records.fss import FSS_BASE
from nasrparse.records.types import FSSTypeCode, HemisCode

from datetime import date

import unittest


class TestFSS_BASE(unittest.TestCase):
    def setUp(self):
        self.maxDiff = None
        self.fss_base = FSS_BASE(
            "2025/10/30",
            "DCA",
            "LEESBURG",
            "WASHINGTON",
            "DC",
            "US",
            "2023/04/17",
            "HUB",
            "LEESBURG",
            "39",
            "0",
            "13.75",
            "N",
            "39.00381944",
            "77",
            "29",
            "13.84",
            "W",
            "-77.48717777",
            "24",
            "A",
            "",
            "N",
            "",
            "1-800-WX-BRIEF",
        )

    def tearDown(self):
        pass

    def test_repr(self):
        result = repr(self.fss_base)
        self.assertEqual(
            result,
            "FSS_BASE ( "
            "EFF_DATE=datetime.date(2025, 10, 30), "
            "FSS_ID='DCA', "
            "NAME='LEESBURG', "
            "CITY='WASHINGTON', "
            "STATE_CODE='DC', "
            "COUNTRY_CODE='US', "
            "UPDATE_DATE=datetime.date(2023, 4, 17), "
            f"FSS_FAC_TYPE={FSSTypeCode.FS21_HUB!r}, "
            "VOICE_CALL='LEESBURG', "
            "LAT_DEG=39, "
            "LAT_MIN=0, "
            "LAT_SEC=13.75, "
            f"LAT_HEMIS={HemisCode.NORTH!r}, "
            "LAT_DECIMAL=39.00381944, "
            "LON_DEG=77, "
            "LON_MIN=29, "
            "LON_SEC=13.84, "
            f"LON_HEMIS={HemisCode.WEST!r}, "
            "LON_DECIMAL=-77.48717777, "
            "OPR_HOURS='24', "
            "FAC_STATUS='A', "
            "ALTERNATE_FSS=None, "
            "WEA_RADAR_FLAG=False, "
            "PHONE_NO=None, "
            "TOLL_FREE_NO='1-800-WX-BRIEF'"
            " )",
        ),

    def test_ordered_fields(self):
        result = self.fss_base.ordered_fields()
        self.assertListEqual(
            result,
            [
                "eff_date",
                "fss_id",
                "name",
                "city",
                "state_code",
                "country_code",
                "update_date",
                "fss_fac_type",
                "voice_call",
                "lat_deg",
                "lat_min",
                "lat_sec",
                "lat_hemis",
                "lat_decimal",
                "lon_deg",
                "lon_min",
                "lon_sec",
                "lon_hemis",
                "lon_decimal",
                "opr_hours",
                "fac_status",
                "alternate_fss",
                "wea_radar_flag",
                "phone_no",
                "toll_free_no",
            ],
        )

    def test_to_dict(self):
        result = self.fss_base.to_dict()
        self.assertDictEqual(
            result,
            {
                "eff_date": date(2025, 10, 30).strftime("%Y-%m-%d"),
                "fss_id": "DCA",
                "name": "LEESBURG",
                "city": "WASHINGTON",
                "state_code": "DC",
                "country_code": "US",
                "update_date": date(2023, 4, 17).strftime("%Y-%m-%d"),
                "fss_fac_type": FSSTypeCode.FS21_HUB.value,
                "voice_call": "LEESBURG",
                "lat_deg": 39,
                "lat_min": 0,
                "lat_sec": 13.75,
                "lat_hemis": HemisCode.NORTH.value,
                "lat_decimal": 39.00381944,
                "lon_deg": 77,
                "lon_min": 29,
                "lon_sec": 13.84,
                "lon_hemis": HemisCode.WEST.value,
                "lon_decimal": -77.48717777,
                "opr_hours": "24",
                "fac_status": "A",
                "alternate_fss": None,
                "wea_radar_flag": False,
                "phone_no": None,
                "toll_free_no": "1-800-WX-BRIEF",
            },
        )

    def test_to_str(self):
        result = self.fss_base.to_str()
        self.assertEqual(
            result,
            "eff_date: 2025-10-30, "
            "fss_id: DCA, "
            "name: LEESBURG, "
            "city: WASHINGTON, "
            "state_code: DC, "
            "country_code: US, "
            "update_date: 2023-04-17, "
            "fss_fac_type: HUB, "
            "voice_call: LEESBURG, "
            "lat_deg: 39, "
            "lat_min: 0, "
            "lat_sec: 13.75, "
            "lat_hemis: N, "
            "lat_decimal: 39.00381944, "
            "lon_deg: 77, "
            "lon_min: 29, "
            "lon_sec: 13.84, "
            "lon_hemis: W, "
            "lon_decimal: -77.48717777, "
            "opr_hours: 24, "
            "fac_status: A, "
            "alternate_fss: None, "
            "wea_radar_flag: False, "
            "phone_no: None, "
            "toll_free_no: 1-800-WX-BRIEF",
        )
