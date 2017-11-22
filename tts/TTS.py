from abc import ABCMeta, abstractmethod


class TTS:
    __metaclass__ = ABCMeta

    @abstractmethod
    def text_to_speech(self, plain_text, output_filename):
        """
        Converts a plaintext document to a speech file
        """
        pass
