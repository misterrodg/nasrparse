from nasrparse.records.atc import ATC_SVC
from nasrparse.records.types import FacilityTypeCode, SiteTypeCode

from datetime import date

import unittest


class TestATC_SVC(unittest.TestCase):
    def setUp(self):
        self.maxDiff = None
        self.atc_svc = ATC_SVC(
            "2025/10/30",
            "25986.",
            "A",
            "ATCT-TRACON",
            "VA",
            "ROA",
            "ROANOKE",
            "US",
            "ARTS-II",
        )

    def tearDown(self):
        pass

    def test_repr(self):
        result = repr(self.atc_svc)
        self.assertEqual(
            result,
            "ATC_SVC ( "
            "EFF_DATE=datetime.date(2025, 10, 30), "
            "SITE_NO='25986.', "
            f"SITE_TYPE_CODE={SiteTypeCode.AIRPORT!r}, "
            f"FACILITY_TYPE={FacilityTypeCode.ATCT_TRACON!r}, "
            "STATE_CODE='VA', "
            "FACILITY_ID='ROA', "
            "CITY='ROANOKE', "
            "COUNTRY_CODE='US', "
            "CTL_SVC='ARTS-II'"
            " )",
        ),

    def test_ordered_fields(self):
        result = self.atc_svc.ordered_fields()
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
                "ctl_svc",
            ],
        )

    def test_to_dict(self):
        result = self.atc_svc.to_dict()
        self.assertDictEqual(
            result,
            {
                "eff_date": date(2025, 10, 30).strftime("%Y-%m-%d"),
                "site_no": "25986.",
                "site_type_code": SiteTypeCode.AIRPORT.value,
                "facility_type": FacilityTypeCode.ATCT_TRACON.value,
                "state_code": "VA",
                "facility_id": "ROA",
                "city": "ROANOKE",
                "country_code": "US",
                "ctl_svc": "ARTS-II",
            },
        )

    def test_to_str(self):
        result = self.atc_svc.to_str()
        self.assertEqual(
            result,
            "eff_date: 2025-10-30, "
            "site_no: 25986., "
            "site_type_code: A, "
            "facility_type: ATCT-TRACON, "
            "state_code: VA, "
            "facility_id: ROA, "
            "city: ROANOKE, "
            "country_code: US, "
            "ctl_svc: ARTS-II",
        )
