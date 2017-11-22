from abc import ABCMeta, abstractmethod


class LatexToText:
    __metaclass__ = ABCMeta

    @abstractmethod
    def convert_input(self, file_path):
        """
        Converts a LaTeX document to plaintext
        :rtype: string Plaintext object to convert into speech
        """
        pass
