# Import necessary libraries
from src import VideoProperties as vp

# <================================================================>

#           Source : https://github.com/RahmaniSajjad

# <================================================================>

videos, videos_properties = [], []

while True:
    print("\n" + "-" * 50 + "\n")

    if len(videos) + len(videos_properties) != 0:
        reset = input("Reset? (y for YES else for NO) ") == 'y'
        if reset:
            videos, videos_properties = [], []

    # Getting path from input
    dir_files = input("Enter Dir : ")

    is_deep = input("Is Deep? (y for YES else for NO) ") == 'y'
    print()

    # Setting files formats that you want to calculate
    vp.valid_format = ["mp4", "mkv", "wmv"]

    # Getting all videos and all videos properties in given path
    result = vp.get_all_video_properties(dir_files, is_deep)

    # Loop in video's 'directory + name'
    for i in range(len(result[0])):
        if result[0][i] not in videos:
            videos.append(result[0][i])
            videos_properties.append(result[1][i])

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
