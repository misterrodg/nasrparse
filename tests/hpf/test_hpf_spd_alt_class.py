from nasrparse.records.hpf import HPF_SPD_ALT

from datetime import date

import unittest


class TestHPF_SPD_ALT(unittest.TestCase):
    def setUp(self):
        self.maxDiff = None
        self.hpf_spd_alt = HPF_SPD_ALT(
            "2025/10/30",
            "HYPER INT*MD*K6",
            "1",
            "MD",
            "US",
            "210",
            "50/140",
        )

    def tearDown(self):
        pass

    def test_repr(self):
        result = repr(self.hpf_spd_alt)
        self.assertEqual(
            result,
            "HPF_SPD_ALT ( "
            "EFF_DATE=datetime.date(2025, 10, 30), "
            "HP_NAME='HYPER INT*MD*K6', "
            "HP_NO=1, "
            "STATE_CODE='MD', "
            "COUNTRY_CODE='US', "
            "SPEED_RANGE='210', "
            "ALTITUDE='50/140'"
            " )",
        ),

    def test_ordered_fields(self):
        result = self.hpf_spd_alt.ordered_fields()
        self.assertListEqual(
            result,
            [
                "eff_date",
                "hp_name",
                "hp_no",
                "state_code",
                "country_code",
                "speed_range",
                "altitude",
            ],
        )

    def test_to_dict(self):
        result = self.hpf_spd_alt.to_dict()
        self.assertDictEqual(
            result,
            {
                "eff_date": date(2025, 10, 30).strftime("%Y-%m-%d"),
                "hp_name": "HYPER INT*MD*K6",
                "hp_no": 1,
                "state_code": "MD",
                "country_code": "US",
                "speed_range": "210",
                "altitude": "50/140",
            },
        )

    def test_to_str(self):
        result = self.hpf_spd_alt.to_str()
        self.assertEqual(
            result,
            "eff_date: 2025-10-30, "
            "hp_name: HYPER INT*MD*K6, "
            "hp_no: 1, "
            "state_code: MD, "
            "country_code: US, "
            "speed_range: 210, "
            "altitude: 50/140",
        )
