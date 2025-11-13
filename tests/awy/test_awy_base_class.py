from nasrparse.records.awy import AWY_BASE
from nasrparse.records.types import AirwayDesignationCode, AirwayLocationCode

from datetime import date

import unittest


class TestAWY_BASE(unittest.TestCase):
    def setUp(self):
        self.maxDiff = None
        self.awy_base = AWY_BASE(
            "2025/10/02",
            "Y",
            "C",
            "J149",
            "J",
            "2023/04/25",
            "",
            "AML GINYA RAMAY EYTEE SINDE GEFFS HACKS SUMET VLADY EMPTY MECAN ROD FWA",
        )

    def tearDown(self):
        pass

    def test_repr(self):
        result = repr(self.awy_base)
        self.assertEqual(
            result,
            "AWY_BASE ( "
            "EFF_DATE=datetime.date(2025, 10, 2), "
            "REGULATORY=True, "
            f"AWY_LOCATION={AirwayLocationCode.CONTIGUOUS_US!r}, "
            "AWY_ID='J149', "
            f"AWY_DESIGNATION={AirwayDesignationCode.JET!r}, "
            "UPDATE_DATE=datetime.date(2023, 4, 25), "
            "REMARK=None, "
            "AIRWAY_STRING='AML GINYA RAMAY EYTEE SINDE GEFFS HACKS SUMET VLADY EMPTY MECAN ROD FWA'"
            " )",
        ),

    def test_ordered_fields(self):
        result = self.awy_base.ordered_fields()
        self.assertListEqual(
            result,
            [
                "eff_date",
                "regulatory",
                "awy_location",
                "awy_id",
                "awy_designation",
                "update_date",
                "remark",
                "airway_string",
            ],
        )

    def test_to_dict(self):
        result = self.awy_base.to_dict()
        self.assertDictEqual(
            result,
            {
                "eff_date": date(2025, 10, 2).strftime("%Y-%m-%d"),
                "regulatory": True,
                "awy_location": AirwayLocationCode.CONTIGUOUS_US.value,
                "awy_id": "J149",
                "awy_designation": AirwayDesignationCode.JET.value,
                "update_date": date(2023, 4, 25).strftime("%Y-%m-%d"),
                "remark": None,
                "airway_string": "AML GINYA RAMAY EYTEE SINDE GEFFS HACKS SUMET VLADY EMPTY MECAN ROD FWA",
            },
        )

    def test_to_str(self):
        result = self.awy_base.to_str()
        self.assertEqual(
            result,
            "eff_date: 2025-10-02, "
            "regulatory: True, "
            "awy_location: C, "
            "awy_id: J149, "
            "awy_designation: J, "
            "update_date: 2023-04-25, "
            "remark: None, "
            "airway_string: AML GINYA RAMAY EYTEE SINDE GEFFS HACKS SUMET VLADY EMPTY MECAN ROD FWA",
        )
