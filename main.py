import argparse
import logging
import os
import uuid

from vosk import Model, SetLogLevel

from sharetape import Sharetape


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-v", "--video", type=str, required=True)
    args = parser.parse_args()
    video_id = str(uuid.uuid4())

    model = Model(
        model_path="/Users/parasadhikary/Downloads/scratch_s2t/vosk-model-en-us-0.42-gigaspeech"
    )
    SetLogLevel(0)
    logging.info("sp2t setup")

    os.makedirs(f"{video_id}")

    shartape = Sharetape(
        args.video,
        f"{video_id}/audio.wav",
        f"{video_id}/mono_audio.wav",
        f"{video_id}/transcript.txt",
        f"{video_id}/words.json",
        f"{video_id}/subtitles.srt",
        model,
    )
    shartape.extract_transcript()


if __name__ == "__main__":
    main()
