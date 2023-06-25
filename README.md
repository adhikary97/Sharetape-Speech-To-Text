# Sharetape-Speech-To-Text

Run speech to text for video for free. This outputs 3 files, 1 `words.json` file that has all of the words said along with their timing and confidence, 1 `transcript.txt` with just all the words read, and 1 `captions.srt` file which is the captions for that video.

## Install requirements

```
$ python3 -m venv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
```

## Download Vosk Library

This is the language library this speech to text uses. Download this [Here](https://alphacephei.com/vosk/models/vosk-model-en-us-0.42-gigaspeech.zip)

Once downloaded unzip in your project directory.

## Speech to text with video

Video must be `.mp4` or `.mov`

```
$ python main.py --video videoname.mp4
```

## Speech to text with audio

Video must be `.wav`

```
$ python main.py --audio audioname.wav
```