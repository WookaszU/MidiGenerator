from miditime.miditime import MIDITime
import Algorithm

class generator:

    def __init__(self, algo):
        self.algorithm = algo

    def set_algorithm(self, algo):
        self.algorithm = algo

    def generate(self, lenght, path_in, path_out, bmp, nutes_max):
        mymidi = MIDITime(bmp, path_out)

        midinotes = self.algorithm.compose(lenght, path_in, nutes_max)

        mymidi.add_track(midinotes)
        mymidi.save_midi()




