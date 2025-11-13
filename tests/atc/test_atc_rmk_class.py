from nasrparse.records.atc import ATC_RMK
from nasrparse.records.types import FacilityTypeCode, SiteTypeCode

from datetime import date

import unittest


class TestATC_RMK(unittest.TestCase):
    def setUp(self):
        self.maxDiff = None
        self.atc_rmk = ATC_RMK(
            "2025/10/30",
            "24226.1",
            "A",
            "NON-ATCT",
            "TX",
            "00R",
            "LIVINGSTON",
            "US",
            "1",
            "ARPT_CTL_REMARK",
            "ATC_REMARK",
            "1",
            "APCH/DEP CTL SVC PRVDD BY HOUSTON ARTCC (ZHU) ON FREQS 125.175/285.575 (LUFKIN RCAG).",
        )

    def tearDown(self):
        pass

    def test_repr(self):
        result = repr(self.atc_rmk)
        self.assertEqual(
            result,
            "ATC_RMK ( "
            "EFF_DATE=datetime.date(2025, 10, 30), "
            "SITE_NO='24226.1', "
            f"SITE_TYPE_CODE={SiteTypeCode.AIRPORT!r}, "
            f"FACILITY_TYPE={FacilityTypeCode.NON_ATCT!r}, "
            "STATE_CODE='TX', "
            "FACILITY_ID='00R', "
            "CITY='LIVINGSTON', "
            "COUNTRY_CODE='US', "
            "LEGACY_ELEMENT_NUMBER='1', "
            "TAB_NAME='ARPT_CTL_REMARK', "
            "REF_COL_NAME='ATC_REMARK', "
            "REMARK_NO=1, "
            "REMARK='APCH/DEP CTL SVC PRVDD BY HOUSTON ARTCC (ZHU) ON FREQS 125.175/285.575 (LUFKIN RCAG).'"
            " )",
        ),

    def test_ordered_fields(self):
        result = self.atc_rmk.ordered_fields()
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
                "legacy_element_number",
                "tab_name",
                "ref_col_name",
                "remark_no",
                "remark",
            ],
        )

    def test_to_dict(self):
        result = self.atc_rmk.to_dict()
        self.assertDictEqual(
            result,
            {
                "eff_date": date(2025, 10, 30).strftime("%Y-%m-%d"),
                "site_no": "24226.1",
                "site_type_code": SiteTypeCode.AIRPORT.value,
                "facility_type": FacilityTypeCode.NON_ATCT.value,
                "state_code": "TX",
                "facility_id": "00R",
                "city": "LIVINGSTON",
                "country_code": "US",
                "legacy_element_number": "1",
                "tab_name": "ARPT_CTL_REMARK",
                "ref_col_name": "ATC_REMARK",
                "remark_no": 1,
                "remark": "APCH/DEP CTL SVC PRVDD BY HOUSTON ARTCC (ZHU) ON FREQS 125.175/285.575 (LUFKIN RCAG).",
            },
        )

    def test_to_str(self):
        result = self.atc_rmk.to_str()
        self.assertEqual(
            result,
            "eff_date: 2025-10-30, "
            "site_no: 24226.1, "
            "site_type_code: A, "
            "facility_type: NON-ATCT, "
            "state_code: TX, "
            "facility_id: 00R, "
            "city: LIVINGSTON, "
            "country_code: US, "
            "legacy_element_number: 1, "
            "tab_name: ARPT_CTL_REMARK, "
            "ref_col_name: ATC_REMARK, "
            "remark_no: 1, "
            "remark: APCH/DEP CTL SVC PRVDD BY HOUSTON ARTCC (ZHU) ON FREQS 125.175/285.575 (LUFKIN RCAG).",
        )
