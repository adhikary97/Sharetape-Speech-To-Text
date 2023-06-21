# Sharetape-Speech-To-Text

Run speech to text for video for free.

## Install requirements
```
$ python3 -m venv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
```

## Install Vosk Library
This is the language library this speech to text uses. Download this [Here](https://alphacephei.com/vosk/models/vosk-model-en-us-0.42-gigaspeech.zip)

Once downloaded unzip in your project directory.

## Speech to text
Video must be `.mp4` or `.mov`

```
$ python main.py --video videoname.mp4
```


