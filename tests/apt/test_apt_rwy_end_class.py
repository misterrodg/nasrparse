from nasrparse.records.apt import APT_RWY_END
from nasrparse.records.types import (
    ApproachLightCode,
    HemisCode,
    ILSCode,
    ObstructionMarkingCode,
    Part77Code,
    RunwayMarkCode,
    RunwayMarkCondCode,
    RVRCode,
    SiteTypeCode,
    VGSICode,
)

from datetime import date

import unittest


class TestAPT_RWY_END(unittest.TestCase):
    def setUp(self):
        self.maxDiff = None
        self.apt_rwy_end = APT_RWY_END(
            "2025/10/30",
            "00103.",
            "A",
            "AL",
            "0J0",
            "ABBEVILLE",
            "US",
            "18/36",
            "18",
            "172",
            "",
            "N",
            "BSC",
            "GOOD",
            "31",
            "36",
            "30.6998",
            "N",
            "31.60852772",
            "85",
            "14",
            "22.7315",
            "W",
            "-85.23964763",
            "464.7",
            "44",
            "3",
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
            "468.3",
            "P2L",
            "",
            "",
            "",
            "",
            "",
            "",
            "TREES",
            "",
            "A(V)",
            "9",
            "32",
            "499",
            "237",
            "R",
            "",
            "",
            "3RD PARTY SURVEY",
            "2025/06/17",
            "3RD PARTY SURVEY",
            "2025/06/17",
            "",
            "",
            "",
            "",
            "3RD PARTY SURVEY",
            "2025/06/17",
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
        )

    def tearDown(self):
        pass

    def test_repr(self):
        result = repr(self.apt_rwy_end)
        self.assertEqual(
            result,
            "APT_RWY_END ( "
            "EFF_DATE=datetime.date(2025, 10, 30), "
            "SITE_NO='00103.', "
            f"SITE_TYPE_CODE={SiteTypeCode.AIRPORT!r}, "
            "STATE_CODE='AL', "
            "ARPT_ID='0J0', "
            "CITY='ABBEVILLE', "
            "COUNTRY_CODE='US', "
            "RWY_ID='18/36', "
            "RWY_END_ID='18', "
            "TRUE_ALIGNMENT=172, "
            f"ILS_TYPE={ILSCode.NULL!r}, "
            "RIGHT_HAND_TRAFFIC_PAT_FLAG=False, "
            f"RWY_MARKING_TYPE_CODE={RunwayMarkCode.BASIC!r}, "
            f"RWY_MARKING_COND={RunwayMarkCondCode.GOOD!r}, "
            "RWY_END_LAT_DEG=31, "
            "RWY_END_LAT_MIN=36, "
            "RWY_END_LAT_SEC=30.6998, "
            f"RWY_END_LAT_HEMIS={HemisCode.NORTH!r}, "
            "LAT_DECIMAL=31.60852772, "
            "RWY_END_LON_DEG=85, "
            "RWY_END_LON_MIN=14, "
            "RWY_END_LON_SEC=22.7315, "
            f"RWY_END_LON_HEMIS={HemisCode.WEST!r}, "
            "LON_DECIMAL=-85.23964763, "
            "RWY_END_ELEV=464.7, "
            "THR_CROSSING_HGT=44, "
            "VISUAL_GLIDE_PATH_ANGLE=3.0, "
            "DISPLACED_THR_LAT_DEG=None, "
            "DISPLACED_THR_LAT_MIN=None, "
            "DISPLACED_THR_LAT_SEC=None, "
            f"DISPLACED_THR_LAT_HEMIS={HemisCode.NULL!r}, "
            "LAT_DISPLACED_THR_DECIMAL=None, "
            "DISPLACED_THR_LON_DEG=None, "
            "DISPLACED_THR_LON_MIN=None, "
            "DISPLACED_THR_LON_SEC=None, "
            f"DISPLACED_THR_LON_HEMIS={HemisCode.NULL!r}, "
            "LON_DISPLACED_THR_DECIMAL=None, "
            "DISPLACED_THR_ELEV=None, "
            "DISPLACED_THR_LEN=None, "
            "TDZ_ELEV=468.3, "
            f"VGSI_CODE={VGSICode.PAPI_2_LEFT!r}, "
            f"RWY_VISUAL_RANGE_EQUIP_CODE={RVRCode.NULL!r}, "
            "RWY_VSBY_VALUE_EQUIP_FLAG=None, "
            f"APCH_LGT_SYSTEM_CODE={ApproachLightCode.NULL!r}, "
            "RWY_END_LGTS_FLAG=None, "
            "CNTRLN_LGTS_AVBL_FLAG=None, "
            "TDZ_LGT_AVBL_FLAG=None, "
            "OBSTN_TYPE='TREES', "
            f"OBSTN_MRKD_CODE={ObstructionMarkingCode.NULL!r}, "
            f"FAR_PART_77_CODE={Part77Code.UTILITY_RUNWAY_VISUAL!r}, "
            "OBSTN_CLNC_SLOPE='9', "
            "OBSTN_HGT=32, "
            "DIST_FROM_THR=499, "
            "CNTRLN_OFFSET=237, "
            "CNTRLN_DIR_CODE='R', "
            "RWY_GRAD=None, "
            "RWY_GRAD_DIRECTION=None, "
            "RWY_END_PSN_SOURCE='3RD PARTY SURVEY', "
            "RWY_END_PSN_DATE=datetime.date(2025, 6, 17), "
            "RWY_END_ELEV_SOURCE='3RD PARTY SURVEY', "
            "RWY_END_ELEV_DATE=datetime.date(2025, 6, 17), "
            "DSPL_THR_PSN_SOURCE=None, "
            "RWY_END_DSPL_THR_PSN_DATE=None, "
            "DSPL_THR_ELEV_SOURCE=None, "
            "RWY_END_DSPL_THR_ELEV_DATE=None, "
            "TDZ_ELEV_SOURCE='3RD PARTY SURVEY', "
            "RWY_END_TDZ_ELEV_DATE=datetime.date(2025, 6, 17), "
            "TKOF_RUN_AVBL=None, "
            "TKOF_DIST_AVBL=None, "
            "ACLT_STOP_DIST_AVBL=None, "
            "LNDG_DIST_AVBL=None, "
            "LAHSO_ALD=None, "
            "RWY_END_INTERSECT_LAHSO=None, "
            "LAHSO_DESC=None, "
            "LAHSO_LAT=None, "
            "LAT_LAHSO_DECIMAL=None, "
            "LAHSO_LON=None, "
            "LON_LAHSO_DECIMAL=None, "
            "LAHSO_PSN_SOURCE=None, "
            "RWY_END_LAHSO_PSN_DATE=None"
            " )",
        ),

    def test_ordered_fields(self):
        result = self.apt_rwy_end.ordered_fields()
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
                "rwy_end_id",
                "true_alignment",
                "ils_type",
                "right_hand_traffic_pat_flag",
                "rwy_marking_type_code",
                "rwy_marking_cond",
                "rwy_end_lat_deg",
                "rwy_end_lat_min",
                "rwy_end_lat_sec",
                "rwy_end_lat_hemis",
                "lat_decimal",
                "rwy_end_lon_deg",
                "rwy_end_lon_min",
                "rwy_end_lon_sec",
                "rwy_end_lon_hemis",
                "lon_decimal",
                "rwy_end_elev",
                "thr_crossing_hgt",
                "visual_glide_path_angle",
                "displaced_thr_lat_deg",
                "displaced_thr_lat_min",
                "displaced_thr_lat_sec",
                "displaced_thr_lat_hemis",
                "lat_displaced_thr_decimal",
                "displaced_thr_lon_deg",
                "displaced_thr_lon_min",
                "displaced_thr_lon_sec",
                "displaced_thr_lon_hemis",
                "lon_displaced_thr_decimal",
                "displaced_thr_elev",
                "displaced_thr_len",
                "tdz_elev",
                "vgsi_code",
                "rwy_visual_range_equip_code",
                "rwy_vsby_value_equip_flag",
                "apch_lgt_system_code",
                "rwy_end_lgts_flag",
                "cntrln_lgts_avbl_flag",
                "tdz_lgt_avbl_flag",
                "obstn_type",
                "obstn_mrkd_code",
                "far_part_77_code",
                "obstn_clnc_slope",
                "obstn_hgt",
                "dist_from_thr",
                "cntrln_offset",
                "cntrln_dir_code",
                "rwy_grad",
                "rwy_grad_direction",
                "rwy_end_psn_source",
                "rwy_end_psn_date",
                "rwy_end_elev_source",
                "rwy_end_elev_date",
                "dspl_thr_psn_source",
                "rwy_end_dspl_thr_psn_date",
                "dspl_thr_elev_source",
                "rwy_end_dspl_thr_elev_date",
                "tdz_elev_source",
                "rwy_end_tdz_elev_date",
                "tkof_run_avbl",
                "tkof_dist_avbl",
                "aclt_stop_dist_avbl",
                "lndg_dist_avbl",
                "lahso_ald",
                "rwy_end_intersect_lahso",
                "lahso_desc",
                "lahso_lat",
                "lat_lahso_decimal",
                "lahso_lon",
                "lon_lahso_decimal",
                "lahso_psn_source",
                "rwy_end_lahso_psn_date",
            ],
        )

    def test_to_dict(self):
        result = self.apt_rwy_end.to_dict()
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
                "rwy_end_id": "18",
                "true_alignment": 172,
                "ils_type": ILSCode.NULL.value,
                "right_hand_traffic_pat_flag": False,
                "rwy_marking_type_code": RunwayMarkCode.BASIC.value,
                "rwy_marking_cond": RunwayMarkCondCode.GOOD.value,
                "rwy_end_lat_deg": 31,
                "rwy_end_lat_min": 36,
                "rwy_end_lat_sec": 30.6998,
                "rwy_end_lat_hemis": HemisCode.NORTH.value,
                "lat_decimal": 31.60852772,
                "rwy_end_lon_deg": 85,
                "rwy_end_lon_min": 14,
                "rwy_end_lon_sec": 22.7315,
                "rwy_end_lon_hemis": HemisCode.WEST.value,
                "lon_decimal": -85.23964763,
                "rwy_end_elev": 464.7,
                "thr_crossing_hgt": 44,
                "visual_glide_path_angle": 3,
                "displaced_thr_lat_deg": None,
                "displaced_thr_lat_min": None,
                "displaced_thr_lat_sec": None,
                "displaced_thr_lat_hemis": HemisCode.NULL.value,
                "lat_displaced_thr_decimal": None,
                "displaced_thr_lon_deg": None,
                "displaced_thr_lon_min": None,
                "displaced_thr_lon_sec": None,
                "displaced_thr_lon_hemis": HemisCode.NULL.value,
                "lon_displaced_thr_decimal": None,
                "displaced_thr_elev": None,
                "displaced_thr_len": None,
                "tdz_elev": 468.3,
                "vgsi_code": VGSICode.PAPI_2_LEFT.value,
                "rwy_visual_range_equip_code": RVRCode.NULL.value,
                "rwy_vsby_value_equip_flag": None,
                "apch_lgt_system_code": ApproachLightCode.NULL.value,
                "rwy_end_lgts_flag": None,
                "cntrln_lgts_avbl_flag": None,
                "tdz_lgt_avbl_flag": None,
                "obstn_type": "TREES",
                "obstn_mrkd_code": ObstructionMarkingCode.NULL.value,
                "far_part_77_code": Part77Code.UTILITY_RUNWAY_VISUAL.value,
                "obstn_clnc_slope": "9",
                "obstn_hgt": 32,
                "dist_from_thr": 499,
                "cntrln_offset": 237,
                "cntrln_dir_code": "R",
                "rwy_grad": None,
                "rwy_grad_direction": None,
                "rwy_end_psn_source": "3RD PARTY SURVEY",
                "rwy_end_psn_date": date(2025, 6, 17).strftime("%Y-%m-%d"),
                "rwy_end_elev_source": "3RD PARTY SURVEY",
                "rwy_end_elev_date": date(2025, 6, 17).strftime("%Y-%m-%d"),
                "dspl_thr_psn_source": None,
                "rwy_end_dspl_thr_psn_date": None,
                "dspl_thr_elev_source": None,
                "rwy_end_dspl_thr_elev_date": None,
                "tdz_elev_source": "3RD PARTY SURVEY",
                "rwy_end_tdz_elev_date": date(2025, 6, 17).strftime("%Y-%m-%d"),
                "tkof_run_avbl": None,
                "tkof_dist_avbl": None,
                "aclt_stop_dist_avbl": None,
                "lndg_dist_avbl": None,
                "lahso_ald": None,
                "rwy_end_intersect_lahso": None,
                "lahso_desc": None,
                "lahso_lat": None,
                "lat_lahso_decimal": None,
                "lahso_lon": None,
                "lon_lahso_decimal": None,
                "lahso_psn_source": None,
                "rwy_end_lahso_psn_date": None,
            },
        )

    def test_to_str(self):
        result = self.apt_rwy_end.to_str()
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
            "rwy_end_id: 18, "
            "true_alignment: 172, "
            "ils_type: None, "
            "right_hand_traffic_pat_flag: False, "
            "rwy_marking_type_code: BSC, "
            "rwy_marking_cond: GOOD, "
            "rwy_end_lat_deg: 31, "
            "rwy_end_lat_min: 36, "
            "rwy_end_lat_sec: 30.6998, "
            "rwy_end_lat_hemis: N, "
            "lat_decimal: 31.60852772, "
            "rwy_end_lon_deg: 85, "
            "rwy_end_lon_min: 14, "
            "rwy_end_lon_sec: 22.7315, "
            "rwy_end_lon_hemis: W, "
            "lon_decimal: -85.23964763, "
            "rwy_end_elev: 464.7, "
            "thr_crossing_hgt: 44, "
            "visual_glide_path_angle: 3.0, "
            "displaced_thr_lat_deg: None, "
            "displaced_thr_lat_min: None, "
            "displaced_thr_lat_sec: None, "
            "displaced_thr_lat_hemis: None, "
            "lat_displaced_thr_decimal: None, "
            "displaced_thr_lon_deg: None, "
            "displaced_thr_lon_min: None, "
            "displaced_thr_lon_sec: None, "
            "displaced_thr_lon_hemis: None, "
            "lon_displaced_thr_decimal: None, "
            "displaced_thr_elev: None, "
            "displaced_thr_len: None, "
            "tdz_elev: 468.3, "
            "vgsi_code: P2L, "
            "rwy_visual_range_equip_code: None, "
            "rwy_vsby_value_equip_flag: None, "
            "apch_lgt_system_code: None, "
            "rwy_end_lgts_flag: None, "
            "cntrln_lgts_avbl_flag: None, "
            "tdz_lgt_avbl_flag: None, "
            "obstn_type: TREES, "
            "obstn_mrkd_code: None, "
            "far_part_77_code: A(V), "
            "obstn_clnc_slope: 9, "
            "obstn_hgt: 32, "
            "dist_from_thr: 499, "
            "cntrln_offset: 237, "
            "cntrln_dir_code: R, "
            "rwy_grad: None, "
            "rwy_grad_direction: None, "
            "rwy_end_psn_source: 3RD PARTY SURVEY, "
            "rwy_end_psn_date: 2025-06-17, "
            "rwy_end_elev_source: 3RD PARTY SURVEY, "
            "rwy_end_elev_date: 2025-06-17, "
            "dspl_thr_psn_source: None, "
            "rwy_end_dspl_thr_psn_date: None, "
            "dspl_thr_elev_source: None, "
            "rwy_end_dspl_thr_elev_date: None, "
            "tdz_elev_source: 3RD PARTY SURVEY, "
            "rwy_end_tdz_elev_date: 2025-06-17, "
            "tkof_run_avbl: None, "
            "tkof_dist_avbl: None, "
            "aclt_stop_dist_avbl: None, "
            "lndg_dist_avbl: None, "
            "lahso_ald: None, "
            "rwy_end_intersect_lahso: None, "
            "lahso_desc: None, "
            "lahso_lat: None, "
            "lat_lahso_decimal: None, "
            "lahso_lon: None, "
            "lon_lahso_decimal: None, "
            "lahso_psn_source: None, "
            "rwy_end_lahso_psn_date: None",
        )
