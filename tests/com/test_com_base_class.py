from nasrparse.records.com import COM_BASE
from nasrparse.records.types import (
    CommunicationOutletCode,
    CommunicationStatusCode,
    HemisCode,
    PointCode,
    RegionCode,
)

from datetime import date

import unittest


class TestCOM_BASE(unittest.TestCase):
    def setUp(self):
        self.maxDiff = None
        self.com_base = COM_BASE(
            "2025/10/30",
            "",
            "RCAG",
            "",
            "",
            "",
            "VA",
            "AEA",
            "US",
            "BUENA VISTA",
            "37",
            "48",
            "0.48",
            "N",
            "37.80013333",
            "79",
            "10",
            "59.1",
            "W",
            "-79.18308333",
            "ZDC",
            "WASHINGTON",
            "",
            "",
            "",
            "",
            "",
            "",
        )

    def tearDown(self):
        pass

    def test_repr(self):
        result = repr(self.com_base)
        self.assertEqual(
            result,
            "COM_BASE ( "
            "EFF_DATE=datetime.date(2025, 10, 30), "
            "COMM_LOC_ID=None, "
            f"COMM_TYPE={CommunicationOutletCode.RCAG!r}, "
            "NAV_ID=None, "
            f"NAV_TYPE={PointCode.NULL!r}, "
            "CITY=None, "
            "STATE_CODE='VA', "
            f"REGION_CODE={RegionCode.EASTERN!r}, "
            "COUNTRY_CODE='US', "
            "COMM_OUTLET_NAME='BUENA VISTA', "
            "LAT_DEG=37, "
            "LAT_MIN=48, "
            "LAT_SEC=0.48, "
            f"LAT_HEMIS={HemisCode.NORTH!r}, "
            "LAT_DECIMAL=37.80013333, "
            "LON_DEG=79, "
            "LON_MIN=10, "
            "LON_SEC=59.1, "
            f"LON_HEMIS={HemisCode.WEST!r}, "
            "LON_DECIMAL=-79.18308333, "
            "FACILITY_ID='ZDC', "
            "FACILITY_NAME='WASHINGTON', "
            "ALT_FSS_ID=None, "
            "ALT_FSS_NAME=None, "
            "OPR_HRS=None, "
            f"COMM_STATUS_CODE={CommunicationStatusCode.NULL!r}, "
            "COMM_STATUS_DATE=None, "
            "REMARK=None"
            " )",
        ),

    def test_ordered_fields(self):
        result = self.com_base.ordered_fields()
        self.assertListEqual(
            result,
            [
                "eff_date",
                "comm_loc_id",
                "comm_type",
                "nav_id",
                "nav_type",
                "city",
                "state_code",
                "region_code",
                "country_code",
                "comm_outlet_name",
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
                "facility_id",
                "facility_name",
                "alt_fss_id",
                "alt_fss_name",
                "opr_hrs",
                "comm_status_code",
                "comm_status_date",
                "remark",
            ],
        )

    def test_to_dict(self):
        result = self.com_base.to_dict()
        self.assertDictEqual(
            result,
            {
                "eff_date": date(2025, 10, 30).strftime("%Y-%m-%d"),
                "comm_loc_id": None,
                "comm_type": CommunicationOutletCode.RCAG.value,
                "nav_id": None,
                "nav_type": PointCode.NULL.value,
                "city": None,
                "state_code": "VA",
                "region_code": RegionCode.EASTERN.value,
                "country_code": "US",
                "comm_outlet_name": "BUENA VISTA",
                "lat_deg": 37,
                "lat_min": 48,
                "lat_sec": 0.48,
                "lat_hemis": HemisCode.NORTH.value,
                "lat_decimal": 37.80013333,
                "lon_deg": 79,
                "lon_min": 10,
                "lon_sec": 59.1,
                "lon_hemis": HemisCode.WEST.value,
                "lon_decimal": -79.18308333,
                "facility_id": "ZDC",
                "facility_name": "WASHINGTON",
                "alt_fss_id": None,
                "alt_fss_name": None,
                "opr_hrs": None,
                "comm_status_code": CommunicationStatusCode.NULL.value,
                "comm_status_date": None,
                "remark": None,
            },
        )

    def test_to_str(self):
        result = self.com_base.to_str()
        self.assertEqual(
            result,
            "eff_date: 2025-10-30, "
            "comm_loc_id: None, "
            "comm_type: RCAG, "
            "nav_id: None, "
            "nav_type: None, "
            "city: None, "
            "state_code: VA, "
            "region_code: AEA, "
            "country_code: US, "
            "comm_outlet_name: BUENA VISTA, "
            "lat_deg: 37, "
            "lat_min: 48, "
            "lat_sec: 0.48, "
            "lat_hemis: N, "
            "lat_decimal: 37.80013333, "
            "lon_deg: 79, "
            "lon_min: 10, "
            "lon_sec: 59.1, "
            "lon_hemis: W, "
            "lon_decimal: -79.18308333, "
            "facility_id: ZDC, "
            "facility_name: WASHINGTON, "
            "alt_fss_id: None, "
            "alt_fss_name: None, "
            "opr_hrs: None, "
            "comm_status_code: None, "
            "comm_status_date: None, "
            "remark: None",
        )
