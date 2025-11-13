from nasrparse.records.maa import MAA_SHP

from datetime import date

import unittest


class TestMAA_SHP(unittest.TestCase):
    def setUp(self):
        self.maxDiff = None
        self.maa_shp = MAA_SHP(
            "2025/10/30", "AVA001", "1", "38-24-24.4600N", "077-27-59.2900W"
        )

    def tearDown(self):
        pass

    def test_repr(self):
        result = repr(self.maa_shp)
        self.assertEqual(
            result,
            "MAA_SHP ( "
            "EFF_DATE=datetime.date(2025, 10, 30), "
            "MAA_ID='AVA001', "
            "POINT_SEQ=1, "
            "LATITUDE=38.406794444444444, "
            "LONGITUDE=-77.46646944444444"
            " )",
        ),

    def test_ordered_fields(self):
        result = self.maa_shp.ordered_fields()
        self.assertListEqual(
            result,
            [
                "eff_date",
                "maa_id",
                "point_seq",
                "latitude",
                "longitude",
            ],
        )

    def test_to_dict(self):
        result = self.maa_shp.to_dict()
        self.assertDictEqual(
            result,
            {
                "eff_date": date(2025, 10, 30).strftime("%Y-%m-%d"),
                "maa_id": "AVA001",
                "point_seq": 1,
                "latitude": 38.406794444444444,
                "longitude": -77.46646944444444,
            },
        )

    def test_to_str(self):
        result = self.maa_shp.to_str()
        self.assertEqual(
            result,
            "eff_date: 2025-10-30, "
            "maa_id: AVA001, "
            "point_seq: 1, "
            "latitude: 38.406794444444444, "
            "longitude: -77.46646944444444",
        )
