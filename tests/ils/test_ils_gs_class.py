from nasrparse.records.ils import ILS_GS
from nasrparse.records.types import (
    GSTypeCode,
    HemisCode,
    PositionSourceCode,
    SiteTypeCode,
    SystemTypeCode,
)

from datetime import date

import unittest


class TestILS_GS(unittest.TestCase):
    def setUp(self):
        self.maxDiff = None
        self.ils_gs = ILS_GS(
            "2025/10/30",
            "25847.1",
            "A",
            "VA",
            "JYO",
            "LEESBURG",
            "US",
            "17",
            "JYO",
            "LD",
            "OPERATIONAL IFR",
            "2011/02/09",
            "39",
            "4",
            "57.5516",
            "N",
            "39.08265322",
            "77",
            "33",
            "37.8036",
            "W",
            "-77.560501",
            "T",
            "372.1",
            "GD",
            "3",
            "333.35",
        )

    def tearDown(self):
        pass

    def test_repr(self):
        result = repr(self.ils_gs)
        self.assertEqual(
            result,
            "ILS_GS ( "
            "EFF_DATE=datetime.date(2025, 10, 30), "
            "SITE_NO='25847.1', "
            f"SITE_TYPE_CODE={SiteTypeCode.AIRPORT!r}, "
            "STATE_CODE='VA', "
            "ARPT_ID='JYO', "
            "CITY='LEESBURG', "
            "COUNTRY_CODE='US', "
            "RWY_END_ID='17', "
            "ILS_LOC_ID='JYO', "
            f"SYSTEM_TYPE_CODE={SystemTypeCode.ILS_DME!r}, "
            "COMPONENT_STATUS='OPERATIONAL IFR', "
            "COMPONENT_STATUS_DATE=datetime.date(2011, 2, 9), "
            "LAT_DEG=39, "
            "LAT_MIN=4, "
            "LAT_SEC=57.5516, "
            f"LAT_HEMIS={HemisCode.NORTH!r}, "
            "LAT_DECIMAL=39.08265322, "
            "LON_DEG=77, "
            "LON_MIN=33, "
            "LON_SEC=37.8036, "
            f"LON_HEMIS={HemisCode.WEST!r}, "
            "LON_DECIMAL=-77.560501, "
            f"LAT_LON_SOURCE_CODE={PositionSourceCode.THIRD_PARTY_SURVEY!r}, "
            "SITE_ELEVATION=372.1, "
            f"G_S_TYPE_CODE={GSTypeCode.GLIDE_SLOPE_DME!r}, "
            "G_S_ANGLE=3.0, "
            "G_S_FREQ='333.35'"
            " )",
        ),

    def test_ordered_fields(self):
        result = self.ils_gs.ordered_fields()
        self.assertListEqual(
            result,
            [
                "eff_date",
                "site_no",
                "site_type_code",
                "state_code",
                "arpt_id",
                "city",
                "country_code",
                "rwy_end_id",
                "ils_loc_id",
                "system_type_code",
                "component_status",
                "component_status_date",
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
                "lat_lon_source_code",
                "site_elevation",
                "g_s_type_code",
                "g_s_angle",
                "g_s_freq",
            ],
        )

    def test_to_dict(self):
        result = self.ils_gs.to_dict()
        self.assertDictEqual(
            result,
            {
                "eff_date": date(2025, 10, 30).strftime("%Y-%m-%d"),
                "site_no": "25847.1",
                "site_type_code": SiteTypeCode.AIRPORT.value,
                "state_code": "VA",
                "arpt_id": "JYO",
                "city": "LEESBURG",
                "country_code": "US",
                "rwy_end_id": "17",
                "ils_loc_id": "JYO",
                "system_type_code": SystemTypeCode.ILS_DME.value,
                "component_status": "OPERATIONAL IFR",
                "component_status_date": date(2011, 2, 9).strftime("%Y-%m-%d"),
                "lat_deg": 39,
                "lat_min": 4,
                "lat_sec": 57.5516,
                "lat_hemis": HemisCode.NORTH.value,
                "lat_decimal": 39.08265322,
                "lon_deg": 77,
                "lon_min": 33,
                "lon_sec": 37.8036,
                "lon_hemis": HemisCode.WEST.value,
                "lon_decimal": -77.560501,
                "lat_lon_source_code": PositionSourceCode.THIRD_PARTY_SURVEY.value,
                "site_elevation": 372.1,
                "g_s_type_code": GSTypeCode.GLIDE_SLOPE_DME.value,
                "g_s_angle": 3.0,
                "g_s_freq": "333.35",
            },
        )

    def test_to_str(self):
        result = self.ils_gs.to_str()
        self.assertEqual(
            result,
            "eff_date: 2025-10-30, "
            "site_no: 25847.1, "
            "site_type_code: A, "
            "state_code: VA, "
            "arpt_id: JYO, "
            "city: LEESBURG, "
            "country_code: US, "
            "rwy_end_id: 17, "
            "ils_loc_id: JYO, "
            "system_type_code: LD, "
            "component_status: OPERATIONAL IFR, "
            "component_status_date: 2011-02-09, "
            "lat_deg: 39, "
            "lat_min: 4, "
            "lat_sec: 57.5516, "
            "lat_hemis: N, "
            "lat_decimal: 39.08265322, "
            "lon_deg: 77, "
            "lon_min: 33, "
            "lon_sec: 37.8036, "
            "lon_hemis: W, "
            "lon_decimal: -77.560501, "
            "lat_lon_source_code: T, "
            "site_elevation: 372.1, "
            "g_s_type_code: GD, "
            "g_s_angle: 3.0, "
            "g_s_freq: 333.35",
        )
