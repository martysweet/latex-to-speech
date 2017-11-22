import pypandoc

from latextotext.LatexToText import LatexToText


class Pandoc(LatexToText):
    def convert_input(self, file_path):
        return pypandoc.convert_file(file_path, 'plain', format='latex')
