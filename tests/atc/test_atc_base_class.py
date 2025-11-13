from nasrparse.records.atc import ATC_BASE
from nasrparse.records.types import (
    AgencyTypeCode,
    FacilityOperatorCode,
    FacilityTypeCode,
    RegionCode,
    SiteTypeCode,
)

from datetime import date

import unittest


class TestATC_BASE(unittest.TestCase):
    def setUp(self):
        self.maxDiff = None
        self.atc_base = ATC_BASE(
            "2025/10/30",
            "24226.1",
            "A",
            "NON-ATCT",
            "TX",
            "00R",
            "LIVINGSTON",
            "US",
            "",
            "LIVINGSTON MUNI",
            "ASW",
            "",
            "",
            "",
            "HOUSTON ARTCC",
            "ZHU",
            "C",
            "",
            "",
            "",
            "HOUSTON ARTCC",
            "ZHU",
            "C",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
        )

    def tearDown(self):
        pass

    def test_repr(self):
        result = repr(self.atc_base)
        self.assertEqual(
            result,
            "ATC_BASE ( "
            "EFF_DATE=datetime.date(2025, 10, 30), "
            "SITE_NO='24226.1', "
            f"SITE_TYPE_CODE={SiteTypeCode.AIRPORT!r}, "
            f"FACILITY_TYPE={FacilityTypeCode.NON_ATCT!r}, "
            "STATE_CODE='TX', "
            "FACILITY_ID='00R', "
            "CITY='LIVINGSTON', "
            "COUNTRY_CODE='US', "
            "ICAO_ID=None, "
            "FACILITY_NAME='LIVINGSTON MUNI', "
            f"REGION_CODE={RegionCode.SOUTHWEST!r}, "
            f"TWR_OPERATOR_CODE={FacilityOperatorCode.NULL!r}, "
            "TWR_CALL=None, "
            "TWR_HRS=None, "
            "PRIMARY_APCH_RADIO_CALL='HOUSTON ARTCC', "
            "APCH_P_PROVIDER='ZHU', "
            f"APCH_P_PROV_TYPE_CD={AgencyTypeCode.ARTCC!r}, "
            "SECONDARY_APCH_RADIO_CALL=None, "
            "APCH_S_PROVIDER=None, "
            f"APCH_S_PROV_TYPE_CD={AgencyTypeCode.NULL!r}, "
            "PRIMARY_DEP_RADIO_CALL='HOUSTON ARTCC', "
            "DEP_P_PROVIDER='ZHU', "
            f"DEP_P_PROV_TYPE_CD={AgencyTypeCode.ARTCC!r}, "
            "SECONDARY_DEP_RADIO_CALL=None, "
            "DEP_S_PROVIDER=None, "
            f"DEP_S_PROV_TYPE_CD={AgencyTypeCode.NULL!r}, "
            "CTL_FAC_APCH_DEP_CALLS=None, "
            f"APCH_DEP_OPER_CODE={FacilityOperatorCode.NULL!r}, "
            "CTL_PRVDING_HRS=None, "
            "SECONDARY_CTL_PRVDING_HRS=None"
            " )",
        ),

    def test_ordered_fields(self):
        result = self.atc_base.ordered_fields()
        self.assertListEqual(
            result,
            [
                "eff_date",
                "site_no",
                "site_type_code",
                "facility_type",
                "state_code",
                "facility_id",
                "city",
                "country_code",
                "icao_id",
                "facility_name",
                "region_code",
                "twr_operator_code",
                "twr_call",
                "twr_hrs",
                "primary_apch_radio_call",
                "apch_p_provider",
                "apch_p_prov_type_cd",
                "secondary_apch_radio_call",
                "apch_s_provider",
                "apch_s_prov_type_cd",
                "primary_dep_radio_call",
                "dep_p_provider",
                "dep_p_prov_type_cd",
                "secondary_dep_radio_call",
                "dep_s_provider",
                "dep_s_prov_type_cd",
                "ctl_fac_apch_dep_calls",
                "apch_dep_oper_code",
                "ctl_prvding_hrs",
                "secondary_ctl_prvding_hrs",
            ],
        )

    def test_to_dict(self):
        result = self.atc_base.to_dict()
        self.assertDictEqual(
            result,
            {
                "eff_date": date(2025, 10, 30).strftime("%Y-%m-%d"),
                "site_no": "24226.1",
                "site_type_code": SiteTypeCode.AIRPORT.value,
                "facility_type": FacilityTypeCode.NON_ATCT.value,
                "state_code": "TX",
                "facility_id": "00R",
                "city": "LIVINGSTON",
                "country_code": "US",
                "icao_id": None,
                "facility_name": "LIVINGSTON MUNI",
                "region_code": RegionCode.SOUTHWEST.value,
                "twr_operator_code": FacilityOperatorCode.NULL.value,
                "twr_call": None,
                "twr_hrs": None,
                "primary_apch_radio_call": "HOUSTON ARTCC",
                "apch_p_provider": "ZHU",
                "apch_p_prov_type_cd": AgencyTypeCode.ARTCC.value,
                "secondary_apch_radio_call": None,
                "apch_s_provider": None,
                "apch_s_prov_type_cd": AgencyTypeCode.NULL.value,
                "primary_dep_radio_call": "HOUSTON ARTCC",
                "dep_p_provider": "ZHU",
                "dep_p_prov_type_cd": AgencyTypeCode.ARTCC.value,
                "secondary_dep_radio_call": None,
                "dep_s_provider": None,
                "dep_s_prov_type_cd": AgencyTypeCode.NULL.value,
                "ctl_fac_apch_dep_calls": None,
                "apch_dep_oper_code": FacilityOperatorCode.NULL.value,
                "ctl_prvding_hrs": None,
                "secondary_ctl_prvding_hrs": None,
            },
        )

    def test_to_str(self):
        result = self.atc_base.to_str()
        self.assertEqual(
            result,
            "eff_date: 2025-10-30, "
            "site_no: 24226.1, "
            "site_type_code: A, "
            "facility_type: NON-ATCT, "
            "state_code: TX, "
            "facility_id: 00R, "
            "city: LIVINGSTON, "
            "country_code: US, "
            "icao_id: None, "
            "facility_name: LIVINGSTON MUNI, "
            "region_code: ASW, "
            "twr_operator_code: None, "
            "twr_call: None, "
            "twr_hrs: None, "
            "primary_apch_radio_call: HOUSTON ARTCC, "
            "apch_p_provider: ZHU, "
            "apch_p_prov_type_cd: C, "
            "secondary_apch_radio_call: None, "
            "apch_s_provider: None, "
            "apch_s_prov_type_cd: None, "
            "primary_dep_radio_call: HOUSTON ARTCC, "
            "dep_p_provider: ZHU, "
            "dep_p_prov_type_cd: C, "
            "secondary_dep_radio_call: None, "
            "dep_s_provider: None, "
            "dep_s_prov_type_cd: None, "
            "ctl_fac_apch_dep_calls: None, "
            "apch_dep_oper_code: None, "
            "ctl_prvding_hrs: None, "
            "secondary_ctl_prvding_hrs: None",
        )
