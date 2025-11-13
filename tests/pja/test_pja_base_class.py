from nasrparse.records.pja import PJA_BASE
from nasrparse.records.types import AltitudeTypeCode, PointCode, SiteTypeCode

from datetime import date

import unittest


class TestPJA_BASE(unittest.TestCase):
    def setUp(self):
        self.maxDiff = None
        self.pja_base = PJA_BASE(
            "2025/10/02",
            "PVA020",
            "LDN",
            "VORTAC",
            "249.41",
            "26.43",
            "LINDEN",
            "VA",
            "NEW MARKET",
            "38-39-21.4008N",
            "38.65594466",
            "078-42-30.3058W",
            "-78.70841827",
            "8W2",
            "25893.1",
            "A",
            "NEW MARKET/BLUE RIDGE SPORT",
            "17500",
            "MSL",
            "",
            "Y",
            "Y",
            "",
            "0800 LCL UNTIL DARK",
            "DCA",
            "LEESBURG",
            "CIVIL",
            "",
            "BLUE RIDGE SPORT AVIATION",
            "",
        )

    def tearDown(self):
        pass

    def test_repr(self):
        result = repr(self.pja_base)
        self.assertEqual(
            result,
            "PJA_BASE ( "
            "EFF_DATE=datetime.date(2025, 10, 2), "
            "PJA_ID='PVA020', "
            "NAV_ID='LDN', "
            f"NAV_TYPE={PointCode.VORTAC!r}, "
            "RADIAL=249.41, "
            "DISTANCE=26.43, "
            "NAVAID_NAME='LINDEN', "
            "STATE_CODE='VA', "
            "CITY='NEW MARKET', "
            "LATITUDE='38-39-21.4008N', "
            "LAT_DECIMAL=38.65594466, "
            "LONGITUDE='078-42-30.3058W', "
            "LONG_DECIMAL=-78.70841827, "
            "ARPT_ID='8W2', "
            "SITE_NO='25893.1', "
            f"SITE_TYPE_CODE={SiteTypeCode.AIRPORT!r}, "
            "DROP_ZONE_NAME='NEW MARKET/BLUE RIDGE SPORT', "
            "MAX_ALTITUDE='17500', "
            f"MAX_ALTITUDE_TYPE_CODE={AltitudeTypeCode.MSL!r}, "
            "PJA_RADIUS=None, "
            "CHART_REQUEST_FLAG=True, "
            "PUBLISH_CRITERIA=True, "
            "DESCRIPTION=None, "
            "TIME_OF_USE='0800 LCL UNTIL DARK', "
            "FSS_ID='DCA', "
            "FSS_NAME='LEESBURG', "
            "PJA_USE='CIVIL', "
            "VOLUME=None, "
            "PJA_USER='BLUE RIDGE SPORT AVIATION', "
            "REMARK=None"
            " )",
        ),

    def test_ordered_fields(self):
        result = self.pja_base.ordered_fields()
        self.assertListEqual(
            result,
            [
                "eff_date",
                "pja_id",
                "nav_id",
                "nav_type",
                "radial",
                "distance",
                "navaid_name",
                "state_code",
                "city",
                "latitude",
                "lat_decimal",
                "longitude",
                "long_decimal",
                "arpt_id",
                "site_no",
                "site_type_code",
                "drop_zone_name",
                "max_altitude",
                "max_altitude_type_code",
                "pja_radius",
                "chart_request_flag",
                "publish_criteria",
                "description",
                "time_of_use",
                "fss_id",
                "fss_name",
                "pja_use",
                "volume",
                "pja_user",
                "remark",
            ],
        )

    def test_to_dict(self):
        result = self.pja_base.to_dict()
        self.assertDictEqual(
            result,
            {
                "eff_date": date(2025, 10, 2).strftime("%Y-%m-%d"),
                "pja_id": "PVA020",
                "nav_id": "LDN",
                "nav_type": PointCode.VORTAC.value,
                "radial": 249.41,
                "distance": 26.43,
                "navaid_name": "LINDEN",
                "state_code": "VA",
                "city": "NEW MARKET",
                "latitude": "38-39-21.4008N",
                "lat_decimal": 38.65594466,
                "longitude": "078-42-30.3058W",
                "long_decimal": -78.70841827,
                "arpt_id": "8W2",
                "site_no": "25893.1",
                "site_type_code": SiteTypeCode.AIRPORT.value,
                "drop_zone_name": "NEW MARKET/BLUE RIDGE SPORT",
                "max_altitude": "17500",
                "max_altitude_type_code": AltitudeTypeCode.MSL.value,
                "pja_radius": None,
                "chart_request_flag": True,
                "publish_criteria": True,
                "description": None,
                "time_of_use": "0800 LCL UNTIL DARK",
                "fss_id": "DCA",
                "fss_name": "LEESBURG",
                "pja_use": "CIVIL",
                "volume": None,
                "pja_user": "BLUE RIDGE SPORT AVIATION",
                "remark": None,
            },
        )

    def test_to_str(self):
        result = self.pja_base.to_str()
        self.assertEqual(
            result,
            "eff_date: 2025-10-02, "
            "pja_id: PVA020, "
            "nav_id: LDN, "
            "nav_type: VORTAC, "
            "radial: 249.41, "
            "distance: 26.43, "
            "navaid_name: LINDEN, "
            "state_code: VA, "
            "city: NEW MARKET, "
            "latitude: 38-39-21.4008N, "
            "lat_decimal: 38.65594466, "
            "longitude: 078-42-30.3058W, "
            "long_decimal: -78.70841827, "
            "arpt_id: 8W2, "
            "site_no: 25893.1, "
            "site_type_code: A, "
            "drop_zone_name: NEW MARKET/BLUE RIDGE SPORT, "
            "max_altitude: 17500, "
            "max_altitude_type_code: MSL, "
            "pja_radius: None, "
            "chart_request_flag: True, "
            "publish_criteria: True, "
            "description: None, "
            "time_of_use: 0800 LCL UNTIL DARK, "
            "fss_id: DCA, "
            "fss_name: LEESBURG, "
            "pja_use: CIVIL, "
            "volume: None, "
            "pja_user: BLUE RIDGE SPORT AVIATION, "
            "remark: None",
        )
