import os
import tempfile
from time import sleep
import boto3

from tts.TTS import TTS
from pydub import AudioSegment
from contextlib import closing


class AWSPolly(TTS):
    def __init__(self):
        # Create a polly client using default settings
        self.client = boto3.client('polly')

    def text_to_speech(self, plain_text, output_filename):
        responses = []

        words = plain_text.split()
        words.reverse()
        current_seg = ""

        while len(words) > 0:
            word = words.pop()

            # If we have gone over the boundary, process the word
            if len(current_seg) + len(word) > 1500:
                # Push the last word back onto the stack and remove the word
                words.append(word)
                # Process the element
                responses.append(self.__synthesize_speech(current_seg))
                # Cleanup segment
                current_seg = ""
            else:
                current_seg = current_seg + " " + word

            # Catch any left over words
            if len(words) == 0 and len(current_seg) > 0:
                responses.append(self.__synthesize_speech(current_seg))

        # Merge all the responses
        self.__merge_responses(responses, output_filename)

    def __synthesize_speech(self, text_input):
        sleep(0.1)
        print("Sending request to AWS Polly. Size: {}".format(len(text_input)))
        response = self.client.synthesize_speech(
            OutputFormat='mp3',
            SampleRate='22050',
            Text=text_input,
            TextType='text',
            VoiceId='Amy'
        )
        return response

    @staticmethod
    def __merge_responses(responses, output_filename):

        print("Saving the response to disk...")

        # AudioSegments
        audio_segments = []

        # Save each response to disk in order
        with tempfile.TemporaryDirectory() as dirname:
            for response in responses:
                if "AudioStream" in response:
                    with closing(response["AudioStream"]) as stream:
                        data = stream.read()
                        temp_filename = os.path.join(dirname, 'tempmp3')
                        fp = open(temp_filename, 'wb')
                        fp.write(data)
                        fp.close()
                        audio_segments.append(AudioSegment.from_mp3(temp_filename))
                else:
                    print("Bad/Empty response from AWS Polly")

        # Merge all the responses into one
        if len(audio_segments) > 0:
            merged_audio = audio_segments[0]
            for index, item in enumerate(audio_segments):
                if index != 0:
                    merged_audio = merged_audio + item

            # Save the merged audio
            merged_audio.export(output_filename, format="mp3")
        else:
            print("No audio segments to process")
