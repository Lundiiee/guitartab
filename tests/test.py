import unittest
from guitartab import musicinfo


class MusicInfo(unittest.TestCase):

    def setUp(self):
        raise Exception()

    def test_music_list(self):
        self.assertEquals(musicinfo.get_note_list(
            starting_key='E', ending_key='E', octave_start=2, octave_end=4),
            ['E2', 'F2', 'F#2', 'G2', 'G#2', 'A2', 'A#2', 'B2', 'C3', 'C#3', 'D3', 'D#3', 'E3', 'F3', 'F#3', 'G3',
             'G#3', 'A3', 'A#3', 'B3', 'C4', 'C#4', 'D4', 'D#4', 'E4'])


if __name__ == '__main__':
    unittest.main()
