import pathlib
import subprocess
import json

def get_video_codec_ffprobe(file_paths:list):
    """
    Function to display .mp4 video codecs which are not h264 

    Args:
        file_paths: list of file paths
    """

    for i in file_paths:

        try:
            command = [
                'ffprobe',
                '-v', 'error',
                '-select_streams', 'v:0',                                       # select first video stream
                '-show_entries', 'stream=codec_name',
                '-of', 'json',
                str(i)
            ]
            result = subprocess.run(command, capture_output=True, 
                                    text=True, check=True)
            data = json.loads(result.stdout)
            
            if 'streams' in data and len(data['streams']) > 0:
                if data['streams'][0]['codec_name']!="h264":
                    print(i, "\t", data['streams'][0]['codec_name'])
            else:
                return "No video stream found"
            
        except subprocess.CalledProcessError as e:
            return f"Error running ffprobe: {e}"
        
        except FileNotFoundError:
            return "ffprobe not found. Please ensure FFmpeg is installed and added to PATH."
        
        except json.JSONDecodeError:
            return "Error parsing ffprobe output."


if __name__=="__main__":

    file_dir = pathlib.Path("Add path here")
    filenames = list(file_dir.glob("*.mp4"))
    get_video_codec_ffprobe(filenames)

