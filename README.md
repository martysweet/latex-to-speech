# Latex to Speech

This tool is designed to allow the easy proof reading of documents. 
Often mistakes can go unnoticed if you are proof reading your own work,
having someone (or a speech tool) read out the text can drastically
increase the amount of errors you catch.

## Requirements
- pandoc
- ffmpeg or avconv
- Python 3.6
- AWS account

## Usage

Options:
```
-i              the input LaTeX file
-o              output filename of the MP3 file
TODO: (--tts)         text to speech integration to use (see below) - default is aws_polly
TODO: (--converter)   LaTex to text convertor to use
```

If you have no default AWS profile, one can be set before invoking the tool:
```bash
$ export AWS_PROFILE="MyProfile"
$ python main.py -i example.tex -o output.mp3
```

## Integrations
This small program is modular to allow for other integrations to be added.
By default, AWS Polly is used to generate speech from an inputted LaTeX file.

### Latex to Plaintext
- Pandoc

### Text to Speech
- AWS Polly (aws_polly)
