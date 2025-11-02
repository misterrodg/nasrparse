from nasrparse.records import (
    APTs,
    CLSs,
    AWYs,
    ATCs,
    AWOSs,
    ARBs,
    CDRs,
    COMs,
    DPs,
)

from sqlite3 import connect

import json
import os


class NASR:
    __exists: bool
    __dir_path: str

    __APTs: APTs
    __CLSs: CLSs
    __AWYs: AWYs
    __ATCs: ATCs
    __AWOSs: AWOSs
    __ARBs: ARBs
    __CDRs: CDRs
    __COMs: COMs
    __DPs: DPs

    def __init__(self, path: str) -> None:
        self.__exists = False
        self.__dir_path = ""

        self.__set_path(path)

        self.__APTs = APTs(self.__dir_path)
        self.__CLSs = CLSs(self.__dir_path)
        self.__AWYs = AWYs(self.__dir_path)
        self.__ATCs = ATCs(self.__dir_path)
        self.__AWOSs = AWOSs(self.__dir_path)
        self.__ARBs = ARBs(self.__dir_path)
        self.__CDRs = CDRs(self.__dir_path)
        self.__COMs = COMs(self.__dir_path)
        self.__DPs = DPs(self.__dir_path)

    def __set_path(self, path: str) -> None:
        self.__dir_path = path
        if os.path.exists(self.__dir_path):
            print(f"NASR Parser :: Found NASR dir at: {path}")
            self.__exists = True
        else:
            print(f"NASR Parser :: Unable to find NASR dir at: {path}")
            return

    def parse_apt_ars(self) -> None:
        if self.__exists:
            self.__APTs.parse_apt_ars()

    def parse_apt_att(self) -> None:
        if self.__exists:
            self.__APTs.parse_apt_att()

    def parse_apt_base(self) -> None:
        if self.__exists:
            self.__APTs.parse_apt_base()

    def parse_apt_con(self) -> None:
        if self.__exists:
            self.__APTs.parse_apt_con()

    def parse_apt_rmk(self) -> None:
        if self.__exists:
            self.__APTs.parse_apt_rmk()

    def parse_apt_rwy(self) -> None:
        if self.__exists:
            self.__APTs.parse_apt_rwy()

    def parse_apt_rwy_end(self) -> None:
        if self.__exists:
            self.__APTs.parse_apt_rwy_end()

    def parse_apt(self) -> None:
        if self.__exists:
            self.__APTs.parse()

    def parse_awy_alt(self) -> None:
        if self.__exists:
            self.__AWYs.parse_awy_alt()

    def parse_awy_base(self) -> None:
        if self.__exists:
            self.__AWYs.parse_awy_base()

    def parse_awy_seg(self) -> None:
        if self.__exists:
            self.__AWYs.parse_awy_seg()

    def parse_awy_seg_alt(self) -> None:
        if self.__exists:
            self.__AWYs.parse_awy_seg_alt()

    def parse_awy(self) -> None:
        if self.__exists:
            self.__AWYs.parse()

    def parse_arb_base(self) -> None:
        if self.__exists:
            self.__ARBs.parse_arb_base()

    def parse_arb_seg(self) -> None:
        if self.__exists:
            self.__ARBs.parse_arb_seg()

    def parse_arb(self) -> None:
        if self.__exists:
            self.__ARBs.parse()

    def parse_atc_atis(self) -> None:
        if self.__exists:
            self.__ATCs.parse_atc_atis()

    def parse_atc_base(self) -> None:
        if self.__exists:
            self.__ATCs.parse_atc_base()

    def parse_atc_rmk(self) -> None:
        if self.__exists:
            self.__ATCs.parse_atc_rmk()

    def parse_atc_svc(self) -> None:
        if self.__exists:
            self.__ATCs.parse_atc_svc()

    def parse_atc(self) -> None:
        if self.__exists:
            self.__ATCs.parse()

    def parse_awos_base(self) -> None:
        if self.__exists:
            self.__AWOSs.parse_awos_base()

    def parse_awos(self) -> None:
        if self.__exists:
            self.__AWOSs.parse()

    def parse_cdr_base(self) -> None:
        if self.__exists:
            self.__CDRs.parse_cdr_base()

    def parse_cdr(self) -> None:
        if self.__exists:
            self.__CDRs.parse()

    def parse_cls_arsp(self) -> None:
        if self.__exists:
            self.__CLSs.parse_cls_arsp()

    def parse_cls(self) -> None:
        if self.__exists:
            self.__CLSs.parse()

    def parse_com_base(self) -> None:
        if self.__exists:
            self.__COMs.parse_com_base()

    def parse_com(self) -> None:
        if self.__exists:
            self.__COMs.parse()

    def parse_dp_apt(self) -> None:
        if self.__exists:
            self.__DPs.parse_dp_apt()

    def parse_dp_base(self) -> None:
        if self.__exists:
            self.__DPs.parse_dp_base()

    def parse_dp_rte(self) -> None:
        if self.__exists:
            self.__DPs.parse_dp_rte()

    def parse_dp(self) -> None:
        if self.__exists:
            self.__DPs.parse()

    def parse(self) -> None:
        self.parse_apt()
        self.parse_arb()
        self.parse_atc()
        self.parse_awy()
        self.parse_awos()
        self.parse_cdr()
        self.parse_cls()
        self.parse_com()
        self.parse_dp()

    def to_dict(self, json_file_path: str) -> None:
        if os.path.exists(json_file_path):
            os.remove(json_file_path)

        result = {
            **self.__APTs.to_dict(),
            **self.__CLSs.to_dict(),
            **self.__AWYs.to_dict(),
            **self.__ATCs.to_dict(),
            **self.__AWOSs.to_dict(),
            **self.__ARBs.to_dict(),
            **self.__CDRs.to_dict(),
            **self.__COMs.to_dict(),
            **self.__DPs.to_dict(),
        }

        with open(json_file_path, "w") as jf:
            json.dump(result, jf, indent=4)

    def to_db(self, db_file_path: str) -> None:
        if os.path.exists(db_file_path):
            os.remove(db_file_path)

        connection = connect(db_file_path)
        db_cursor = connection.cursor()

        self.__APTs.to_db(db_cursor)
        self.__CLSs.to_db(db_cursor)
        self.__AWYs.to_db(db_cursor)
        self.__ATCs.to_db(db_cursor)
        self.__AWOSs.to_db(db_cursor)
        self.__ARBs.to_db(db_cursor)
        self.__CDRs.to_db(db_cursor)
        self.__COMs.to_db(db_cursor)
        self.__DPs.to_db(db_cursor)

        connection.commit()
        connection.close()
