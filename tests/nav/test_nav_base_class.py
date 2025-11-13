from nasrparse.records.nav import NAV_BASE
from nasrparse.records.types import (
    HemisCode,
    MonitoringCode,
    PointCode,
    RegionCode,
    ServiceVolumeCode,
    SurveyAccuracyCode,
)

from datetime import date

import unittest


class TestNAV_BASE(unittest.TestCase):
    def setUp(self):
        self.maxDiff = None
        self.nav_base = NAV_BASE(
            "2025/10/30",
            "AML",
            "VOR/DME",
            "VA",
            "HERNDON",
            "US",
            "OPERATIONAL RESTRICTED",
            "ARMEL",
            "VIRGINIA",
            "AEA",
            "UNITED STATES",
            "",
            "F-FEDERAL AVIATION ADMIN",
            "F-FEDERAL AVIATION ADMIN",
            "Y",
            "Y",
            "",
            "24",
            "ZDC",
            "WASHINGTON",
            "ZDC",
            "WASHINGTON",
            "38",
            "56",
            "4.5329",
            "N",
            "38.93459247",
            "77",
            "28",
            "0.1263",
            "W",
            "-77.46670175",
            "6",
            "OPERATIONAL RESTRICTED",
            "38",
            "56",
            "4.5329",
            "N",
            "38.93459247",
            "77",
            "28",
            "0.1263",
            "W",
            "-77.46670175",
            "295.7",
            "8",
            "W",
            "1980",
            "N",
            "",
            "Y",
            "1",
            "NONE",
            "82X",
            "113.5",
            "",
            "",
            "",
            "L",
            "L",
            "Y",
            "",
            "DCA",
            "LEESBURG",
            "24",
            "IAD",
            "",
            "N",
            "N",
            "N",
            "",
            "",
        )

    def tearDown(self):
        pass

    def test_repr(self):
        result = repr(self.nav_base)
        self.assertEqual(
            result,
            "NAV_BASE ( "
            "EFF_DATE=datetime.date(2025, 10, 30), "
            "NAV_ID='AML', "
            f"NAV_TYPE={PointCode.VOR_DME!r}, "
            "STATE_CODE='VA', "
            "CITY='HERNDON', "
            "COUNTRY_CODE='US', "
            "NAV_STATUS='OPERATIONAL RESTRICTED', "
            "NAME='ARMEL', "
            "STATE_NAME='VIRGINIA', "
            f"REGION_CODE={RegionCode.EASTERN!r}, "
            "COUNTRY_NAME='UNITED STATES', "
            "FAN_MARKER=None, "
            "OWNER='F-FEDERAL AVIATION ADMIN', "
            "OPERATOR='F-FEDERAL AVIATION ADMIN', "
            "NAS_USE_FLAG=True, "
            "PUBLIC_USE_FLAG=True, "
            "NDB_CLASS_CODE=None, "
            "OPER_HOURS='24', "
            "HIGH_ALT_ARTCC_ID='ZDC', "
            "HIGH_ARTCC_NAME='WASHINGTON', "
            "LOW_ALT_ARTCC_ID='ZDC', "
            "LOW_ARTCC_NAME='WASHINGTON', "
            "LAT_DEG=38, "
            "LAT_MIN=56, "
            "LAT_SEC=4.5329, "
            f"LAT_HEMIS={HemisCode.NORTH!r}, "
            "LAT_DECIMAL=38.93459247, "
            "LON_DEG=77, "
            "LON_MIN=28, "
            "LON_SEC=0.1263, "
            f"LON_HEMIS={HemisCode.WEST!r}, "
            "LON_DECIMAL=-77.46670175, "
            f"SURVEY_ACCURACY_CODE={SurveyAccuracyCode.NOS!r}, "
            "TACAN_DME_STATUS='OPERATIONAL RESTRICTED', "
            "TACAN_DME_LAT_DEG=38, "
            "TACAN_DME_LAT_MIN=56, "
            "TACAN_DME_LAT_SEC=4.5329, "
            f"TACAN_DME_LAT_HEMIS={HemisCode.NORTH!r}, "
            "TACAN_DME_LAT_DECIMAL=38.93459247, "
            "TACAN_DME_LON_DEG=77, "
            "TACAN_DME_LON_MIN=28, "
            "TACAN_DME_LON_SEC=0.1263, "
            f"TACAN_DME_LON_HEMIS={HemisCode.WEST!r}, "
            "TACAN_DME_LON_DECIMAL=-77.46670175, "
            "ELEV=295.7, "
            "MAG_VARN=8, "
            f"MAG_VARN_HEMIS={HemisCode.WEST!r}, "
            "MAG_VARN_YEAR='1980', "
            "SIMUL_VOICE_FLAG=False, "
            "PWR_OUTPUT=None, "
            "AUTO_VOICE_ID_FLAG=True, "
            f"MNT_CAT_CODE={MonitoringCode.INTERNAL_PLUS_INDICATOR!r}, "
            "VOICE_CALL='NONE', "
            "CHAN='82X', "
            "FREQ='113.5', "
            "MKR_IDENT=None, "
            "MKR_SHAPE=None, "
            "MKR_BRG=None, "
            f"ALT_CODE={ServiceVolumeCode.LOW_ALTITUDE!r}, "
            f"DME_SSV={ServiceVolumeCode.LOW_ALTITUDE!r}, "
            "LOW_NAV_ON_HIGH_CHART_FLAG=True, "
            "Z_MKR_FLAG=None, "
            "FSS_ID='DCA', "
            "FSS_NAME='LEESBURG', "
            "FSS_HOURS='24', "
            "NOTAM_ID='IAD', "
            "QUAD_IDENT=None, "
            "PITCH_FLAG=False, "
            "CATCH_FLAG=False, "
            "SUA_ATCAA_FLAG=False, "
            "RESTRICTION_FLAG=None, "
            "HIWAS_FLAG=None"
            " )",
        ),

    def test_ordered_fields(self):
        result = self.nav_base.ordered_fields()
        self.assertListEqual(
            result,
            [
                "eff_date",
                "nav_id",
                "nav_type",
                "state_code",
                "city",
                "country_code",
                "nav_status",
                "name",
                "state_name",
                "region_code",
                "country_name",
                "fan_marker",
                "owner",
                "operator",
                "nas_use_flag",
                "public_use_flag",
                "ndb_class_code",
                "oper_hours",
                "high_alt_artcc_id",
                "high_artcc_name",
                "low_alt_artcc_id",
                "low_artcc_name",
                "lat_deg",
                "lat_min",
                "lat_sec",
                "lat_hemis",
                "lat_decimal",
                "lon_deg",
                "lon_min",
                "lon_sec",
                "lon_hemis",
                "lon_decimal",
                "survey_accuracy_code",
                "tacan_dme_status",
                "tacan_dme_lat_deg",
                "tacan_dme_lat_min",
                "tacan_dme_lat_sec",
                "tacan_dme_lat_hemis",
                "tacan_dme_lat_decimal",
                "tacan_dme_lon_deg",
                "tacan_dme_lon_min",
                "tacan_dme_lon_sec",
                "tacan_dme_lon_hemis",
                "tacan_dme_lon_decimal",
                "elev",
                "mag_varn",
                "mag_varn_hemis",
                "mag_varn_year",
                "simul_voice_flag",
                "pwr_output",
                "auto_voice_id_flag",
                "mnt_cat_code",
                "voice_call",
                "chan",
                "freq",
                "mkr_ident",
                "mkr_shape",
                "mkr_brg",
                "alt_code",
                "dme_ssv",
                "low_nav_on_high_chart_flag",
                "z_mkr_flag",
                "fss_id",
                "fss_name",
                "fss_hours",
                "notam_id",
                "quad_ident",
                "pitch_flag",
                "catch_flag",
                "sua_atcaa_flag",
                "restriction_flag",
                "hiwas_flag",
            ],
        )

    def test_to_dict(self):
        result = self.nav_base.to_dict()
        self.assertDictEqual(
            result,
            {
                "eff_date": date(2025, 10, 30).strftime("%Y-%m-%d"),
                "nav_id": "AML",
                "nav_type": PointCode.VOR_DME.value,
                "state_code": "VA",
                "city": "HERNDON",
                "country_code": "US",
                "nav_status": "OPERATIONAL RESTRICTED",
                "name": "ARMEL",
                "state_name": "VIRGINIA",
                "region_code": RegionCode.EASTERN.value,
                "country_name": "UNITED STATES",
                "fan_marker": None,
                "owner": "F-FEDERAL AVIATION ADMIN",
                "operator": "F-FEDERAL AVIATION ADMIN",
                "nas_use_flag": True,
                "public_use_flag": True,
                "ndb_class_code": None,
                "oper_hours": "24",
                "high_alt_artcc_id": "ZDC",
                "high_artcc_name": "WASHINGTON",
                "low_alt_artcc_id": "ZDC",
                "low_artcc_name": "WASHINGTON",
                "lat_deg": 38,
                "lat_min": 56,
                "lat_sec": 4.5329,
                "lat_hemis": HemisCode.NORTH.value,
                "lat_decimal": 38.93459247,
                "lon_deg": 77,
                "lon_min": 28,
                "lon_sec": 0.1263,
                "lon_hemis": HemisCode.WEST.value,
                "lon_decimal": -77.46670175,
                "survey_accuracy_code": SurveyAccuracyCode.NOS.value,
                "tacan_dme_status": "OPERATIONAL RESTRICTED",
                "tacan_dme_lat_deg": 38,
                "tacan_dme_lat_min": 56,
                "tacan_dme_lat_sec": 4.5329,
                "tacan_dme_lat_hemis": HemisCode.NORTH.value,
                "tacan_dme_lat_decimal": 38.93459247,
                "tacan_dme_lon_deg": 77,
                "tacan_dme_lon_min": 28,
                "tacan_dme_lon_sec": 0.1263,
                "tacan_dme_lon_hemis": HemisCode.WEST.value,
                "tacan_dme_lon_decimal": -77.46670175,
                "elev": 295.7,
                "mag_varn": 8,
                "mag_varn_hemis": HemisCode.WEST.value,
                "mag_varn_year": "1980",
                "simul_voice_flag": False,
                "pwr_output": None,
                "auto_voice_id_flag": True,
                "mnt_cat_code": MonitoringCode.INTERNAL_PLUS_INDICATOR.value,
                "voice_call": "NONE",
                "chan": "82X",
                "freq": "113.5",
                "mkr_ident": None,
                "mkr_shape": None,
                "mkr_brg": None,
                "alt_code": ServiceVolumeCode.LOW_ALTITUDE.value,
                "dme_ssv": ServiceVolumeCode.LOW_ALTITUDE.value,
                "low_nav_on_high_chart_flag": True,
                "z_mkr_flag": None,
                "fss_id": "DCA",
                "fss_name": "LEESBURG",
                "fss_hours": "24",
                "notam_id": "IAD",
                "quad_ident": None,
                "pitch_flag": False,
                "catch_flag": False,
                "sua_atcaa_flag": False,
                "restriction_flag": None,
                "hiwas_flag": None,
            },
        )

    def test_to_str(self):
        result = self.nav_base.to_str()
        self.assertEqual(
            result,
            "eff_date: 2025-10-30, "
            "nav_id: AML, "
            "nav_type: VOR/DME, "
            "state_code: VA, "
            "city: HERNDON, "
            "country_code: US, "
            "nav_status: OPERATIONAL RESTRICTED, "
            "name: ARMEL, "
            "state_name: VIRGINIA, "
            "region_code: AEA, "
            "country_name: UNITED STATES, "
            "fan_marker: None, "
            "owner: F-FEDERAL AVIATION ADMIN, "
            "operator: F-FEDERAL AVIATION ADMIN, "
            "nas_use_flag: True, "
            "public_use_flag: True, "
            "ndb_class_code: None, "
            "oper_hours: 24, "
            "high_alt_artcc_id: ZDC, "
            "high_artcc_name: WASHINGTON, "
            "low_alt_artcc_id: ZDC, "
            "low_artcc_name: WASHINGTON, "
            "lat_deg: 38, "
            "lat_min: 56, "
            "lat_sec: 4.5329, "
            "lat_hemis: N, "
            "lat_decimal: 38.93459247, "
            "lon_deg: 77, "
            "lon_min: 28, "
            "lon_sec: 0.1263, "
            "lon_hemis: W, "
            "lon_decimal: -77.46670175, "
            "survey_accuracy_code: 6, "
            "tacan_dme_status: OPERATIONAL RESTRICTED, "
            "tacan_dme_lat_deg: 38, "
            "tacan_dme_lat_min: 56, "
            "tacan_dme_lat_sec: 4.5329, "
            "tacan_dme_lat_hemis: N, "
            "tacan_dme_lat_decimal: 38.93459247, "
            "tacan_dme_lon_deg: 77, "
            "tacan_dme_lon_min: 28, "
            "tacan_dme_lon_sec: 0.1263, "
            "tacan_dme_lon_hemis: W, "
            "tacan_dme_lon_decimal: -77.46670175, "
            "elev: 295.7, "
            "mag_varn: 8, "
            "mag_varn_hemis: W, "
            "mag_varn_year: 1980, "
            "simul_voice_flag: False, "
            "pwr_output: None, "
            "auto_voice_id_flag: True, "
            "mnt_cat_code: 1, "
            "voice_call: NONE, "
            "chan: 82X, "
            "freq: 113.5, "
            "mkr_ident: None, "
            "mkr_shape: None, "
            "mkr_brg: None, "
            "alt_code: L, "
            "dme_ssv: L, "
            "low_nav_on_high_chart_flag: True, "
            "z_mkr_flag: None, "
            "fss_id: DCA, "
            "fss_name: LEESBURG, "
            "fss_hours: 24, "
            "notam_id: IAD, "
            "quad_ident: None, "
            "pitch_flag: False, "
            "catch_flag: False, "
            "sua_atcaa_flag: False, "
            "restriction_flag: None, "
            "hiwas_flag: None",
        )
