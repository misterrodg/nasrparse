from nasrparse.records.pja import PJA_CON

from datetime import date

import unittest


class TestPJA_CON(unittest.TestCase):
    def setUp(self):
        self.maxDiff = None
        self.pja_con = PJA_CON(
            "2025/10/02",
            "PVA019",
            "PCT",
            "POTOMAC TRACON",
            "PCT",
            "126.8",
            "Y",
            "307.2",
            "N",
            "",
            "",
        )

    def tearDown(self):
        pass

    def test_repr(self):
        result = repr(self.pja_con)
        self.assertEqual(
            result,
            "PJA_CON ( "
            "EFF_DATE=datetime.date(2025, 10, 2), "
            "PJA_ID='PVA019', "
            "FAC_ID='PCT', "
            "FAC_NAME='POTOMAC TRACON', "
            "LOC_ID='PCT', "
            "COMMERCIAL_FREQ='126.8', "
            "COMMERCIAL_CHART_FLAG=True, "
            "MIL_FREQ='307.2', "
            "MIL_CHART_FLAG=False, "
            "SECTOR=None, "
            "CONTACT_FREQ_ALTITUDE=None"
            " )",
        ),

    def test_ordered_fields(self):
        result = self.pja_con.ordered_fields()
        self.assertListEqual(
            result,
            [
                "eff_date",
                "pja_id",
                "fac_id",
                "fac_name",
                "loc_id",
                "commercial_freq",
                "commercial_chart_flag",
                "mil_freq",
                "mil_chart_flag",
                "sector",
                "contact_freq_altitude",
            ],
        )

    def test_to_dict(self):
        result = self.pja_con.to_dict()
        self.assertDictEqual(
            result,
            {
                "eff_date": date(2025, 10, 2).strftime("%Y-%m-%d"),
                "pja_id": "PVA019",
                "fac_id": "PCT",
                "fac_name": "POTOMAC TRACON",
                "loc_id": "PCT",
                "commercial_freq": "126.8",
                "commercial_chart_flag": True,
                "mil_freq": "307.2",
                "mil_chart_flag": False,
                "sector": None,
                "contact_freq_altitude": None,
            },
        )

    def test_to_str(self):
        result = self.pja_con.to_str()
        self.assertEqual(
            result,
            "eff_date: 2025-10-02, "
            "pja_id: PVA019, "
            "fac_id: PCT, "
            "fac_name: POTOMAC TRACON, "
            "loc_id: PCT, "
            "commercial_freq: 126.8, "
            "commercial_chart_flag: True, "
            "mil_freq: 307.2, "
            "mil_chart_flag: False, "
            "sector: None, "
            "contact_freq_altitude: None",
        )
