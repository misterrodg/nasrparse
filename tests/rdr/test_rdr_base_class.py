from nasrparse.records.rdr import RDR_BASE
from nasrparse.records.types import RadarFacilityTypeCode, RadarTypeCode

from datetime import date

import unittest


class TestRDR_BASE(unittest.TestCase):
    def setUp(self):
        self.maxDiff = None
        self.rdr_base = RDR_BASE(
            "2025/10/30",
            "MRY",
            "AIRPORT",
            "CA",
            "US",
            "ASR",
            "1",
            "0600-2100",
            "(RADAR_TYPE) ASR-11 ANTENNA LOCATED MARINA MUNI (OAR), REMOTED TO MONTEREY RGNL (MRY). ASR-11 SERVES MRY AND OAR.",
        )

    def tearDown(self):
        pass

    def test_repr(self):
        result = repr(self.rdr_base)
        self.assertEqual(
            result,
            "RDR_BASE ( "
            "EFF_DATE=datetime.date(2025, 10, 30), "
            "FACILITY_ID='MRY', "
            f"FACILITY_TYPE={RadarFacilityTypeCode.AIRPORT!r}, "
            "STATE_CODE='CA', "
            "COUNTRY_CODE='US', "
            f"RADAR_TYPE={RadarTypeCode.AIRPORT_SURVEILLANCE_RADAR!r}, "
            "RADAR_NO=1, "
            "RADAR_HRS='0600-2100', "
            "REMARK='(RADAR_TYPE) ASR-11 ANTENNA LOCATED MARINA MUNI (OAR), REMOTED TO MONTEREY RGNL (MRY). ASR-11 SERVES MRY AND OAR.'"
            " )",
        ),

    def test_ordered_fields(self):
        result = self.rdr_base.ordered_fields()
        self.assertListEqual(
            result,
            [
                "eff_date",
                "facility_id",
                "facility_type",
                "state_code",
                "country_code",
                "radar_type",
                "radar_no",
                "radar_hrs",
                "remark",
            ],
        )

    def test_to_dict(self):
        result = self.rdr_base.to_dict()
        self.assertDictEqual(
            result,
            {
                "eff_date": date(2025, 10, 30).strftime("%Y-%m-%d"),
                "facility_id": "MRY",
                "facility_type": RadarFacilityTypeCode.AIRPORT.value,
                "state_code": "CA",
                "country_code": "US",
                "radar_type": RadarTypeCode.AIRPORT_SURVEILLANCE_RADAR.value,
                "radar_no": 1,
                "radar_hrs": "0600-2100",
                "remark": "(RADAR_TYPE) ASR-11 ANTENNA LOCATED MARINA MUNI (OAR), REMOTED TO MONTEREY RGNL (MRY). ASR-11 SERVES MRY AND OAR.",
            },
        )

    def test_to_str(self):
        result = self.rdr_base.to_str()
        self.assertEqual(
            result,
            "eff_date: 2025-10-30, "
            "facility_id: MRY, "
            "facility_type: AIRPORT, "
            "state_code: CA, "
            "country_code: US, "
            "radar_type: ASR, "
            "radar_no: 1, "
            "radar_hrs: 0600-2100, "
            "remark: (RADAR_TYPE) ASR-11 ANTENNA LOCATED MARINA MUNI (OAR), REMOTED TO MONTEREY RGNL (MRY). ASR-11 SERVES MRY AND OAR.",
        )
