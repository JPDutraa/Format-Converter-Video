import os
import sys
from moviepy.editor import *

def convert_ts_to_mp4(ts_file, output_file):
    video = VideoFileClip(ts_file)
    video.write_videofile(output_file, codec='libx264', audio_codec='aac')


def main():
    dvd_path = "D:" # Unidade D: no Windows
    output_dir = "output"


    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    video_ts_path = os.path.join(dvd_path, "VIDEO_TS")
    if not os.path.exists(video_ts_path):
        print(f"Failed to find VIDEO_TS directory: {video_ts_path}")
        sys.exit(1)

    title_num = 1
    while True:
        ts_file_path = os.path.join(video_ts_path, f"VTS_{title_num:02d}_1.VOB")
        if not os.path.exists(ts_file_path):
            break

        output_file = os.path.join(output_dir, f"title{title_num}.mp4")
        print(f"Converting {ts_file_path} to {output_file}")
        convert_ts_to_mp4(ts_file_path, output_file)
        title_num += 1

    print("Conversion complete.")


if __name__ == "__main__":
    main()