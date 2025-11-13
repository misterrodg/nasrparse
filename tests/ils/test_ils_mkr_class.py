from nasrparse.records.ils import ILS_MKR
from nasrparse.records.types import (
    HemisCode,
    ILSCompTypeCode,
    MarkerTypeCode,
    PositionSourceCode,
    SiteTypeCode,
    SystemTypeCode,
)

from datetime import date

import unittest


class TestILS_MKR(unittest.TestCase):
    def setUp(self):
        self.maxDiff = None
        self.ils_mkr = ILS_MKR(
            "2025/10/30",
            "25986.",
            "A",
            "VA",
            "ROA",
            "ROANOKE",
            "US",
            "06",
            "SZK",
            "DD",
            "OM",
            "OPERATIONAL IFR",
            "1977/10/06",
            "37",
            "17",
            "14.4138",
            "N",
            "37.28733716",
            "80",
            "4",
            "16.1148",
            "W",
            "-80.071143",
            "K",
            "1025.6",
            "M",
            "SZ",
            "SKIRT",
            "",
            "",
            "",
            "",
        )

    def tearDown(self):
        pass

    def test_repr(self):
        result = repr(self.ils_mkr)
        self.assertEqual(
            result,
            "ILS_MKR ( "
            "EFF_DATE=datetime.date(2025, 10, 30), "
            "SITE_NO='25986.', "
            f"SITE_TYPE_CODE={SiteTypeCode.AIRPORT!r}, "
            "STATE_CODE='VA', "
            "ARPT_ID='ROA', "
            "CITY='ROANOKE', "
            "COUNTRY_CODE='US', "
            "RWY_END_ID='06', "
            "ILS_LOC_ID='SZK', "
            f"SYSTEM_TYPE_CODE={SystemTypeCode.LDA_DME!r}, "
            f"ILS_COMP_TYPE_CODE={ILSCompTypeCode.OUTER_MARKER!r}, "
            "COMPONENT_STATUS='OPERATIONAL IFR', "
            "COMPONENT_STATUS_DATE=datetime.date(1977, 10, 6), "
            "LAT_DEG=37, "
            "LAT_MIN=17, "
            "LAT_SEC=14.4138, "
            f"LAT_HEMIS={HemisCode.NORTH!r}, "
            "LAT_DECIMAL=37.28733716, "
            "LON_DEG=80, "
            "LON_MIN=4, "
            "LON_SEC=16.1148, "
            f"LON_HEMIS={HemisCode.WEST!r}, "
            "LON_DECIMAL=-80.071143, "
            f"LAT_LON_SOURCE_CODE={PositionSourceCode.NGS!r}, "
            "SITE_ELEVATION=1025.6, "
            f"MKR_FAC_TYPE_CODE={MarkerTypeCode.MARKER_ONLY!r}, "
            "MARKER_ID_BEACON='SZ', "
            "COMPASS_LOCATOR_NAME='SKIRT', "
            "FREQ=None, "
            "NAV_ID=None, "
            "NAV_TYPE=None, "
            "LOW_POWERED_NDB_STATUS=None"
            " )",
        ),

    def test_ordered_fields(self):
        result = self.ils_mkr.ordered_fields()
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
                "ils_comp_type_code",
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
                "mkr_fac_type_code",
                "marker_id_beacon",
                "compass_locator_name",
                "freq",
                "nav_id",
                "nav_type",
                "low_powered_ndb_status",
            ],
        )

    def test_to_dict(self):
        result = self.ils_mkr.to_dict()
        self.assertDictEqual(
            result,
            {
                "eff_date": date(2025, 10, 30).strftime("%Y-%m-%d"),
                "site_no": "25986.",
                "site_type_code": SiteTypeCode.AIRPORT.value,
                "state_code": "VA",
                "arpt_id": "ROA",
                "city": "ROANOKE",
                "country_code": "US",
                "rwy_end_id": "06",
                "ils_loc_id": "SZK",
                "system_type_code": SystemTypeCode.LDA_DME.value,
                "ils_comp_type_code": ILSCompTypeCode.OUTER_MARKER.value,
                "component_status": "OPERATIONAL IFR",
                "component_status_date": date(1977, 10, 6).strftime("%Y-%m-%d"),
                "lat_deg": 37,
                "lat_min": 17,
                "lat_sec": 14.4138,
                "lat_hemis": HemisCode.NORTH.value,
                "lat_decimal": 37.28733716,
                "lon_deg": 80,
                "lon_min": 4,
                "lon_sec": 16.1148,
                "lon_hemis": HemisCode.WEST.value,
                "lon_decimal": -80.071143,
                "lat_lon_source_code": PositionSourceCode.NGS.value,
                "site_elevation": 1025.6,
                "mkr_fac_type_code": MarkerTypeCode.MARKER_ONLY.value,
                "marker_id_beacon": "SZ",
                "compass_locator_name": "SKIRT",
                "freq": None,
                "nav_id": None,
                "nav_type": None,
                "low_powered_ndb_status": None,
            },
        )

    def test_to_str(self):
        result = self.ils_mkr.to_str()
        self.assertEqual(
            result,
            "eff_date: 2025-10-30, "
            "site_no: 25986., "
            "site_type_code: A, "
            "state_code: VA, "
            "arpt_id: ROA, "
            "city: ROANOKE, "
            "country_code: US, "
            "rwy_end_id: 06, "
            "ils_loc_id: SZK, "
            "system_type_code: DD, "
            "ils_comp_type_code: OM, "
            "component_status: OPERATIONAL IFR, "
            "component_status_date: 1977-10-06, "
            "lat_deg: 37, "
            "lat_min: 17, "
            "lat_sec: 14.4138, "
            "lat_hemis: N, "
            "lat_decimal: 37.28733716, "
            "lon_deg: 80, "
            "lon_min: 4, "
            "lon_sec: 16.1148, "
            "lon_hemis: W, "
            "lon_decimal: -80.071143, "
            "lat_lon_source_code: K, "
            "site_elevation: 1025.6, "
            "mkr_fac_type_code: M, "
            "marker_id_beacon: SZ, "
            "compass_locator_name: SKIRT, "
            "freq: None, "
            "nav_id: None, "
            "nav_type: None, "
            "low_powered_ndb_status: None",
        )
