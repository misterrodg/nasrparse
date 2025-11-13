from nasrparse.records.lid import LID_BASE
from nasrparse.records.types import LIDGroupCode, RegionCode, SiteTypeCode

from datetime import date

import unittest


class TestLID_BASE(unittest.TestCase):
    def setUp(self):
        self.maxDiff = None
        self.lid_base = LID_BASE(
            "2025/10/30",
            "US",
            "JYO",
            "AEA",
            "VA",
            "LEESBURG",
            "LANDING FACILITY",
            "A",
            "LEESBURG EXEC",
            "ZDC",
            "ZCW",
            "DCA",
        )

    def tearDown(self):
        pass

    def test_repr(self):
        result = repr(self.lid_base)
        self.assertEqual(
            result,
            "LID_BASE ( "
            "EFF_DATE=datetime.date(2025, 10, 30), "
            "COUNTRY_CODE='US', "
            "LOC_ID='JYO', "
            f"REGION_CODE={RegionCode.EASTERN!r}, "
            "STATE_CODE='VA', "
            "CITY='LEESBURG', "
            f"LID_GROUP={LIDGroupCode.LANDING_FACILITY!r}, "
            f"FAC_TYPE={SiteTypeCode.AIRPORT!r}, "
            "FAC_NAME='LEESBURG EXEC', "
            "RESP_ARTCC_ID='ZDC', "
            "ARTCC_COMPUTER_ID='ZCW', "
            "FSS_ID='DCA'"
            " )",
        ),

    def test_ordered_fields(self):
        result = self.lid_base.ordered_fields()
        self.assertListEqual(
            result,
            [
                "eff_date",
                "country_code",
                "loc_id",
                "region_code",
                "state_code",
                "city",
                "lid_group",
                "fac_type",
                "fac_name",
                "resp_artcc_id",
                "artcc_computer_id",
                "fss_id",
            ],
        )

    def test_to_dict(self):
        result = self.lid_base.to_dict()
        self.assertDictEqual(
            result,
            {
                "eff_date": date(2025, 10, 30).strftime("%Y-%m-%d"),
                "country_code": "US",
                "loc_id": "JYO",
                "region_code": RegionCode.EASTERN.value,
                "state_code": "VA",
                "city": "LEESBURG",
                "lid_group": LIDGroupCode.LANDING_FACILITY.value,
                "fac_type": SiteTypeCode.AIRPORT.value,
                "fac_name": "LEESBURG EXEC",
                "resp_artcc_id": "ZDC",
                "artcc_computer_id": "ZCW",
                "fss_id": "DCA",
            },
        )

    def test_to_str(self):
        result = self.lid_base.to_str()
        self.assertEqual(
            result,
            "eff_date: 2025-10-30, "
            "country_code: US, "
            "loc_id: JYO, "
            "region_code: AEA, "
            "state_code: VA, "
            "city: LEESBURG, "
            "lid_group: LANDING FACILITY, "
            "fac_type: A, "
            "fac_name: LEESBURG EXEC, "
            "resp_artcc_id: ZDC, "
            "artcc_computer_id: ZCW, "
            "fss_id: DCA",
        )
