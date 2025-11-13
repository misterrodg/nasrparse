from nasrparse.records.awy import AWY_SEG
from nasrparse.records.types import AirwayLocationCode

from datetime import date

import unittest


class TestAWY_SEG(unittest.TestCase):
    def setUp(self):
        self.maxDiff = None
        self.awy_seg = AWY_SEG(
            "2023/10/05",
            "Y",
            "C",
            "J149",
            "10",
            "AML",
            "VOR/DME",
            "ARMEL",
            "HERNDON",
            "",
            "VA",
            "US",
            "GINYA",
            "280.79",
            "98.68",
            "10",
            "",
            "",
            "",
            "N",
            "N",
            "N",
            "",
        )

    def tearDown(self):
        pass

    def test_repr(self):
        result = repr(self.awy_seg)
        self.assertEqual(
            result,
            "AWY_SEG ( "
            "EFF_DATE=datetime.date(2023, 10, 5), "
            "REGULATORY=True, "
            f"AWY_LOCATION={AirwayLocationCode.CONTIGUOUS_US!r}, "
            "AWY_ID='J149', "
            "POINT_SEQ=10, "
            "SEG_VALUE='AML', "
            "SEG_TYPE='VOR/DME', "
            "NAV_NAME='ARMEL', "
            "NAV_CITY='HERNDON', "
            "ICAO_REGION_CODE=None, "
            "STATE_CODE='VA', "
            "COUNTRY_CODE='US', "
            "NEXT_SEG='GINYA', "
            "MAG_COURSE=280.79, "
            "OPP_MAG_COURSE=98.68, "
            "MAG_COURSE_DIST=10.0, "
            "CHGOVR_PT=None, "
            "CHGOVR_PT_NAME=None, "
            "CHGOVR_PT_DIST=None, "
            "AWY_SEG_GAP_FLAG=False, "
            "SIGNAL_GAP_FLAG=False, "
            "DOGLEG=False, "
            "REMARK=None"
            " )",
        ),

    def test_ordered_fields(self):
        result = self.awy_seg.ordered_fields()
        self.assertListEqual(
            result,
            [
                "eff_date",
                "regulatory",
                "awy_location",
                "awy_id",
                "point_seq",
                "seg_value",
                "seg_type",
                "nav_name",
                "nav_city",
                "icao_region_code",
                "state_code",
                "country_code",
                "next_seg",
                "mag_course",
                "opp_mag_course",
                "mag_course_dist",
                "chgovr_pt",
                "chgovr_pt_name",
                "chgovr_pt_dist",
                "awy_seg_gap_flag",
                "signal_gap_flag",
                "dogleg",
                "remark",
            ],
        )

    def test_to_dict(self):
        result = self.awy_seg.to_dict()
        self.assertDictEqual(
            result,
            {
                "eff_date": date(2023, 10, 5).strftime("%Y-%m-%d"),
                "regulatory": True,
                "awy_location": AirwayLocationCode.CONTIGUOUS_US.value,
                "awy_id": "J149",
                "point_seq": 10,
                "seg_value": "AML",
                "seg_type": "VOR/DME",
                "nav_name": "ARMEL",
                "nav_city": "HERNDON",
                "icao_region_code": None,
                "state_code": "VA",
                "country_code": "US",
                "next_seg": "GINYA",
                "mag_course": 280.79,
                "opp_mag_course": 98.68,
                "mag_course_dist": 10.0,
                "chgovr_pt": None,
                "chgovr_pt_name": None,
                "chgovr_pt_dist": None,
                "awy_seg_gap_flag": False,
                "signal_gap_flag": False,
                "dogleg": False,
                "remark": None,
            },
        )

    def test_to_str(self):
        result = self.awy_seg.to_str()
        self.assertEqual(
            result,
            "eff_date: 2023-10-05, "
            "regulatory: True, "
            "awy_location: C, "
            "awy_id: J149, "
            "point_seq: 10, "
            "seg_value: AML, "
            "seg_type: VOR/DME, "
            "nav_name: ARMEL, "
            "nav_city: HERNDON, "
            "icao_region_code: None, "
            "state_code: VA, "
            "country_code: US, "
            "next_seg: GINYA, "
            "mag_course: 280.79, "
            "opp_mag_course: 98.68, "
            "mag_course_dist: 10.0, "
            "chgovr_pt: None, "
            "chgovr_pt_name: None, "
            "chgovr_pt_dist: None, "
            "awy_seg_gap_flag: False, "
            "signal_gap_flag: False, "
            "dogleg: False, "
            "remark: None",
        )
