from nasrparse.records.mil import MIL_BASE
from nasrparse.records.types import FacilityOperatorCode, SiteTypeCode

from datetime import date

import unittest


class TestMIL_BASE(unittest.TestCase):
    def setUp(self):
        self.maxDiff = None
        self.mil_base = MIL_BASE(
            "2025/10/30",
            "16815.",
            "A",
            "NC",
            "NCA",
            "JACKSONVILLE",
            "US",
            "N",
            "NEW RIVER OPS",
            "SEE RMRKS",
            "",
            "244.775 1100-2200Z++ DLY (OT BROADCASTS ASOS INFO).",
            "(MIL_OPS_HRS) OPERATIONS HOURS 0700-SS MON-FRI, 0700-1200 SAT, 1600-2000 SUN.",
        )

    def tearDown(self):
        pass

    def test_repr(self):
        result = repr(self.mil_base)
        self.assertEqual(
            result,
            "MIL_BASE ( "
            "EFF_DATE=datetime.date(2025, 10, 30), "
            "SITE_NO='16815.', "
            f"SITE_TYPE_CODE={SiteTypeCode.AIRPORT!r}, "
            "STATE_CODE='NC', "
            "ARPT_ID='NCA', "
            "CITY='JACKSONVILLE', "
            "COUNTRY_CODE='US', "
            f"MIL_OPS_OPER_CODE={FacilityOperatorCode.USN!r}, "
            "MIL_OPS_CALL='NEW RIVER OPS', "
            "MIL_OPS_HRS='SEE RMRKS', "
            "AMCP_HRS=None, "
            "PMSV_HRS='244.775 1100-2200Z++ DLY (OT BROADCASTS ASOS INFO).', "
            "REMARK='(MIL_OPS_HRS) OPERATIONS HOURS 0700-SS MON-FRI, 0700-1200 SAT, 1600-2000 SUN.'"
            " )",
        ),

    def test_ordered_fields(self):
        result = self.mil_base.ordered_fields()
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
                "mil_ops_oper_code",
                "mil_ops_call",
                "mil_ops_hrs",
                "amcp_hrs",
                "pmsv_hrs",
                "remark",
            ],
        )

    def test_to_dict(self):
        result = self.mil_base.to_dict()
        self.assertDictEqual(
            result,
            {
                "eff_date": date(2025, 10, 30).strftime("%Y-%m-%d"),
                "site_no": "16815.",
                "site_type_code": SiteTypeCode.AIRPORT.value,
                "state_code": "NC",
                "arpt_id": "NCA",
                "city": "JACKSONVILLE",
                "country_code": "US",
                "mil_ops_oper_code": FacilityOperatorCode.USN.value,
                "mil_ops_call": "NEW RIVER OPS",
                "mil_ops_hrs": "SEE RMRKS",
                "amcp_hrs": None,
                "pmsv_hrs": "244.775 1100-2200Z++ DLY (OT BROADCASTS ASOS INFO).",
                "remark": "(MIL_OPS_HRS) OPERATIONS HOURS 0700-SS MON-FRI, 0700-1200 SAT, 1600-2000 SUN.",
            },
        )

    def test_to_str(self):
        result = self.mil_base.to_str()
        self.assertEqual(
            result,
            "eff_date: 2025-10-30, "
            "site_no: 16815., "
            "site_type_code: A, "
            "state_code: NC, "
            "arpt_id: NCA, "
            "city: JACKSONVILLE, "
            "country_code: US, "
            "mil_ops_oper_code: N, "
            "mil_ops_call: NEW RIVER OPS, "
            "mil_ops_hrs: SEE RMRKS, "
            "amcp_hrs: None, "
            "pmsv_hrs: 244.775 1100-2200Z++ DLY (OT BROADCASTS ASOS INFO)., "
            "remark: (MIL_OPS_HRS) OPERATIONS HOURS 0700-SS MON-FRI, 0700-1200 SAT, 1600-2000 SUN.",
        )
