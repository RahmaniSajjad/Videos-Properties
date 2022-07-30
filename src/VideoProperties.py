# Import necessary libraries
import cv2
import os


# <================================================================>

#           Source : https://github.com/RahmaniSajjad

# <================================================================>


def get_video_properties(video_dir):
    """this function returns properties of a video

    Parameters:
    video_dir (string): video's directory

    Returns:
    dict : a dictionary of properties included{
                width, height, length_sec, length, fps, dir, type, size_byte, size
                }

   """

    # Read video using opencv
    video = cv2.VideoCapture(video_dir)

    # Get fps(frame per second) of video
    fps = video.get(cv2.CAP_PROP_FPS)

    # Get length of video ( frame / (frame / second) = second )
    length_sec = video.get(cv2.CAP_PROP_FRAME_COUNT) / fps

    # Get size of video
    size_byte = os.path.getsize(video_dir)

    properties = {
        "width": round(video.get(cv2.CAP_PROP_FRAME_WIDTH)),
        "height": round(video.get(cv2.CAP_PROP_FRAME_HEIGHT)),
        "length_sec": round(length_sec),
        "length": convert_length(length_sec),
        "fps": round(fps),
        "dir": video_dir,
        "type": video_dir.split('.')[-1],  # D:\Sajjad\Videos\video.mkv --> mkv
        "size_byte": round(size_byte),
        "size": convert_size(size_byte)
    }
    return properties


def convert_size(size):
    """Example : 2_000_000_000  -->  1.86 GB

        Parameters:
        size (int): file size in bit

        Returns:
        string: file size

    """

    # Defining KB & MB & GB
    K, M, G = 1024, 1024 ** 2, 1024 ** 3

    if size >= G:
        return str(round(size / G, 2)) + ' GB'
    elif size >= M:
        return str(round(size / M, 2)) + ' MB'
    elif size >= K:
        return str(round(size / K, 2)) + ' KB'
    else:
        return str(size) + ' Bytes'


def convert_length(length):
    """Example : 20_000  -->  05:33:20

            Parameters:
            length (int): length in second

            Returns:
            string: length in hh:mm:ss

    """

    # calculate hours & minutes & seconds
    m, s = divmod(length, 60)
    h, m = divmod(m, 60)

    return f"{int(h):02}:{int(m):02}:{int(s):02}"


def get_all_video_properties(directory):
    """this function returns properties of all video in given directory

        Parameters:
        directory (string): given directory

        Returns:
        list, list: list of all video in given directory,
                        list of all videos properties

    """

    global valid_format
    videos = []
    videos_properties = []

    # Get all sub-folders in given directory
    all_directories = [folder_dir[0] for folder_dir in os.walk(directory)]

    for directory in all_directories:
        try:
            # Get all file in a folder
            files = os.listdir(directory)
        except PermissionError:
            os.system("")  # for colored text in command line
            print('\033[93m' + f"|--> Can't Access to {directory} <---|" + '\033[0m')
            return videos, videos_properties

        for file in files:
            if file.split('.')[-1] in valid_format:  # file.split('.')[-1] --> File format

                # Append to videos list
                videos.append(directory + "\\" + file)

                # Append to videos properties list
                videos_properties.append(get_video_properties(directory + "\\" + file))

    # Return result
    return videos, videos_properties


# File format that you want to calculate
valid_format = ["mp4", "mkv", "wmv"]
