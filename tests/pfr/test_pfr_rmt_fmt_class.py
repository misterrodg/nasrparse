from nasrparse.records.pfr import PFR_RMT_FMT
from nasrparse.records.types import PrefRouteTypeCode

from datetime import date

import unittest


class TestPFR_RMT_FMT(unittest.TestCase):
    def setUp(self):
        self.maxDiff = None
        self.pfr_rmt_fmt = PFR_RMT_FMT(
            "IAD",
            "IAD JDUBB4 RRSIN GSO Q83 ROYCO Q85 LPERD SNFLD3 MCO",
            "MCO",
            "",
            "H",
            "FROM DCA,DAA,IAD,JYO,MRB,OKV TO ISM,MCO",
            "",
            "",
            "",
            "5",
            "ZDC",
            "ZJX",
        )

    def tearDown(self):
        pass

    def test_repr(self):
        result = repr(self.pfr_rmt_fmt)
        self.assertEqual(
            result,
            "PFR_RMT_FMT ( "
            "ORIG='IAD', "
            "ROUTE_STRING='IAD JDUBB4 RRSIN GSO Q83 ROYCO Q85 LPERD SNFLD3 MCO', "
            "DEST='MCO', "
            "HOURS1=None, "
            f"TYPE={PrefRouteTypeCode.HIGH_ALTITUDE!r}, "
            "AREA='FROM DCA,DAA,IAD,JYO,MRB,OKV TO ISM,MCO', "
            "ALTITUDE=None, "
            "AIRCRAFT=None, "
            "DIRECTION=None, "
            "SEQ=5, "
            "DCNTR='ZDC', "
            "ACNTR='ZJX'"
            " )",
        ),

    def test_ordered_fields(self):
        result = self.pfr_rmt_fmt.ordered_fields()
        self.assertListEqual(
            result,
            [
                "orig",
                "route_string",
                "dest",
                "hours1",
                "type",
                "area",
                "altitude",
                "aircraft",
                "direction",
                "seq",
                "dcntr",
                "acntr",
            ],
        )

    def test_to_dict(self):
        result = self.pfr_rmt_fmt.to_dict()
        self.assertDictEqual(
            result,
            {
                "orig": "IAD",
                "route_string": "IAD JDUBB4 RRSIN GSO Q83 ROYCO Q85 LPERD SNFLD3 MCO",
                "dest": "MCO",
                "hours1": None,
                "type": PrefRouteTypeCode.HIGH_ALTITUDE.value,
                "area": "FROM DCA,DAA,IAD,JYO,MRB,OKV TO ISM,MCO",
                "altitude": None,
                "aircraft": None,
                "direction": None,
                "seq": 5,
                "dcntr": "ZDC",
                "acntr": "ZJX",
            },
        )

    def test_to_str(self):
        result = self.pfr_rmt_fmt.to_str()
        self.assertEqual(
            result,
            "orig: IAD, "
            "route_string: IAD JDUBB4 RRSIN GSO Q83 ROYCO Q85 LPERD SNFLD3 MCO, "
            "dest: MCO, "
            "hours1: None, "
            "type: H, "
            "area: FROM DCA,DAA,IAD,JYO,MRB,OKV TO ISM,MCO, "
            "altitude: None, "
            "aircraft: None, "
            "direction: None, "
            "seq: 5, "
            "dcntr: ZDC, "
            "acntr: ZJX",
        )
