from nasrparse.records.atc import ATC_ATIS
from nasrparse.records.types import FacilityTypeCode, SiteTypeCode

from datetime import date

import unittest


class TestATC_ATIS(unittest.TestCase):
    def setUp(self):
        self.maxDiff = None
        self.atc_atis = ATC_ATIS(
            "2025/10/30",
            "00164.",
            "A",
            "ATCT-TRACON",
            "AL",
            "BHM",
            "BIRMINGHAM",
            "US",
            "1",
            "",
            "24",
            "",
        )

    def tearDown(self):
        pass

    def test_repr(self):
        result = repr(self.atc_atis)
        self.assertEqual(
            result,
            "ATC_ATIS ( "
            "EFF_DATE=datetime.date(2025, 10, 30), "
            "SITE_NO='00164.', "
            f"SITE_TYPE_CODE={SiteTypeCode.AIRPORT!r}, "
            f"FACILITY_TYPE={FacilityTypeCode.ATCT_TRACON!r}, "
            "STATE_CODE='AL', "
            "FACILITY_ID='BHM', "
            "CITY='BIRMINGHAM', "
            "COUNTRY_CODE='US', "
            "ATIS_NO='1', "
            "DESCRIPTION=None, "
            "ATIS_HRS='24', "
            "ATIS_PHONE_NO=None"
            " )",
        ),

    def test_ordered_fields(self):
        result = self.atc_atis.ordered_fields()
        self.assertListEqual(
            result,
            [
                "eff_date",
                "site_no",
                "site_type_code",
                "facility_type",
                "state_code",
                "facility_id",
                "city",
                "country_code",
                "atis_no",
                "description",
                "atis_hrs",
                "atis_phone_no",
            ],
        )

    def test_to_dict(self):
        result = self.atc_atis.to_dict()
        self.assertDictEqual(
            result,
            {
                "eff_date": date(2025, 10, 30).strftime("%Y-%m-%d"),
                "site_no": "00164.",
                "site_type_code": SiteTypeCode.AIRPORT.value,
                "facility_type": FacilityTypeCode.ATCT_TRACON.value,
                "state_code": "AL",
                "facility_id": "BHM",
                "city": "BIRMINGHAM",
                "country_code": "US",
                "atis_no": "1",
                "description": None,
                "atis_hrs": "24",
                "atis_phone_no": None,
            },
        )

    def test_to_str(self):
        result = self.atc_atis.to_str()
        self.assertEqual(
            result,
            "eff_date: 2025-10-30, "
            "site_no: 00164., "
            "site_type_code: A, "
            "facility_type: ATCT-TRACON, "
            "state_code: AL, "
            "facility_id: BHM, "
            "city: BIRMINGHAM, "
            "country_code: US, "
            "atis_no: 1, "
            "description: None, "
            "atis_hrs: 24, "
            "atis_phone_no: None",
        )
