from nasrparse.records.cdr import CDR_BASE
from nasrparse.records.types import NavigationEquipmentCode

import unittest


class TestCDR_BASE(unittest.TestCase):
    def setUp(self):
        self.maxDiff = None
        self.cdr_base = CDR_BASE(
            "ATLIADSK",
            "KATL",
            "KIAD",
            "BOBBD",
            "KATL SMKEY2 BOBBD Q71 ATUME JARLO GIBBZ5 KIAD",
            "ZTL",
            "ZDC",
            "ZDC ZID ZTL",
            "Y",
            "",
            "2",
            "564",
        )

    def tearDown(self):
        pass

    def test_repr(self):
        result = repr(self.cdr_base)
        self.assertEqual(
            result,
            "CDR_BASE ( "
            "RCODE='ATLIADSK', "
            "ORIG='KATL', "
            "DEST='KIAD', "
            "DEPFIX='BOBBD', "
            "ROUTE_STRING='KATL SMKEY2 BOBBD Q71 ATUME JARLO GIBBZ5 KIAD', "
            "DCNTR='ZTL', "
            "ACNTR='ZDC', "
            "TCNTRS='ZDC ZID ZTL', "
            "COORDREQ=True, "
            "PLAY=None, "
            f"NAVEQP={NavigationEquipmentCode.RNAV_PROCEDURES!r}, "
            "LENGTH=564"
            " )",
        ),

    def test_ordered_fields(self):
        result = self.cdr_base.ordered_fields()
        self.assertListEqual(
            result,
            [
                "rcode",
                "orig",
                "dest",
                "depfix",
                "route_string",
                "dcntr",
                "acntr",
                "tcntrs",
                "coordreq",
                "play",
                "naveqp",
                "length",
            ],
        )

    def test_to_dict(self):
        result = self.cdr_base.to_dict()
        self.assertDictEqual(
            result,
            {
                "rcode": "ATLIADSK",
                "orig": "KATL",
                "dest": "KIAD",
                "depfix": "BOBBD",
                "route_string": "KATL SMKEY2 BOBBD Q71 ATUME JARLO GIBBZ5 KIAD",
                "dcntr": "ZTL",
                "acntr": "ZDC",
                "tcntrs": "ZDC ZID ZTL",
                "coordreq": True,
                "play": None,
                "naveqp": NavigationEquipmentCode.RNAV_PROCEDURES.value,
                "length": 564,
            },
        )

    def test_to_str(self):
        result = self.cdr_base.to_str()
        self.assertEqual(
            result,
            "rcode: ATLIADSK, "
            "orig: KATL, "
            "dest: KIAD, "
            "depfix: BOBBD, "
            "route_string: KATL SMKEY2 BOBBD Q71 ATUME JARLO GIBBZ5 KIAD, "
            "dcntr: ZTL, "
            "acntr: ZDC, "
            "tcntrs: ZDC ZID ZTL, "
            "coordreq: True, "
            "play: None, "
            "naveqp: 2, "
            "length: 564",
        )
