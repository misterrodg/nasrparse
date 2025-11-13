from nasrparse.records.cls import CLS_ARSP
from nasrparse.records.types import SiteTypeCode

from datetime import date

import unittest


class TestCLS_ARSP(unittest.TestCase):
    def setUp(self):
        self.maxDiff = None
        self.cls_arsp = CLS_ARSP(
            "2025/10/30",
            "08556.",
            "A",
            "MD",
            "FDK",
            "FREDERICK",
            "US",
            "",
            "",
            "Y",
            "Y",
            "CLASS D SVC 0700-2100; OTHER TIMES CLASS E",
            "",
        )

    def tearDown(self):
        pass

    def test_repr(self):
        result = repr(self.cls_arsp)
        self.assertEqual(
            result,
            "CLS_ARSP ( "
            "EFF_DATE=datetime.date(2025, 10, 30), "
            "SITE_NO='08556.', "
            f"SITE_TYPE_CODE={SiteTypeCode.AIRPORT!r}, "
            "STATE_CODE='MD', "
            "ARPT_ID='FDK', "
            "CITY='FREDERICK', "
            "COUNTRY_CODE='US', "
            "CLASS_B_AIRSPACE=None, "
            "CLASS_C_AIRSPACE=None, "
            "CLASS_D_AIRSPACE=True, "
            "CLASS_E_AIRSPACE=True, "
            "AIRSPACE_HRS='CLASS D SVC 0700-2100; OTHER TIMES CLASS E', "
            "REMARK=None"
            " )",
        ),

    def test_ordered_fields(self):
        result = self.cls_arsp.ordered_fields()
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
                "class_b_airspace",
                "class_c_airspace",
                "class_d_airspace",
                "class_e_airspace",
                "airspace_hrs",
                "remark",
            ],
        )

    def test_to_dict(self):
        result = self.cls_arsp.to_dict()
        self.assertDictEqual(
            result,
            {
                "eff_date": date(2025, 10, 30).strftime("%Y-%m-%d"),
                "site_no": "08556.",
                "site_type_code": SiteTypeCode.AIRPORT.value,
                "state_code": "MD",
                "arpt_id": "FDK",
                "city": "FREDERICK",
                "country_code": "US",
                "class_b_airspace": None,
                "class_c_airspace": None,
                "class_d_airspace": True,
                "class_e_airspace": True,
                "airspace_hrs": "CLASS D SVC 0700-2100; OTHER TIMES CLASS E",
                "remark": None,
            },
        )

    def test_to_str(self):
        result = self.cls_arsp.to_str()
        self.assertEqual(
            result,
            "eff_date: 2025-10-30, "
            "site_no: 08556., "
            "site_type_code: A, "
            "state_code: MD, "
            "arpt_id: FDK, "
            "city: FREDERICK, "
            "country_code: US, "
            "class_b_airspace: None, "
            "class_c_airspace: None, "
            "class_d_airspace: True, "
            "class_e_airspace: True, "
            "airspace_hrs: CLASS D SVC 0700-2100; OTHER TIMES CLASS E, "
            "remark: None",
        )
