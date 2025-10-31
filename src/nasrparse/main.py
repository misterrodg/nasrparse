from nasrparse.records import (
    Airports,
    Airspaces,
    Airways,
    ATCComms,
    AWOSs,
    Boundaries,
    CodedRoutes,
)

from sqlite3 import connect

import os


class NASR:
    __exists: bool
    __dir_path: str

    __Airports: Airports
    __Airspaces: Airspaces
    __Airways: Airways
    __ATCComms: ATCComms
    __AWOSs: AWOSs
    __Boundaries: Boundaries
    __CodedRoutes: CodedRoutes

    def __init__(self, path: str) -> None:
        self.__exists = False
        self.__dir_path = ""

        self.__set_path(path)

        if self.__exists:
            self.__Airports = Airports(self.__dir_path)
            self.__Airspaces = Airspaces(self.__dir_path)
            self.__Airways = Airways(self.__dir_path)
            self.__ATCComms = ATCComms(self.__dir_path)
            self.__AWOSs = AWOSs(self.__dir_path)
            self.__Boundaries = Boundaries(self.__dir_path)
            self.__CodedRoutes = CodedRoutes(self.__dir_path)

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
            self.__Airports.parse_apt_ars()

    def parse_apt_att(self) -> None:
        if self.__exists:
            self.__Airports.parse_apt_att()

    def parse_apt_base(self) -> None:
        if self.__exists:
            self.__Airports.parse_apt_base()

    def parse_apt_con(self) -> None:
        if self.__exists:
            self.__Airports.parse_apt_con()

    def parse_apt_rmk(self) -> None:
        if self.__exists:
            self.__Airports.parse_apt_rmk()

    def parse_apt_rwy(self) -> None:
        if self.__exists:
            self.__Airports.parse_apt_rwy()

    def parse_apt_rwy_end(self) -> None:
        if self.__exists:
            self.__Airports.parse_apt_rwy_end()

    def parse_apt(self) -> None:
        self.__Airports.parse()

    def parse_awy_alt(self) -> None:
        if self.__exists:
            self.__Airways.parse_awy_alt()

    def parse_awy_base(self) -> None:
        if self.__exists:
            self.__Airways.parse_awy_base()

    def parse_awy_seg(self) -> None:
        if self.__exists:
            self.__Airways.parse_awy_seg()

    def parse_awy_seg_alt(self) -> None:
        if self.__exists:
            self.__Airways.parse_awy_seg_alt()

    def parse_awy(self) -> None:
        self.__Airways.parse()

    def parse_arb_base(self) -> None:
        if self.__exists:
            self.__Boundaries.parse_arb_base()

    def parse_arb_seg(self) -> None:
        if self.__exists:
            self.__Boundaries.parse_arb_seg()

    def parse_arb(self) -> None:
        self.__Boundaries.parse()

    def parse_atc_atis(self) -> None:
        if self.__exists:
            self.__ATCComms.parse_atc_atis()

    def parse_atc_base(self) -> None:
        if self.__exists:
            self.__ATCComms.parse_atc_base()

    def parse_atc_rmk(self) -> None:
        if self.__exists:
            self.__ATCComms.parse_atc_rmk()

    def parse_atc_svc(self) -> None:
        if self.__exists:
            self.__ATCComms.parse_atc_svc()

    def parse_atc(self) -> None:
        self.__ATCComms.parse()

    def parse_awos_base(self) -> None:
        if self.__exists:
            self.__AWOSs.parse_awos_base()

    def parse_awos(self) -> None:
        if self.__exists:
            self.__AWOSs.parse()

    def parse_cdr_base(self) -> None:
        if self.__exists:
            self.__CodedRoutes.parse_cdr_base()

    def parse_cdr(self) -> None:
        if self.__exists:
            self.__CodedRoutes.parse()

    def parse_cls_arsp(self) -> None:
        if self.__exists:
            self.__Airspaces.parse_cls_arsp()

    def parse_cls(self) -> None:
        if self.__exists:
            self.__Airspaces.parse()

    def parse(self) -> None:
        self.parse_apt()
        self.parse_arb()
        self.parse_atc()
        self.parse_awy()
        self.parse_awos()
        self.parse_cdr()
        self.parse_cls()

    def to_db(self, db_file_path: str) -> None:
        if os.path.exists(db_file_path):
            os.remove(db_file_path)

        connection = connect(db_file_path)
        db_cursor = connection.cursor()

        self.__Airports.to_db(db_cursor)
        self.__Airspaces.to_db(db_cursor)
        self.__Airways.to_db(db_cursor)
        self.__ATCComms.to_db(db_cursor)
        self.__AWOSs.to_db(db_cursor)
        self.__Boundaries.to_db(db_cursor)
        self.__CodedRoutes.to_db(db_cursor)

        connection.commit()
        connection.close()
