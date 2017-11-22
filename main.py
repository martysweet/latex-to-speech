import argparse
import os

from latextotext.Pandoc import Pandoc
from tts.AWSPolly import AWSPolly


def __is_valid_file(parser, arg):
    if not os.path.exists(arg):
        parser.error("The file {} does not exist!".format(arg))
    else:
        return arg

parser = argparse.ArgumentParser(description='Convert LaTeX to speech')

parser.add_argument("-i", dest="input_filename", required=True,
                    help="input LaTeX document", metavar="FILE",
                    type=lambda x: __is_valid_file(parser, x))

parser.add_argument("-o", dest="output_filename", required=True,
                    help="output MP3 file", metavar="FILE")

# Get the arguments
args = parser.parse_args()
input_filename = str(args.input_filename)
output_filename = str(args.output_filename)

# Launch
latextotext = Pandoc()
txt = latextotext.convert_input(input_filename)

tts = AWSPolly()
tts.text_to_speech(txt, output_filename)


