

class MusicInfo:
    def __init__(self, info):
        """

        info contains notes for standard or guitar notation
        numbers next to it indicate octave

        [["C4", "E4", "G4"], ["A4"]]

        when converted to guitar tab:

        each note in a guitar tab is represented by (fret, string)
                 I
        [[(8,2), (x, y)], ...]

        """
        self.info = info

        if validate_info(info).type == "invalid":
            raise Exception("Music info given does not follow correct format. Convert by calling convert_to_info(info)")

    def get_guitar_tab(self, tuning=[]) -> list:
        """
        Turns musical info of MusicInfo format into an array of guitar numbers

        [(fret, string), [(fret, string), (fret, string)], (...)]
        """
        pass

    def get_guitar_tab_string(self, tuning=[]) -> str:
        """
        converts and returns guitar tab list to readable string

        e ---------0--------|
        B ------------------|
        G ---------3--------|
        D ------------------|
        A 5--6--7-----------|
        E 4--5--6-----------|
        """
        pass


def convert_to_info(notationtype):
    """
    Converts guitar tab into the correct MusicInfo format
    """
    return True


def validate_info(info):
    """
    Validates that the musical info is valid (is in the correct MusicInfo format
    or is in guitar tab format
    """
    _info = info.info if isinstance(info, MusicInfo) else info

    return True


def get_notation_type(info):
    """
    Returns information on the music info's type (guitar tab or standard notes)
    """
    _info = info.info if isinstance(info, MusicInfo) else info

    pass


def get_tab_from_ug(self):
    """
    Retrieves guitar tabs from ultimate-guitar.com
    """
    pass
