from nasrparse.records.awy import AWY_ALT
from nasrparse.records.types import AirwayLocationCode, PointCode

from datetime import date

import unittest


class TestAWY_ALT(unittest.TestCase):
    def setUp(self):
        self.maxDiff = None
        self.awy_alt = AWY_ALT(
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
            "EYTEE",
            "31000",
            "",
            "",
            "",
            "18000",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "41000",
            "",
            "",
            "",
        )

    def tearDown(self):
        pass

    def test_repr(self):
        result = repr(self.awy_alt)
        self.assertEqual(
            result,
            "AWY_ALT ( "
            "EFF_DATE=datetime.date(2023, 10, 5), "
            "REGULATORY=True, "
            f"AWY_LOCATION={AirwayLocationCode.CONTIGUOUS_US!r}, "
            "AWY_ID='J149', "
            "POINT_SEQ=10, "
            "MEA_PT='AML', "
            f"MEA_PT_TYPE={PointCode.VOR_DME!r}, "
            "NAV_NAME='ARMEL', "
            "NAV_CITY='HERNDON', "
            "ICAO_REGION_CODE=None, "
            "STATE_CODE='VA', "
            "COUNTRY_CODE='US', "
            "NEXT_MEA_PT='EYTEE', "
            "MIN_ENROUTE_ALT=31000, "
            "MIN_ENROUTE_ALT_DIR=None, "
            "MIN_ENROUTE_ALT_OPPOSITE=None, "
            "MIN_ENROUTE_ALT_OPPOSITE_DIR=None, "
            "GPS_MIN_ENROUTE_ALT=18000, "
            "GPS_MIN_ENROUTE_ALT_DIR=None, "
            "GPS_MIN_ENROUTE_ALT_OPPOSITE=None, "
            "GPS_MEA_OPPOSITE_DIR=None, "
            "DD_IRU_MEA=None, "
            "DD_IRU_MEA_DIR=None, "
            "DD_I_MEA_OPPOSITE=None, "
            "DD_I_MEA_OPPOSITE_DIR=None, "
            "MIN_OBSTN_CLNC_ALT=None, "
            "MIN_CROSS_ALT=None, "
            "MIN_CROSS_ALT_DIR=None, "
            "MIN_CROSS_ALT_NAV_PT=None, "
            "MIN_CROSS_ALT_OPPOSITE=None, "
            "MIN_CROSS_ALT_OPPOSITE_DIR=None, "
            "MIN_RECEP_ALT=None, "
            "MAX_AUTH_ALT=41000, "
            "MEA_GAP=None, "
            "REQD_NAV_PERFORMANCE=None, "
            "REMARK=None"
            " )",
        ),

    def test_ordered_fields(self):
        result = self.awy_alt.ordered_fields()
        self.assertListEqual(
            result,
            [
                "eff_date",
                "regulatory",
                "awy_location",
                "awy_id",
                "point_seq",
                "mea_pt",
                "mea_pt_type",
                "nav_name",
                "nav_city",
                "icao_region_code",
                "state_code",
                "country_code",
                "next_mea_pt",
                "min_enroute_alt",
                "min_enroute_alt_dir",
                "min_enroute_alt_opposite",
                "min_enroute_alt_opposite_dir",
                "gps_min_enroute_alt",
                "gps_min_enroute_alt_dir",
                "gps_min_enroute_alt_opposite",
                "gps_mea_opposite_dir",
                "dd_iru_mea",
                "dd_iru_mea_dir",
                "dd_i_mea_opposite",
                "dd_i_mea_opposite_dir",
                "min_obstn_clnc_alt",
                "min_cross_alt",
                "min_cross_alt_dir",
                "min_cross_alt_nav_pt",
                "min_cross_alt_opposite",
                "min_cross_alt_opposite_dir",
                "min_recep_alt",
                "max_auth_alt",
                "mea_gap",
                "reqd_nav_performance",
                "remark",
            ],
        )

    def test_to_dict(self):
        result = self.awy_alt.to_dict()
        self.assertDictEqual(
            result,
            {
                "eff_date": date(2023, 10, 5).strftime("%Y-%m-%d"),
                "regulatory": True,
                "awy_location": AirwayLocationCode.CONTIGUOUS_US.value,
                "awy_id": "J149",
                "point_seq": 10,
                "mea_pt": "AML",
                "mea_pt_type": PointCode.VOR_DME.value,
                "nav_name": "ARMEL",
                "nav_city": "HERNDON",
                "icao_region_code": None,
                "state_code": "VA",
                "country_code": "US",
                "next_mea_pt": "EYTEE",
                "min_enroute_alt": 31000,
                "min_enroute_alt_dir": None,
                "min_enroute_alt_opposite": None,
                "min_enroute_alt_opposite_dir": None,
                "gps_min_enroute_alt": 18000,
                "gps_min_enroute_alt_dir": None,
                "gps_min_enroute_alt_opposite": None,
                "gps_mea_opposite_dir": None,
                "dd_iru_mea": None,
                "dd_iru_mea_dir": None,
                "dd_i_mea_opposite": None,
                "dd_i_mea_opposite_dir": None,
                "min_obstn_clnc_alt": None,
                "min_cross_alt": None,
                "min_cross_alt_dir": None,
                "min_cross_alt_nav_pt": None,
                "min_cross_alt_opposite": None,
                "min_cross_alt_opposite_dir": None,
                "min_recep_alt": None,
                "max_auth_alt": 41000,
                "mea_gap": None,
                "reqd_nav_performance": None,
                "remark": None,
            },
        )

    def test_to_str(self):
        result = self.awy_alt.to_str()
        self.assertEqual(
            result,
            "eff_date: 2023-10-05, "
            "regulatory: True, "
            "awy_location: C, "
            "awy_id: J149, "
            "point_seq: 10, "
            "mea_pt: AML, "
            "mea_pt_type: VOR/DME, "
            "nav_name: ARMEL, "
            "nav_city: HERNDON, "
            "icao_region_code: None, "
            "state_code: VA, "
            "country_code: US, "
            "next_mea_pt: EYTEE, "
            "min_enroute_alt: 31000, "
            "min_enroute_alt_dir: None, "
            "min_enroute_alt_opposite: None, "
            "min_enroute_alt_opposite_dir: None, "
            "gps_min_enroute_alt: 18000, "
            "gps_min_enroute_alt_dir: None, "
            "gps_min_enroute_alt_opposite: None, "
            "gps_mea_opposite_dir: None, "
            "dd_iru_mea: None, "
            "dd_iru_mea_dir: None, "
            "dd_i_mea_opposite: None, "
            "dd_i_mea_opposite_dir: None, "
            "min_obstn_clnc_alt: None, "
            "min_cross_alt: None, "
            "min_cross_alt_dir: None, "
            "min_cross_alt_nav_pt: None, "
            "min_cross_alt_opposite: None, "
            "min_cross_alt_opposite_dir: None, "
            "min_recep_alt: None, "
            "max_auth_alt: 41000, "
            "mea_gap: None, "
            "reqd_nav_performance: None, "
            "remark: None",
        )
