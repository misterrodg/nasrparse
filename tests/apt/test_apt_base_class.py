from nasrparse.records.apt import APT_BASE
from nasrparse.records.types import (
    ASPCode,
    BeaconColorCode,
    DirectionCode,
    HemisCode,
    InspectionMethodCode,
    InspectorCode,
    LightScheduleCode,
    MagVarCode,
    MethodCode,
    NASPCode,
    OwnershipCode,
    OxygenCode,
    RegionCode,
    SegmentedCircleCode,
    SERCode,
    SiteTypeCode,
    StatusCode,
    TowerCode,
    UseCode,
    WindIndicatorCode,
)

from datetime import date

import unittest


class TestAPT_BASE(unittest.TestCase):
    def setUp(self):
        self.maxDiff = None
        self.apt_base = APT_BASE(
            "2025/10/30",
            "00103.",
            "A",
            "AL",
            "0J0",
            "ABBEVILLE",
            "US",
            "ASO",
            "JAN",
            "ALABAMA",
            "HENRY",
            "AL",
            "ABBEVILLE MUNI",
            "PU",
            "PU",
            "31",
            "36",
            "6.193",
            "N",
            "31.60172027",
            "85",
            "14",
            "18.761",
            "W",
            "-85.23854472",
            "E",
            "468.3",
            "E",
            "1",
            "W",
            "1985",
            "",
            "NEW ORLEANS",
            "3",
            "N",
            "36",
            "ZJX",
            "ZCJ",
            "JACKSONVILLE",
            "N",
            "ANB",
            "ANNISTON",
            "",
            "1-800-WX-BRIEF",
            "",
            "",
            "",
            "ANB",
            "Y",
            "1959/08",
            "O",
            "",
            "",
            "",
            "N",
            "NOT ANALYZED",
            "",
            "",
            "",
            "",
            "S",
            "S",
            "2023/05/26",
            "",
            "",
            "NONE",
            "NONE",
            "",
            "",
            "SEE RMK",
            "SS-SR",
            "NON-ATCT",
            "N",
            "WG",
            "N",
            "",
            "3RD PARTY SURVEY",
            "2025/06/17",
            "3RD PARTY SURVEY",
            "2025/06/17",
            "",
            "",
            "",
            "Y",
            "",
            "Y-L",
            "",
            "N",
            "",
            "",
        )

    def tearDown(self):
        pass

    def test_repr(self):
        result = repr(self.apt_base)
        self.assertEqual(
            result,
            "APT_BASE ( "
            "EFF_DATE=datetime.date(2025, 10, 30), "
            "SITE_NO='00103.', "
            f"SITE_TYPE_CODE={SiteTypeCode.AIRPORT!r}, "
            "STATE_CODE='AL', "
            "ARPT_ID='0J0', "
            "CITY='ABBEVILLE', "
            "COUNTRY_CODE='US', "
            f"REGION_CODE={RegionCode.SOUTHERN!r}, "
            "ADO_CODE='JAN', "
            "STATE_NAME='ALABAMA', "
            "COUNTY_NAME='HENRY', "
            "COUNTY_ASSOC_STATE='AL', "
            "ARPT_NAME='ABBEVILLE MUNI', "
            f"OWNERSHIP_TYPE_CODE={OwnershipCode.PUBLIC!r}, "
            f"FACILITY_USE_CODE={UseCode.PUBLIC!r}, "
            "LAT_DEG=31, "
            "LAT_MIN=36, "
            "LAT_SEC=6.193, "
            f"LAT_HEMIS={HemisCode.NORTH!r}, "
            "LAT_DECIMAL=31.60172027, "
            "LON_DEG=85, "
            "LON_MIN=14, "
            "LON_SEC=18.761, "
            f"LON_HEMIS={HemisCode.WEST!r}, "
            "LON_DECIMAL=-85.23854472, "
            f"SURVEY_METHOD_CODE={MethodCode.ESTIMATED!r}, "
            "ELEV=468.3, "
            f"ELEV_METHOD_CODE={MethodCode.ESTIMATED!r}, "
            "MAG_VARN=1, "
            f"MAG_HEMIS={MagVarCode.WEST!r}, "
            "MAG_VARN_YEAR=1985, "
            "TPA=None, "
            "CHART_NAME='NEW ORLEANS', "
            "DIST_CITY_TO_AIRPORT=3, "
            f"DIRECTION_CODE={DirectionCode.NORTH!r}, "
            "ACREAGE=36, "
            "RESP_ARTCC_ID='ZJX', "
            "COMPUTER_ID='ZCJ', "
            "ARTCC_NAME='JACKSONVILLE', "
            "FSS_ON_ARPT_FLAG=False, "
            "FSS_ID='ANB', "
            "FSS_NAME='ANNISTON', "
            "PHONE_NO=None, "
            "TOLL_FREE_NO='1-800-WX-BRIEF', "
            "ALT_FSS_ID=None, "
            "ALT_FSS_NAME=None, "
            "ALT_TOLL_FREE_NO=None, "
            "NOTAM_ID='ANB', "
            "NOTAM_FLAG=True, "
            "ACTIVATION_DATE=datetime.date(1959, 8, 1), "
            f"ARPT_STATUS={StatusCode.OPERATIONAL!r}, "
            "FAR_139_TYPE_CODE=None, "
            "FAR_139_CARRIER_SER_CODE=None, "
            "ARFF_CERT_TYPE_DATE=None, "
            "NASP_CODE=<NASPCode.NPIAS: 'N'>, "
            f"ASP_ANLYS_DTRM_CODE={ASPCode.NOT_ANALYZED!r}, "
            "CUST_FLAG=None, "
            "LNDG_RIGHTS_FLAG=None, "
            "JOINT_USE_FLAG=None, "
            "MIL_LNDG_FLAG=None, "
            f"INSPECT_METHOD_CODE={InspectionMethodCode.STATE!r}, "
            f"INSPECTOR_CODE={InspectorCode.STATE_PERSONNEL!r}, "
            "LAST_INSPECTION=datetime.date(2023, 5, 26), "
            "LAST_INFO_RESPONSE=None, "
            "FUEL_TYPES=[], "
            f"AIRFRAME_REPAIR_SER_CODE={SERCode.NONE!r}, "
            f"PWR_PLANT_REPAIR_SER={SERCode.NONE!r}, "
            f"BOTTLED_OXY_TYPE={OxygenCode.NULL!r}, "
            f"BULK_OXY_TYPE={OxygenCode.NULL!r}, "
            f"LGT_SKED={LightScheduleCode.SEE_RMK!r}, "
            f"BCN_LGT_SKED={LightScheduleCode.SS_SR!r}, "
            f"TWR_TYPE_CODE={TowerCode.NON_ATCT!r}, "
            f"SEG_CIRCLE_MKR_FLAG={SegmentedCircleCode.NO!r}, "
            f"BCN_LENS_COLOR={BeaconColorCode.WHITE_GREEN!r}, "
            "LNDG_FEE_FLAG=False, "
            "MEDICAL_USE_FLAG=None, "
            "ARPT_PSN_SOURCE='3RD PARTY SURVEY', "
            "POSITION_SRC_DATE=datetime.date(2025, 6, 17), "
            "ARPT_ELEV_SOURCE='3RD PARTY SURVEY', "
            "ELEVATION_SRC_DATE=datetime.date(2025, 6, 17), "
            "CONTR_FUEL_AVBL=None, "
            "TRNS_STRG_BUOY_FLAG=None, "
            "TRNS_STRG_HGR_FLAG=None, "
            "TRNS_STRG_TIE_FLAG=True, "
            "OTHER_SERVICES=[], "
            f"WIND_INDCR_FLAG={WindIndicatorCode.LIGHTED!r}, "
            "ICAO_ID=None, "
            "MIN_OP_NETWORK=False, "
            "USER_FEE_FLAG=None, "
            "CTA=None"
            " )",
        ),

    def test_ordered_fields(self):
        result = self.apt_base.ordered_fields()
        self.assertListEqual(
            result,
            [
                "eff_date",
                "site_no",
                "site_type_code",
                "state_code",
                "arpt_id",
                "city",
                "country_code",
                "region_code",
                "ado_code",
                "state_name",
                "county_name",
                "county_assoc_state",
                "arpt_name",
                "ownership_type_code",
                "facility_use_code",
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
                "survey_method_code",
                "elev",
                "elev_method_code",
                "mag_varn",
                "mag_hemis",
                "mag_varn_year",
                "tpa",
                "chart_name",
                "dist_city_to_airport",
                "direction_code",
                "acreage",
                "resp_artcc_id",
                "computer_id",
                "artcc_name",
                "fss_on_arpt_flag",
                "fss_id",
                "fss_name",
                "phone_no",
                "toll_free_no",
                "alt_fss_id",
                "alt_fss_name",
                "alt_toll_free_no",
                "notam_id",
                "notam_flag",
                "activation_date",
                "arpt_status",
                "far_139_type_code",
                "far_139_carrier_ser_code",
                "arff_cert_type_date",
                "nasp_code",
                "asp_anlys_dtrm_code",
                "cust_flag",
                "lndg_rights_flag",
                "joint_use_flag",
                "mil_lndg_flag",
                "inspect_method_code",
                "inspector_code",
                "last_inspection",
                "last_info_response",
                "fuel_types",
                "airframe_repair_ser_code",
                "pwr_plant_repair_ser",
                "bottled_oxy_type",
                "bulk_oxy_type",
                "lgt_sked",
                "bcn_lgt_sked",
                "twr_type_code",
                "seg_circle_mkr_flag",
                "bcn_lens_color",
                "lndg_fee_flag",
                "medical_use_flag",
                "arpt_psn_source",
                "position_src_date",
                "arpt_elev_source",
                "elevation_src_date",
                "contr_fuel_avbl",
                "trns_strg_buoy_flag",
                "trns_strg_hgr_flag",
                "trns_strg_tie_flag",
                "other_services",
                "wind_indcr_flag",
                "icao_id",
                "min_op_network",
                "user_fee_flag",
                "cta",
            ],
        )

    def test_to_dict(self):
        result = self.apt_base.to_dict()
        self.assertDictEqual(
            result,
            {
                "eff_date": date(2025, 10, 30).strftime("%Y-%m-%d"),
                "site_no": "00103.",
                "site_type_code": SiteTypeCode.AIRPORT.value,
                "state_code": "AL",
                "arpt_id": "0J0",
                "city": "ABBEVILLE",
                "country_code": "US",
                "region_code": "ASO",
                "ado_code": "JAN",
                "state_name": "ALABAMA",
                "county_name": "HENRY",
                "county_assoc_state": "AL",
                "arpt_name": "ABBEVILLE MUNI",
                "ownership_type_code": OwnershipCode.PUBLIC.value,
                "facility_use_code": UseCode.PUBLIC.value,
                "lat_deg": 31,
                "lat_min": 36,
                "lat_sec": 6.193,
                "lat_hemis": HemisCode.NORTH.value,
                "lat_decimal": 31.60172027,
                "lon_deg": 85,
                "lon_min": 14,
                "lon_sec": 18.761,
                "lon_hemis": HemisCode.WEST.value,
                "lon_decimal": -85.23854472,
                "survey_method_code": MethodCode.ESTIMATED.value,
                "elev": 468.3,
                "elev_method_code": MethodCode.ESTIMATED.value,
                "mag_varn": 1,
                "mag_hemis": MagVarCode.WEST.value,
                "mag_varn_year": 1985,
                "tpa": None,
                "chart_name": "NEW ORLEANS",
                "dist_city_to_airport": 3,
                "direction_code": DirectionCode.NORTH.value,
                "acreage": 36,
                "resp_artcc_id": "ZJX",
                "computer_id": "ZCJ",
                "artcc_name": "JACKSONVILLE",
                "fss_on_arpt_flag": False,
                "fss_id": "ANB",
                "fss_name": "ANNISTON",
                "phone_no": None,
                "toll_free_no": "1-800-WX-BRIEF",
                "alt_fss_id": None,
                "alt_fss_name": None,
                "alt_toll_free_no": None,
                "notam_id": "ANB",
                "notam_flag": True,
                "activation_date": date(1959, 8, 1).strftime("%Y-%m-%d"),
                "arpt_status": StatusCode.OPERATIONAL.value,
                "far_139_type_code": None,
                "far_139_carrier_ser_code": None,
                "arff_cert_type_date": None,
                "nasp_code": NASPCode.NPIAS.value,
                "asp_anlys_dtrm_code": ASPCode.NOT_ANALYZED.value,
                "cust_flag": None,
                "lndg_rights_flag": None,
                "joint_use_flag": None,
                "mil_lndg_flag": None,
                "inspect_method_code": InspectionMethodCode.STATE.value,
                "inspector_code": InspectorCode.STATE_PERSONNEL.value,
                "last_inspection": date(2023, 5, 26).strftime("%Y-%m-%d"),
                "last_info_response": None,
                "fuel_types": None,
                "airframe_repair_ser_code": SERCode.NONE.value,
                "pwr_plant_repair_ser": SERCode.NONE.value,
                "bottled_oxy_type": OxygenCode.NULL.value,
                "bulk_oxy_type": OxygenCode.NULL.value,
                "lgt_sked": LightScheduleCode.SEE_RMK.value,
                "bcn_lgt_sked": LightScheduleCode.SS_SR.value,
                "twr_type_code": TowerCode.NON_ATCT.value,
                "seg_circle_mkr_flag": SegmentedCircleCode.NO.value,
                "bcn_lens_color": BeaconColorCode.WHITE_GREEN.value,
                "lndg_fee_flag": False,
                "medical_use_flag": None,
                "arpt_psn_source": "3RD PARTY SURVEY",
                "position_src_date": date(2025, 6, 17).strftime("%Y-%m-%d"),
                "arpt_elev_source": "3RD PARTY SURVEY",
                "elevation_src_date": date(2025, 6, 17).strftime("%Y-%m-%d"),
                "contr_fuel_avbl": None,
                "trns_strg_buoy_flag": None,
                "trns_strg_hgr_flag": None,
                "trns_strg_tie_flag": True,
                "other_services": None,
                "wind_indcr_flag": WindIndicatorCode.LIGHTED.value,
                "icao_id": None,
                "min_op_network": False,
                "user_fee_flag": None,
                "cta": None,
            },
        )

    def test_to_str(self):
        result = self.apt_base.to_str()
        self.assertEqual(
            result,
            "eff_date: 2025-10-30, "
            "site_no: 00103., "
            "site_type_code: A, "
            "state_code: AL, "
            "arpt_id: 0J0, "
            "city: ABBEVILLE, "
            "country_code: US, "
            "region_code: ASO, "
            "ado_code: JAN, "
            "state_name: ALABAMA, "
            "county_name: HENRY, "
            "county_assoc_state: AL, "
            "arpt_name: ABBEVILLE MUNI, "
            "ownership_type_code: PU, "
            "facility_use_code: PU, "
            "lat_deg: 31, "
            "lat_min: 36, "
            "lat_sec: 6.193, "
            "lat_hemis: N, "
            "lat_decimal: 31.60172027, "
            "lon_deg: 85, "
            "lon_min: 14, "
            "lon_sec: 18.761, "
            "lon_hemis: W, "
            "lon_decimal: -85.23854472, "
            "survey_method_code: E, "
            "elev: 468.3, "
            "elev_method_code: E, "
            "mag_varn: 1, "
            "mag_hemis: W, "
            "mag_varn_year: 1985, "
            "tpa: None, "
            "chart_name: NEW ORLEANS, "
            "dist_city_to_airport: 3, "
            "direction_code: N, "
            "acreage: 36, "
            "resp_artcc_id: ZJX, "
            "computer_id: ZCJ, "
            "artcc_name: JACKSONVILLE, "
            "fss_on_arpt_flag: False, "
            "fss_id: ANB, "
            "fss_name: ANNISTON, "
            "phone_no: None, "
            "toll_free_no: 1-800-WX-BRIEF, "
            "alt_fss_id: None, "
            "alt_fss_name: None, "
            "alt_toll_free_no: None, "
            "notam_id: ANB, "
            "notam_flag: True, "
            "activation_date: 1959-08-01, "
            "arpt_status: O, "
            "far_139_type_code: None, "
            "far_139_carrier_ser_code: None, "
            "arff_cert_type_date: None, "
            "nasp_code: N, "
            "asp_anlys_dtrm_code: NOT ANALYZED, "
            "cust_flag: None, "
            "lndg_rights_flag: None, "
            "joint_use_flag: None, "
            "mil_lndg_flag: None, "
            "inspect_method_code: S, "
            "inspector_code: S, "
            "last_inspection: 2023-05-26, "
            "last_info_response: None, "
            "fuel_types: None, "
            "airframe_repair_ser_code: NONE, "
            "pwr_plant_repair_ser: NONE, "
            "bottled_oxy_type: None, "
            "bulk_oxy_type: None, "
            "lgt_sked: SEE RMK, "
            "bcn_lgt_sked: SS-SR, "
            "twr_type_code: NON-ATCT, "
            "seg_circle_mkr_flag: N, "
            "bcn_lens_color: WG, "
            "lndg_fee_flag: False, "
            "medical_use_flag: None, "
            "arpt_psn_source: 3RD PARTY SURVEY, "
            "position_src_date: 2025-06-17, "
            "arpt_elev_source: 3RD PARTY SURVEY, "
            "elevation_src_date: 2025-06-17, "
            "contr_fuel_avbl: None, "
            "trns_strg_buoy_flag: None, "
            "trns_strg_hgr_flag: None, "
            "trns_strg_tie_flag: True, "
            "other_services: None, "
            "wind_indcr_flag: Y-L, "
            "icao_id: None, "
            "min_op_network: False, "
            "user_fee_flag: None, "
            "cta: None",
        )
