from nasrparse.records.pfr import PFR_SEG
from nasrparse.records.types import PrefRouteTypeCode

from datetime import date

import unittest


class TestPFR_SEG(unittest.TestCase):
    def setUp(self):
        self.maxDiff = None
        self.pfr_seg = PFR_SEG(
            "2025/10/02",
            "IAD",
            "BOS",
            "H",
            "2",
            "10",
            "SWANN",
            "FIX",
            "MD",
            "US",
            "K6",
            "",
            "BROSS",
        )

    def tearDown(self):
        pass

    def test_repr(self):
        result = repr(self.pfr_seg)
        self.assertEqual(
            result,
            "PFR_SEG ( "
            "EFF_DATE=datetime.date(2025, 10, 2), "
            "ORIGIN_ID='IAD', "
            "DSTN_ID='BOS', "
            f"PFR_TYPE_CODE={PrefRouteTypeCode.HIGH_ALTITUDE!r}, "
            "ROUTE_NO=2, "
            "SEGMENT_SEQ=10, "
            "SEG_VALUE='SWANN', "
            "SEG_TYPE='FIX', "
            "STATE_CODE='MD', "
            "COUNTRY_CODE='US', "
            "ICAO_REGION_CODE='K6', "
            "NAV_TYPE=None, "
            "NEXT_SEG='BROSS'"
            " )",
        ),

    def test_ordered_fields(self):
        result = self.pfr_seg.ordered_fields()
        self.assertListEqual(
            result,
            [
                "eff_date",
                "origin_id",
                "dstn_id",
                "pfr_type_code",
                "route_no",
                "segment_seq",
                "seg_value",
                "seg_type",
                "state_code",
                "country_code",
                "icao_region_code",
                "nav_type",
                "next_seg",
            ],
        )

    def test_to_dict(self):
        result = self.pfr_seg.to_dict()
        self.assertDictEqual(
            result,
            {
                "eff_date": date(2025, 10, 2).strftime("%Y-%m-%d"),
                "origin_id": "IAD",
                "dstn_id": "BOS",
                "pfr_type_code": PrefRouteTypeCode.HIGH_ALTITUDE.value,
                "route_no": 2,
                "segment_seq": 10,
                "seg_value": "SWANN",
                "seg_type": "FIX",
                "state_code": "MD",
                "country_code": "US",
                "icao_region_code": "K6",
                "nav_type": None,
                "next_seg": "BROSS",
            },
        )

    def test_to_str(self):
        result = self.pfr_seg.to_str()
        self.assertEqual(
            result,
            "eff_date: 2025-10-02, "
            "origin_id: IAD, "
            "dstn_id: BOS, "
            "pfr_type_code: H, "
            "route_no: 2, "
            "segment_seq: 10, "
            "seg_value: SWANN, "
            "seg_type: FIX, "
            "state_code: MD, "
            "country_code: US, "
            "icao_region_code: K6, "
            "nav_type: None, "
            "next_seg: BROSS",
        )
