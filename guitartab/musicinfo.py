class MusicInfo:

    def __init__(self, info, guitar_frets=20):
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

# todo: add functionality for guitar_tab to include all possible positions of a note based on the tuning


def get_guitar_tab(info, note_list, tuning=['E2', 'A2', 'D3', 'G3', 'B3', 'E4'], guitar_frets=15, use_closest_notes=True, keep_other_options=True) -> list:
    """
    Turns musical info of MusicInfo format into an array of guitar numbers

    [(fret, string), [(fret, string), (fret, string)], (...)]
    """

    guitar_tab = []
    guitar_strings = {}

    # set each tuning string to have a set of notes that correspond to it on the fretboard
    for k in tuning:

        # find where the tuning note starts
        start_index = note_list.index(k)

        if start_index + guitar_frets > len(note_list):
            raise Exception("Note list does not contain enough notes for the specified amount of guitar frets!")

        # set the tuning string to dictionary assigned to a list of the notes
        guitar_strings[k] = []

        # begin to add notes to the corresponding tuning note
        for i in range(start_index, start_index + guitar_frets):
            guitar_strings[k].append(note_list[i])

    def get_tune_string(note):
        for y in guitar_strings:
            if note in guitar_strings[y]:
                return [guitar_strings[y].index(note), y]

        raise Exception("Unable to find note within tuning strings")

    for x in info:

        # check if the current index in notes is a chord or not
        if not isinstance(x, list):
            guitar_tab.append(get_tune_string(x))
        else:
            chord = []
            for y in x:
                chord.append(get_tune_string(y))

            guitar_tab.append(chord)

    return guitar_tab


def convert_note_to_guitar(note):
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
    for k in range(1, number_of_notes):

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


def check_iterable(obj):
    try:
        _ = iter(obj)
    except TypeError:
        return False
    else:
        return True
