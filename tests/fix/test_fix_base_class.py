from nasrparse.records.fix import FIX_BASE
from nasrparse.records.types import HemisCode, PointCode

from datetime import date

import unittest


class TestFIX_BASE(unittest.TestCase):
    def setUp(self):
        self.maxDiff = None
        self.fix_base = FIX_BASE(
            "2025/10/30",
            "RUANE",
            "K6",
            "MD",
            "US",
            "39",
            "26",
            "46",
            "N",
            "39.44611111",
            "77",
            "22",
            "26.34",
            "W",
            "-77.37398333",
            "",
            "RNAV",
            "RP   ",
            "",
            "ZDC",
            "N",
            "N",
            "N",
            "",
            "",
            "CONTROLLER LOW,ENROUTE LOW,IAP,STAR",
        )

    def tearDown(self):
        pass

    def test_repr(self):
        result = repr(self.fix_base)
        self.assertEqual(
            result,
            "FIX_BASE ( "
            "EFF_DATE=datetime.date(2025, 10, 30), "
            "FIX_ID='RUANE', "
            "ICAO_REGION_CODE='K6', "
            "STATE_CODE='MD', "
            "COUNTRY_CODE='US', "
            "LAT_DEG=39, "
            "LAT_MIN=26, "
            "LAT_SEC=46.0, "
            f"LAT_HEMIS={HemisCode.NORTH!r}, "
            "LAT_DECIMAL=39.44611111, "
            "LON_DEG=77, "
            "LON_MIN=22, "
            "LON_SEC=26.34, "
            f"LON_HEMIS={HemisCode.WEST!r}, "
            "LON_DECIMAL=-77.37398333, "
            "FIX_ID_OLD=None, "
            "CHARTING_REMARK='RNAV', "
            f"FIX_USE_CODE={PointCode.REPORTING_POINT!r}, "
            "ARTCC_ID_HIGH=None, "
            "ARTCC_ID_LOW='ZDC', "
            "PITCH_FLAG=False, "
            "CATCH_FLAG=False, "
            "SUA_ATCAA_FLAG=False, "
            "MIN_RECEP_ALT=None, "
            "COMPULSORY=None, "
            "CHARTS='CONTROLLER LOW,ENROUTE LOW,IAP,STAR'"
            " )",
        ),

    def test_ordered_fields(self):
        result = self.fix_base.ordered_fields()
        self.assertListEqual(
            result,
            [
                "eff_date",
                "fix_id",
                "icao_region_code",
                "state_code",
                "country_code",
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
                "fix_id_old",
                "charting_remark",
                "fix_use_code",
                "artcc_id_high",
                "artcc_id_low",
                "pitch_flag",
                "catch_flag",
                "sua_atcaa_flag",
                "min_recep_alt",
                "compulsory",
                "charts",
            ],
        )

    def test_to_dict(self):
        result = self.fix_base.to_dict()
        self.assertDictEqual(
            result,
            {
                "eff_date": date(2025, 10, 30).strftime("%Y-%m-%d"),
                "fix_id": "RUANE",
                "icao_region_code": "K6",
                "state_code": "MD",
                "country_code": "US",
                "lat_deg": 39,
                "lat_min": 26,
                "lat_sec": 46.0,
                "lat_hemis": HemisCode.NORTH.value,
                "lat_decimal": 39.44611111,
                "lon_deg": 77,
                "lon_min": 22,
                "lon_sec": 26.34,
                "lon_hemis": HemisCode.WEST.value,
                "lon_decimal": -77.37398333,
                "fix_id_old": None,
                "charting_remark": "RNAV",
                "fix_use_code": PointCode.REPORTING_POINT.value,
                "artcc_id_high": None,
                "artcc_id_low": "ZDC",
                "pitch_flag": False,
                "catch_flag": False,
                "sua_atcaa_flag": False,
                "min_recep_alt": None,
                "compulsory": None,
                "charts": "CONTROLLER LOW,ENROUTE LOW,IAP,STAR",
            },
        )

    def test_to_str(self):
        result = self.fix_base.to_str()
        self.assertEqual(
            result,
            "eff_date: 2025-10-30, "
            "fix_id: RUANE, "
            "icao_region_code: K6, "
            "state_code: MD, "
            "country_code: US, "
            "lat_deg: 39, "
            "lat_min: 26, "
            "lat_sec: 46.0, "
            "lat_hemis: N, "
            "lat_decimal: 39.44611111, "
            "lon_deg: 77, "
            "lon_min: 22, "
            "lon_sec: 26.34, "
            "lon_hemis: W, "
            "lon_decimal: -77.37398333, "
            "fix_id_old: None, "
            "charting_remark: RNAV, "
            "fix_use_code: RP, "
            "artcc_id_high: None, "
            "artcc_id_low: ZDC, "
            "pitch_flag: False, "
            "catch_flag: False, "
            "sua_atcaa_flag: False, "
            "min_recep_alt: None, "
            "compulsory: None, "
            "charts: CONTROLLER LOW,ENROUTE LOW,IAP,STAR",
        )
