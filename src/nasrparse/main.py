from nasrparse.records.airports import Airports

from sqlite3 import connect

import os


class NASR:
    __exists: bool
    __dir_path: str

    __Airports: Airports

    def __init__(self, path: str) -> None:
        self.__exists = False
        self.__dir_path = ""

        self.__set_path(path)

        if self.__exists:
            self.__Airports = Airports(self.__dir_path)

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
        return

    def parse(self) -> None:
        self.__Airports.parse()

    def to_db(self, db_file_path: str) -> None:
        if os.path.exists(db_file_path):
            os.remove(db_file_path)

        connection = connect(db_file_path)
        db_cursor = connection.cursor()

        self.__Airports.to_db(db_cursor)

        connection.commit()
        connection.close()
