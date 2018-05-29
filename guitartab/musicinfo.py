

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

        if validate_info(info).type == "invalid":
            raise Exception("Music info given does not follow correct format. Convert by calling convert_to_info(info)")

        self.info = info
        self.note_list = get_note_list('C', 'C', 0, 6, 22)

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


def get_guitar_tab(_info, tuning=['E2', 'A2', 'D3', 'G3', 'B3', 'E4']) -> list:
    """
    Turns musical info of MusicInfo format into an array of guitar numbers

    [(fret, string), [(fret, string), (fret, string)], (...)]
    """
    pass

def get_note_list(starting_key='E', ending_key='E', octave_start=2, octave_end=4, guitar_frets=0) -> list:
    """
    Returns a list of notes with their corresponding octaves and is represented by sharp keys

    'F#4', 'C4', '(note)(octave)'
    """

    octave = ['C', 'C#', 'D', 'D#',
              'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']

    # the number of notes between octaves, plus the offset of the octave key from start of octave
    number_of_notes = (octave_end - octave_start) * 12 + (octave.index(ending_key)) + guitar_frets

    note_dictionary = []

    current_octave = octave_start
    index = octave.index(starting_key)
    for k in range(1, number_of_notes + 1):

        if current_octave == octave_end and octave[index] == ending_key:
            note_dictionary.append(octave[index] + str(current_octave))

            break

        # if index reaches end of octave, reset index and change current octave
        if index == len(octave):
            index = 0
            current_octave += 1

            continue

        note_dictionary.append(octave[index] + str(current_octave))

        index += 1

    return note_dictionary


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
