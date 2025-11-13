from nasrparse.records.ils import ILS_DME
from nasrparse.records.types import (
    HemisCode,
    PositionSourceCode,
    SiteTypeCode,
    SystemTypeCode,
)

from datetime import date

import unittest


class TestILS_DME(unittest.TestCase):
    def setUp(self):
        self.maxDiff = None
        self.ils_dme = ILS_DME(
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
            "1901/01/01",
            "39",
            "4",
            "5.9776",
            "N",
            "39.06832711",
            "77",
            "33",
            "8.5167",
            "W",
            "-77.55236575",
            "T",
            "402.1",
            "54Y",
        )

    def tearDown(self):
        pass

    def test_repr(self):
        result = repr(self.ils_dme)
        self.assertEqual(
            result,
            "ILS_DME ( "
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
            "COMPONENT_STATUS_DATE=datetime.date(1901, 1, 1), "
            "LAT_DEG=39, "
            "LAT_MIN=4, "
            "LAT_SEC=5.9776, "
            f"LAT_HEMIS={HemisCode.NORTH!r}, "
            "LAT_DECIMAL=39.06832711, "
            "LON_DEG=77, "
            "LON_MIN=33, "
            "LON_SEC=8.5167, "
            f"LON_HEMIS={HemisCode.WEST!r}, "
            "LON_DECIMAL=-77.55236575, "
            f"LAT_LON_SOURCE_CODE={PositionSourceCode.THIRD_PARTY_SURVEY!r}, "
            "SITE_ELEVATION=402.1, "
            "CHANNEL='54Y'"
            " )",
        ),

    def test_ordered_fields(self):
        result = self.ils_dme.ordered_fields()
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
                "channel",
            ],
        )

    def test_to_dict(self):
        result = self.ils_dme.to_dict()
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
                "component_status_date": date(1901, 1, 1).strftime("%Y-%m-%d"),
                "lat_deg": 39,
                "lat_min": 4,
                "lat_sec": 5.9776,
                "lat_hemis": HemisCode.NORTH.value,
                "lat_decimal": 39.06832711,
                "lon_deg": 77,
                "lon_min": 33,
                "lon_sec": 8.5167,
                "lon_hemis": HemisCode.WEST.value,
                "lon_decimal": -77.55236575,
                "lat_lon_source_code": PositionSourceCode.THIRD_PARTY_SURVEY.value,
                "site_elevation": 402.1,
                "channel": "54Y",
            },
        )

    def test_to_str(self):
        result = self.ils_dme.to_str()
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
            "component_status_date: 1901-01-01, "
            "lat_deg: 39, "
            "lat_min: 4, "
            "lat_sec: 5.9776, "
            "lat_hemis: N, "
            "lat_decimal: 39.06832711, "
            "lon_deg: 77, "
            "lon_min: 33, "
            "lon_sec: 8.5167, "
            "lon_hemis: W, "
            "lon_decimal: -77.55236575, "
            "lat_lon_source_code: T, "
            "site_elevation: 402.1, "
            "channel: 54Y",
        )
