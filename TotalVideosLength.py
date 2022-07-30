# Import necessary libraries
from src import VideoProperties as vp

# <================================================================>

#           Source : https://github.com/RahmaniSajjad

# <================================================================>


# Getting path from input
dir_files = input("Enter Dir : ")

# Getting all videos and all videos properties in given path
videos, videos_properties = vp.get_all_video_properties(dir_files)

# keeping total video's length (second)
total_time = 0

for i in range(len(videos)):
    # Printing all videos with length
    print(f"{i + 1}) {videos[i]}  :  {videos_properties[i]['length']}")

    # Adding video length to total videos length
    total_time += videos_properties[i]['length_sec']

# Printing number of videos in given directory
print(f"\n--- Number of Movies : {len(videos)}")

# Printing converted total videos length
print(f"--- Total Time : {vp.convert_length(total_time)}")
