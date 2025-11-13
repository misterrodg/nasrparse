from nasrparse.records.pfr import PFR_BASE
from nasrparse.records.types import PrefRouteTypeCode

from datetime import date

import unittest


class TestPFR_BASE(unittest.TestCase):
    def setUp(self):
        self.maxDiff = None
        self.pfr_base = PFR_BASE(
            "2025/10/02",
            "IAD",
            "ALB",
            "H",
            "1",
            "WASHINGTON",
            "DC",
            "US",
            "ALBANY",
            "NY",
            "US",
            "TO ALB,SCH",
            "",
            "TURBOJETS  PART 121 AND 129 ONLY",
            "1100-0400",
            "",
            "",
            "",
            "",
            "",
            "",
            "JCOBY4 SWANN BROSS Q419 RBV Q22 LLUND TRUDE V487 CANAN",
        )

    def tearDown(self):
        pass

    def test_repr(self):
        result = repr(self.pfr_base)
        self.assertEqual(
            result,
            "PFR_BASE ( "
            "EFF_DATE=datetime.date(2025, 10, 2), "
            "ORIGIN_ID='IAD', "
            "DSTN_ID='ALB', "
            f"PFR_TYPE_CODE={PrefRouteTypeCode.HIGH_ALTITUDE!r}, "
            "ROUTE_NO=1, "
            "ORIGIN_CITY='WASHINGTON', "
            "ORIGIN_STATE_CODE='DC', "
            "ORIGIN_COUNTRY_CODE='US', "
            "DSTN_CITY='ALBANY', "
            "DSTN_STATE_CODE='NY', "
            "DSTN_COUNTRY_CODE='US', "
            "SPECIAL_AREA_DESCRIP='TO ALB,SCH', "
            "ALT_DESCRIP=None, "
            "AIRCRAFT='TURBOJETS  PART 121 AND 129 ONLY', "
            "HOURS='1100-0400', "
            "ROUTE_DIR_DESCRIP=None, "
            "DESIGNATOR=None, "
            "NAR_TYPE=None, "
            "INLAND_FAC_FIX=None, "
            "COASTAL_FIX=None, "
            "DESTINATION=None, "
            "ROUTE_STRING='JCOBY4 SWANN BROSS Q419 RBV Q22 LLUND TRUDE V487 CANAN'"
            " )",
        ),

    def test_ordered_fields(self):
        result = self.pfr_base.ordered_fields()
        self.assertListEqual(
            result,
            [
                "eff_date",
                "origin_id",
                "dstn_id",
                "pfr_type_code",
                "route_no",
                "origin_city",
                "origin_state_code",
                "origin_country_code",
                "dstn_city",
                "dstn_state_code",
                "dstn_country_code",
                "special_area_descrip",
                "alt_descrip",
                "aircraft",
                "hours",
                "route_dir_descrip",
                "designator",
                "nar_type",
                "inland_fac_fix",
                "coastal_fix",
                "destination",
                "route_string",
            ],
        )

    def test_to_dict(self):
        result = self.pfr_base.to_dict()
        self.assertDictEqual(
            result,
            {
                "eff_date": date(2025, 10, 2).strftime("%Y-%m-%d"),
                "origin_id": "IAD",
                "dstn_id": "ALB",
                "pfr_type_code": PrefRouteTypeCode.HIGH_ALTITUDE.value,
                "route_no": 1,
                "origin_city": "WASHINGTON",
                "origin_state_code": "DC",
                "origin_country_code": "US",
                "dstn_city": "ALBANY",
                "dstn_state_code": "NY",
                "dstn_country_code": "US",
                "special_area_descrip": "TO ALB,SCH",
                "alt_descrip": None,
                "aircraft": "TURBOJETS  PART 121 AND 129 ONLY",
                "hours": "1100-0400",
                "route_dir_descrip": None,
                "designator": None,
                "nar_type": None,
                "inland_fac_fix": None,
                "coastal_fix": None,
                "destination": None,
                "route_string": "JCOBY4 SWANN BROSS Q419 RBV Q22 LLUND TRUDE V487 CANAN",
            },
        )

    def test_to_str(self):
        result = self.pfr_base.to_str()
        self.assertEqual(
            result,
            "eff_date: 2025-10-02, "
            "origin_id: IAD, "
            "dstn_id: ALB, "
            "pfr_type_code: H, "
            "route_no: 1, "
            "origin_city: WASHINGTON, "
            "origin_state_code: DC, "
            "origin_country_code: US, "
            "dstn_city: ALBANY, "
            "dstn_state_code: NY, "
            "dstn_country_code: US, "
            "special_area_descrip: TO ALB,SCH, "
            "alt_descrip: None, "
            "aircraft: TURBOJETS  PART 121 AND 129 ONLY, "
            "hours: 1100-0400, "
            "route_dir_descrip: None, "
            "designator: None, "
            "nar_type: None, "
            "inland_fac_fix: None, "
            "coastal_fix: None, "
            "destination: None, "
            "route_string: JCOBY4 SWANN BROSS Q419 RBV Q22 LLUND TRUDE V487 CANAN",
        )
