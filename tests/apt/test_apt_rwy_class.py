from nasrparse.records.apt import APT_RWY
from nasrparse.records.types import (
    ConditionCode,
    DeterminationCode,
    PavementCode,
    RunwayLightCode,
    SiteTypeCode,
    SurfaceCode,
    TreatmentCode,
)

from datetime import date

import unittest


class TestAPT_RWY(unittest.TestCase):
    def setUp(self):
        self.maxDiff = None
        self.apt_rwy = APT_RWY(
            "2025/10/30",
            "00103.",
            "A",
            "AL",
            "0J0",
            "ABBEVILLE",
            "US",
            "18/36",
            "5000",
            "75",
            "ASPH",
            "FAIR",
            "AFSC",
            "",
            "",
            "",
            "",
            "",
            "MED",
            "3RD PARTY SURVEY",
            "2025/06/17",
            "",
            "",
            "",
            "",
        )

    def tearDown(self):
        pass

    def test_repr(self):
        result = repr(self.apt_rwy)
        self.assertEqual(
            result,
            "APT_RWY ( "
            "EFF_DATE=datetime.date(2025, 10, 30), "
            "SITE_NO='00103.', "
            f"SITE_TYPE_CODE={SiteTypeCode.AIRPORT!r}, "
            "STATE_CODE='AL', "
            "ARPT_ID='0J0', "
            "CITY='ABBEVILLE', "
            "COUNTRY_CODE='US', "
            "RWY_ID='18/36', "
            "RWY_LEN=5000, "
            "RWY_WIDTH=75, "
            f"SURFACE_TYPE_CODE=[{SurfaceCode.ASPHALT_CONCRETE!r}], "
            f"COND={ConditionCode.FAIR!r}, "
            f"TREATMENT_CODE={TreatmentCode.AGGREGATE_FRICTION_SEAL_COAT!r}, "
            "PCN=None, "
            f"PAVEMENT_TYPE_CODE={PavementCode.NULL!r}, "
            "SUBGRADE_STRENGTH_CODE=None, "
            "TIRE_PRES_CODE=None, "
            f"DTRM_METHOD_CODE={DeterminationCode.NULL!r}, "
            f"RWY_LGT_CODE={RunwayLightCode.MED!r}, "
            "RWY_LEN_SOURCE='3RD PARTY SURVEY', "
            "LENGTH_SOURCE_DATE=datetime.date(2025, 6, 17), "
            "GROSS_WT_SW=None, "
            "GROSS_WT_DW=None, "
            "GROSS_WT_DTW=None, "
            "GROSS_WT_DDTW=None"
            " )",
        ),

    def test_ordered_fields(self):
        result = self.apt_rwy.ordered_fields()
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
                "rwy_id",
                "rwy_len",
                "rwy_width",
                "surface_type_code",
                "cond",
                "treatment_code",
                "pcn",
                "pavement_type_code",
                "subgrade_strength_code",
                "tire_pres_code",
                "dtrm_method_code",
                "rwy_lgt_code",
                "rwy_len_source",
                "length_source_date",
                "gross_wt_sw",
                "gross_wt_dw",
                "gross_wt_dtw",
                "gross_wt_ddtw",
            ],
        )

    def test_to_dict(self):
        result = self.apt_rwy.to_dict()
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
                "rwy_id": "18/36",
                "rwy_len": 5000,
                "rwy_width": 75,
                "surface_type_code": SurfaceCode.ASPHALT_CONCRETE.value,
                "cond": ConditionCode.FAIR.value,
                "treatment_code": TreatmentCode.AGGREGATE_FRICTION_SEAL_COAT.value,
                "pcn": None,
                "pavement_type_code": None,
                "subgrade_strength_code": None,
                "tire_pres_code": None,
                "dtrm_method_code": None,
                "rwy_lgt_code": RunwayLightCode.MED.value,
                "rwy_len_source": "3RD PARTY SURVEY",
                "length_source_date": date(2025, 6, 17).strftime("%Y-%m-%d"),
                "gross_wt_sw": None,
                "gross_wt_dw": None,
                "gross_wt_dtw": None,
                "gross_wt_ddtw": None,
            },
        )

    def test_to_str(self):
        result = self.apt_rwy.to_str()
        self.assertEqual(
            result,
            "eff_date: 2025-10-30, "
            "site_no: 00103., "
            "site_type_code: A, "
            "state_code: AL, "
            "arpt_id: 0J0, "
            "city: ABBEVILLE, "
            "country_code: US, "
            "rwy_id: 18/36, "
            "rwy_len: 5000, "
            "rwy_width: 75, "
            "surface_type_code: ASPH, "
            "cond: FAIR, "
            "treatment_code: AFSC, "
            "pcn: None, "
            "pavement_type_code: None, "
            "subgrade_strength_code: None, "
            "tire_pres_code: None, "
            "dtrm_method_code: None, "
            "rwy_lgt_code: MED, "
            "rwy_len_source: 3RD PARTY SURVEY, "
            "length_source_date: 2025-06-17, "
            "gross_wt_sw: None, "
            "gross_wt_dw: None, "
            "gross_wt_dtw: None, "
            "gross_wt_ddtw: None",
        )
