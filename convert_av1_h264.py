import pathlib
import subprocess
import json
import re
from tqdm import tqdm

def get_video_codec(file_path:pathlib.Path)->tuple[str, None]:
    """
    Function for retrieving video codec

    Args:
        file_path: Path to video file

    Returns:
        Video codec if found, else return None
    """

    command = [
        'ffprobe',
        '-v', 'error',
        '-select_streams', 'v:0',
        '-show_entries', 'stream=codec_name',
        '-of', 'json',
        str(file_path)]
    
    try:
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        data = json.loads(result.stdout)
        if 'streams' in data and len(data['streams']) > 0:
            return data['streams'][0]['codec_name']
        
    except Exception as e:
        print(f"Error checking codec: {e}")

    return None

def get_video_duration(file_path):
    command = [
        'ffprobe',
        '-v', 'error',
        '-show_entries', 'format=duration',
        '-of', 'default=noprint_wrappers=1:nokey=1',
        str(file_path)
    ]
    try:
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        return float(result.stdout.strip())
    except Exception as e:
        print(f"Error getting duration: {e}")
    return None

def convert_to_h264_nvenc(input_path:pathlib.Path, output_path:pathlib.Path):
    total_duration = get_video_duration(input_path)
    if not total_duration:
        print(f"Skipping {input_path.name} due to missing duration info.")
        return

    command = [
        'ffmpeg',
        '-y',                                   # Overwrite output if it exists
        '-i', str(input_path),
        '-c:v', 'h264_nvenc',
        '-preset', 'p7',
        '-rc', 'constqp',
        '-qp', '18',
        '-c:a', 'copy',
        str(output_path)
    ]

    process = subprocess.Popen(command, stderr=subprocess.PIPE, stdout=subprocess.DEVNULL, universal_newlines=True)

    pattern = re.compile(r'time=(\d+):(\d+):(\d+)\.(\d+)')
    pbar = tqdm(total=total_duration, unit="s", desc=input_path.name[:30], ncols=100)

    for line in process.stderr:
        match = pattern.search(line)
        if match:
            h, m, s, ms = map(int, match.groups())
            current_time = h * 3600 + m * 60 + s + ms / 100
            pbar.n = min(current_time, total_duration)
            pbar.refresh()

    process.wait()
    pbar.n = total_duration
    pbar.refresh()
    pbar.close()

    if process.returncode == 0:
        print(f"Converted: {input_path.name}")
    else:
        print(f"Failed: {input_path.name}")

if __name__ == "__main__":
    input_dir = pathlib.Path(r"Add path here")
    output_dir = input_dir / "converted"
    output_dir.mkdir(exist_ok=True)

    for video_file in input_dir.glob("*.mp4"):
        codec = get_video_codec(video_file)
        if codec != "h264":
            output_file = output_dir / video_file.name
            print(f"Converting {video_file.name} to H.264...")
            convert_to_h264_nvenc(video_file, output_file)
        else:
            print(f"{video_file.name} already in H.264. Skipping.")
