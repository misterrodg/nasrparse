from nasrparse.records.frq import FRQ_BASE
from nasrparse.records.types import SiteTypeCode

from datetime import date

import unittest


class TestFRQ_BASE(unittest.TestCase):
    def setUp(self):
        self.maxDiff = None
        self.frq_base = FRQ_BASE(
            "2025/10/30",
            "JYO",
            "LEESBURG EXEC",
            "ATCT",
            "",
            "",
            "1300-2300Z++",
            "JYO",
            "LEESBURG EXEC",
            "AIRPORT",
            "39.07797222",
            "-77.5575",
            "LEESBURG",
            "VA",
            "US",
            "LEESBURG TOWER",
            "POTOMAC",
            "127.5",
            "",
            "LCL/P",
            "",
        )

    def tearDown(self):
        pass

    def test_repr(self):
        result = repr(self.frq_base)
        self.assertEqual(
            result,
            "FRQ_BASE ( "
            "EFF_DATE=datetime.date(2025, 10, 30), "
            "FACILITY='JYO', "
            "FAC_NAME='LEESBURG EXEC', "
            "FACILITY_TYPE='ATCT', "
            "ARTCC_OR_FSS_ID=None, "
            "CPDLC=None, "
            "TOWER_HRS='1300-2300Z++', "
            "SERVICED_FACILITY='JYO', "
            "SERVICED_FAC_NAME='LEESBURG EXEC', "
            "SERVICED_SITE_TYPE='AIRPORT', "
            "LAT_DECIMAL=39.07797222, "
            "LON_DECIMAL=-77.5575, "
            "SERVICED_CITY='LEESBURG', "
            "SERVICED_STATE='VA', "
            "SERVICED_COUNTRY='US', "
            "TOWER_OR_COMM_CALL='LEESBURG TOWER', "
            "PRIMARY_APPROACH_RADIO_CALL='POTOMAC', "
            "FREQ='127.5', "
            "SECTORIZATION=None, "
            "FREQ_USE='LCL/P', "
            "REMARK=None"
            " )",
        ),

    def test_ordered_fields(self):
        result = self.frq_base.ordered_fields()
        self.assertListEqual(
            result,
            [
                "eff_date",
                "facility",
                "fac_name",
                "facility_type",
                "artcc_or_fss_id",
                "cpdlc",
                "tower_hrs",
                "serviced_facility",
                "serviced_fac_name",
                "serviced_site_type",
                "lat_decimal",
                "lon_decimal",
                "serviced_city",
                "serviced_state",
                "serviced_country",
                "tower_or_comm_call",
                "primary_approach_radio_call",
                "freq",
                "sectorization",
                "freq_use",
                "remark",
            ],
        )

    def test_to_dict(self):
        result = self.frq_base.to_dict()
        self.assertDictEqual(
            result,
            {
                "eff_date": date(2025, 10, 30).strftime("%Y-%m-%d"),
                "facility": "JYO",
                "fac_name": "LEESBURG EXEC",
                "facility_type": "ATCT",
                "artcc_or_fss_id": None,
                "cpdlc": None,
                "tower_hrs": "1300-2300Z++",
                "serviced_facility": "JYO",
                "serviced_fac_name": "LEESBURG EXEC",
                "serviced_site_type": "AIRPORT",
                "lat_decimal": 39.07797222,
                "lon_decimal": -77.5575,
                "serviced_city": "LEESBURG",
                "serviced_state": "VA",
                "serviced_country": "US",
                "tower_or_comm_call": "LEESBURG TOWER",
                "primary_approach_radio_call": "POTOMAC",
                "freq": "127.5",
                "sectorization": None,
                "freq_use": "LCL/P",
                "remark": None,
            },
        )

    def test_to_str(self):
        result = self.frq_base.to_str()
        self.assertEqual(
            result,
            "eff_date: 2025-10-30, "
            "facility: JYO, "
            "fac_name: LEESBURG EXEC, "
            "facility_type: ATCT, "
            "artcc_or_fss_id: None, "
            "cpdlc: None, "
            "tower_hrs: 1300-2300Z++, "
            "serviced_facility: JYO, "
            "serviced_fac_name: LEESBURG EXEC, "
            "serviced_site_type: AIRPORT, "
            "lat_decimal: 39.07797222, "
            "lon_decimal: -77.5575, "
            "serviced_city: LEESBURG, "
            "serviced_state: VA, "
            "serviced_country: US, "
            "tower_or_comm_call: LEESBURG TOWER, "
            "primary_approach_radio_call: POTOMAC, "
            "freq: 127.5, "
            "sectorization: None, "
            "freq_use: LCL/P, "
            "remark: None",
        )
