from nasrparse.records.ils import ILS_BASE
from nasrparse.records.types import (
    BackCourseStatusCode,
    HemisCode,
    RegionCode,
    PositionSourceCode,
    SiteTypeCode,
    SystemTypeCode,
)

from datetime import date

import unittest


class TestILS_BASE(unittest.TestCase):
    def setUp(self):
        self.maxDiff = None
        self.ils_base = ILS_BASE(
            "2025/10/30",
            "25863.",
            "A",
            "VA",
            "LYH",
            "LYNCHBURG",
            "US",
            "04",
            "LYH",
            "LS",
            "VIRGINIA",
            "AEA",
            "7100",
            "150",
            "I",
            "F-FEDERAL AVIATION ADMIN.",
            "F-FEDERAL AVIATION ADMIN",
            "35.8",
            "8",
            "W",
            "OPERATIONAL IFR",
            "1964/01/17",
            "37",
            "20",
            "2.1105",
            "N",
            "37.33391958",
            "79",
            "11",
            "43.0368",
            "W",
            "-79.195288",
            "T",
            "934.1",
            "110.1",
            "U",
        )

    def tearDown(self):
        pass

    def test_repr(self):
        result = repr(self.ils_base)
        self.assertEqual(
            result,
            "ILS_BASE ( "
            "EFF_DATE=datetime.date(2025, 10, 30), "
            "SITE_NO='25863.', "
            f"SITE_TYPE_CODE={SiteTypeCode.AIRPORT!r}, "
            "STATE_CODE='VA', "
            "ARPT_ID='LYH', "
            "CITY='LYNCHBURG', "
            "COUNTRY_CODE='US', "
            "RWY_END_ID='04', "
            "ILS_LOC_ID='LYH', "
            f"SYSTEM_TYPE_CODE={SystemTypeCode.ILS!r}, "
            "STATE_NAME='VIRGINIA', "
            f"REGION_CODE={RegionCode.EASTERN!r}, "
            "RWY_LEN=7100, "
            "RWY_WIDTH=150, "
            "CATEGORY='I', "
            "OWNER='F-FEDERAL AVIATION ADMIN.', "
            "OPERATOR='F-FEDERAL AVIATION ADMIN', "
            "APCH_BEAR=35.8, "
            "MAG_VAR=8, "
            f"MAG_VAR_HEMIS={HemisCode.WEST!r}, "
            "COMPONENT_STATUS='OPERATIONAL IFR', "
            "COMPONENT_STATUS_DATE=datetime.date(1964, 1, 17), "
            "LAT_DEG=37, "
            "LAT_MIN=20, "
            "LAT_SEC=2.1105, "
            f"LAT_HEMIS={HemisCode.NORTH!r}, "
            "LAT_DECIMAL=37.33391958, "
            "LON_DEG=79, "
            "LON_MIN=11, "
            "LON_SEC=43.0368, "
            f"LON_HEMIS={HemisCode.WEST!r}, "
            "LON_DECIMAL=-79.195288, "
            f"LAT_LON_SOURCE_CODE={PositionSourceCode.THIRD_PARTY_SURVEY!r}, "
            "SITE_ELEVATION=934.1, "
            "LOC_FREQ='110.1', "
            f"BK_COURSE_STATUS_CODE={BackCourseStatusCode.UNUSABLE!r}"
            " )",
        ),

    def test_ordered_fields(self):
        result = self.ils_base.ordered_fields()
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
                "state_name",
                "region_code",
                "rwy_len",
                "rwy_width",
                "category",
                "owner",
                "operator",
                "apch_bear",
                "mag_var",
                "mag_var_hemis",
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
                "loc_freq",
                "bk_course_status_code",
            ],
        )

    def test_to_dict(self):
        result = self.ils_base.to_dict()
        self.assertDictEqual(
            result,
            {
                "eff_date": date(2025, 10, 30).strftime("%Y-%m-%d"),
                "site_no": "25863.",
                "site_type_code": SiteTypeCode.AIRPORT.value,
                "state_code": "VA",
                "arpt_id": "LYH",
                "city": "LYNCHBURG",
                "country_code": "US",
                "rwy_end_id": "04",
                "ils_loc_id": "LYH",
                "system_type_code": SystemTypeCode.ILS.value,
                "state_name": "VIRGINIA",
                "region_code": RegionCode.EASTERN.value,
                "rwy_len": 7100,
                "rwy_width": 150,
                "category": "I",
                "owner": "F-FEDERAL AVIATION ADMIN.",
                "operator": "F-FEDERAL AVIATION ADMIN",
                "apch_bear": 35.8,
                "mag_var": 8,
                "mag_var_hemis": HemisCode.WEST.value,
                "component_status": "OPERATIONAL IFR",
                "component_status_date": date(1964, 1, 17).strftime("%Y-%m-%d"),
                "lat_deg": 37,
                "lat_min": 20,
                "lat_sec": 2.1105,
                "lat_hemis": HemisCode.NORTH.value,
                "lat_decimal": 37.33391958,
                "lon_deg": 79,
                "lon_min": 11,
                "lon_sec": 43.0368,
                "lon_hemis": HemisCode.WEST.value,
                "lon_decimal": -79.195288,
                "lat_lon_source_code": PositionSourceCode.THIRD_PARTY_SURVEY.value,
                "site_elevation": 934.1,
                "loc_freq": "110.1",
                "bk_course_status_code": BackCourseStatusCode.UNUSABLE.value,
            },
        )

    def test_to_str(self):
        result = self.ils_base.to_str()
        self.assertEqual(
            result,
            "eff_date: 2025-10-30, "
            "site_no: 25863., "
            "site_type_code: A, "
            "state_code: VA, "
            "arpt_id: LYH, "
            "city: LYNCHBURG, "
            "country_code: US, "
            "rwy_end_id: 04, "
            "ils_loc_id: LYH, "
            "system_type_code: LS, "
            "state_name: VIRGINIA, "
            "region_code: AEA, "
            "rwy_len: 7100, "
            "rwy_width: 150, "
            "category: I, "
            "owner: F-FEDERAL AVIATION ADMIN., "
            "operator: F-FEDERAL AVIATION ADMIN, "
            "apch_bear: 35.8, "
            "mag_var: 8, "
            "mag_var_hemis: W, "
            "component_status: OPERATIONAL IFR, "
            "component_status_date: 1964-01-17, "
            "lat_deg: 37, "
            "lat_min: 20, "
            "lat_sec: 2.1105, "
            "lat_hemis: N, "
            "lat_decimal: 37.33391958, "
            "lon_deg: 79, "
            "lon_min: 11, "
            "lon_sec: 43.0368, "
            "lon_hemis: W, "
            "lon_decimal: -79.195288, "
            "lat_lon_source_code: T, "
            "site_elevation: 934.1, "
            "loc_freq: 110.1, "
            "bk_course_status_code: U",
        )
