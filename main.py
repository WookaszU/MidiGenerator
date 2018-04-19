import Generator
import Algorithm
import argparse
import Parserhelper
import os


parser = argparse.ArgumentParser(description = "creates a new midi file from given midi or optionally from two midi files")

parser.add_argument("--path", help = "path to directory in which you want to save your midi", default = os.path.dirname(os.path.realpath(__file__)),
                    type = lambda x: Parserhelper.is_valid_directory(parser, x))
parser.add_argument("midi_in", help = "paths to midi files",nargs = '+', type = lambda x: Parserhelper.is_valid_file(parser, x))
parser.add_argument("name", help = "name of new midi file", type = str)
parser.add_argument("--length", help = "approximate length of new midi file in seconds", default = 350,
                    type= lambda x: Parserhelper.is_valid_number(parser, x))
parser.add_argument("--bpm","-b", help = "choose BPM - beats per minute", default = 250,
                    type= lambda x: Parserhelper.is_valid_number(parser, x))
parser.add_argument("--note_num", help = "choose number of nutes which can be used in the same time", default = 10,
                    type = lambda x: Parserhelper.is_valid_number(parser, x))

args = parser.parse_args()
print(args)

path_out = os.path.join(args.path,args.name)

algo = Algorithm.algorithm()
gen = Generator.generator(algo)

gen.generate(args.length, args.midi_in, path_out, args.bpm, args.note_num)