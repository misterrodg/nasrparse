from nasrparse.records.mtr import MTR_AGY
from nasrparse.records.types import MilRouteTypeCode, MTRAgencyTypeCode

from datetime import date

import unittest


class TestMTR_AGY(unittest.TestCase):
    def setUp(self):
        self.maxDiff = None
        self.mtr_agy = MTR_AGY(
            "2025/10/02",
            "IR",
            "062",
            "ZDC",
            "S1",
            "FACSFAC  VACAPES",
            "OCEANA NAS",
            "",
            "VIRGINIA BEACH",
            "VA",
            "23460",
            "757-433-1228",
            "433-1228",
            "SEE GENERAL REMARKS",
        )

    def tearDown(self):
        pass

    def test_repr(self):
        result = repr(self.mtr_agy)
        self.assertEqual(
            result,
            "MTR_AGY ( "
            "EFF_DATE=datetime.date(2025, 10, 2), "
            f"ROUTE_TYPE_CODE={MilRouteTypeCode.IFR_ROUTE!r}, "
            "ROUTE_ID='062', "
            "ARTCC='ZDC', "
            f"AGENCY_TYPE={MTRAgencyTypeCode.SCHEDULING_1!r}, "
            "AGENCY_NAME='FACSFAC  VACAPES', "
            "STATION='OCEANA NAS', "
            "ADDRESS=None, "
            "CITY='VIRGINIA BEACH', "
            "STATE_CODE='VA', "
            "ZIP_CODE='23460', "
            "COMMERCIAL_NO='757-433-1228', "
            "DSN_NO='433-1228', "
            "HOURS='SEE GENERAL REMARKS'"
            " )",
        ),

    def test_ordered_fields(self):
        result = self.mtr_agy.ordered_fields()
        self.assertListEqual(
            result,
            [
                "eff_date",
                "route_type_code",
                "route_id",
                "artcc",
                "agency_type",
                "agency_name",
                "station",
                "address",
                "city",
                "state_code",
                "zip_code",
                "commercial_no",
                "dsn_no",
                "hours",
            ],
        )

    def test_to_dict(self):
        result = self.mtr_agy.to_dict()
        self.assertDictEqual(
            result,
            {
                "eff_date": date(2025, 10, 2).strftime("%Y-%m-%d"),
                "route_type_code": MilRouteTypeCode.IFR_ROUTE.value,
                "route_id": "062",
                "artcc": "ZDC",
                "agency_type": MTRAgencyTypeCode.SCHEDULING_1.value,
                "agency_name": "FACSFAC  VACAPES",
                "station": "OCEANA NAS",
                "address": None,
                "city": "VIRGINIA BEACH",
                "state_code": "VA",
                "zip_code": "23460",
                "commercial_no": "757-433-1228",
                "dsn_no": "433-1228",
                "hours": "SEE GENERAL REMARKS",
            },
        )

    def test_to_str(self):
        result = self.mtr_agy.to_str()
        self.assertEqual(
            result,
            "eff_date: 2025-10-02, "
            "route_type_code: IR, "
            "route_id: 062, "
            "artcc: ZDC, "
            "agency_type: S1, "
            "agency_name: FACSFAC  VACAPES, "
            "station: OCEANA NAS, "
            "address: None, "
            "city: VIRGINIA BEACH, "
            "state_code: VA, "
            "zip_code: 23460, "
            "commercial_no: 757-433-1228, "
            "dsn_no: 433-1228, "
            "hours: SEE GENERAL REMARKS",
        )
