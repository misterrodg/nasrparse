from nasrparse.records.apt import APT_CON
from nasrparse.records.types import SiteTypeCode

from datetime import date

import unittest


class TestAPT_CON(unittest.TestCase):
    def setUp(self):
        self.maxDiff = None
        self.apt_con = APT_CON(
            "2025/10/30",
            "00103.",
            "A",
            "AL",
            "0J0",
            "ABBEVILLE",
            "US",
            "MANAGER",
            "MELISSA WILSON",
            "PO BOX 427",
            "101 E. WASHINGTON ST",
            "ABBEVILLE",
            "AL",
            "36310",
            "",
            "334-585-6444",
        )

    def tearDown(self):
        pass

    def test_repr(self):
        result = repr(self.apt_con)
        self.assertEqual(
            result,
            "APT_CON ( "
            "EFF_DATE=datetime.date(2025, 10, 30), "
            "SITE_NO='00103.', "
            f"SITE_TYPE_CODE={SiteTypeCode.AIRPORT!r}, "
            "STATE_CODE='AL', "
            "ARPT_ID='0J0', "
            "CITY='ABBEVILLE', "
            "COUNTRY_CODE='US', "
            "TITLE='MANAGER', "
            "NAME='MELISSA WILSON', "
            "ADDRESS1='PO BOX 427', "
            "ADDRESS2='101 E. WASHINGTON ST', "
            "TITLE_CITY='ABBEVILLE', "
            "STATE='AL', "
            "ZIP_CODE='36310', "
            "ZIP_PLUS_FOUR=None, "
            "PHONE_NO='334-585-6444'"
            " )",
        ),

    def test_ordered_fields(self):
        result = self.apt_con.ordered_fields()
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
                "title",
                "name",
                "address1",
                "address2",
                "title_city",
                "state",
                "zip_code",
                "zip_plus_four",
                "phone_no",
            ],
        )

    def test_to_dict(self):
        result = self.apt_con.to_dict()
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
                "title": "MANAGER",
                "name": "MELISSA WILSON",
                "address1": "PO BOX 427",
                "address2": "101 E. WASHINGTON ST",
                "title_city": "ABBEVILLE",
                "state": "AL",
                "zip_code": "36310",
                "zip_plus_four": None,
                "phone_no": "334-585-6444",
            },
        )

    def test_to_str(self):
        result = self.apt_con.to_str()
        self.assertEqual(
            result,
            "eff_date: 2025-10-30, "
            "site_no: 00103., "
            "site_type_code: A, "
            "state_code: AL, "
            "arpt_id: 0J0, "
            "city: ABBEVILLE, "
            "country_code: US, "
            "title: MANAGER, "
            "name: MELISSA WILSON, "
            "address1: PO BOX 427, "
            "address2: 101 E. WASHINGTON ST, "
            "title_city: ABBEVILLE, "
            "state: AL, "
            "zip_code: 36310, "
            "zip_plus_four: None, "
            "phone_no: 334-585-6444",
        )
