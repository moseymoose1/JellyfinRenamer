import os
import sys
import re


def extract_episode_info(filename):
    # match the pattern of season number and episode number
    pattern = r"S(\d{2})E(\d{2})[E-]?(\d{2})?"
    match = re.search(pattern, filename, re.IGNORECASE)

    if match:
        season_number = match.group(1)
        episode_number = match.group(2)
        if match.group(3):
            episode_number += f"-{match.group(3)}"
    else:
        season_number = None
        episode_number = None

    # check if the filename contains part information
    part_match = re.search(r"(part|pt)\.? ?(\d+|one)", filename, re.IGNORECASE)
    if part_match:
        part_number = part_match.group(2)
        part_suffix = f" Part{part_number}"
    else:
        part_suffix = ""

    return season_number, episode_number, part_suffix


def is_video_file(filename):
    # check if file is a video file
    video_extensions = {".mp4", ".avi", ".mkv", ".wmv", ".flv", ".m4v"}
    extension = os.path.splitext(filename)[1].lower()
    return extension in video_extensions


def validate_tags(tags_input):
    if not tags_input:
        return ""

    if not re.match(r"^\w+(;\w+)*$", tags_input):
        raise ValueError("Tags must be alphanumeric and separated by semicolons.")

    # split tags by semicolon and add square brackets around each tag
    tags = "[" + "][".join(tags_input.split(";")) + "]"
    # add a space between the episode pattern and the open square bracket
    return " " + tags


def main():
    folder_path = input("Enter the folder path: ")

    tags_input = input("Enter tags separated by ';', or leave blank for no tags: ")
    tags = ""

    try:
        tags = validate_tags(tags_input)
    except ValueError as e:
        print(e)
        sys.exit(1)

    # get a list of all files in the specified folder
    files = os.listdir(folder_path)

    # generator expression to filter video files
    video_files = (f for f in files if is_video_file(os.path.join(folder_path, f)))

    for file in video_files:
        old_path = os.path.join(folder_path, file)

        # extract episode information from file name
        season_number, episode_number, part_suffix = extract_episode_info(file)

        if season_number and episode_number:
            if "-" in episode_number:
                new_file_name = f"Episode S{season_number}E{episode_number}{part_suffix}{tags}{os.path.splitext(file)[1]}"
            else:
                new_file_name = f"Episode S{season_number}E{episode_number}{part_suffix}{tags}{os.path.splitext(file)[1]}"
            new_path = os.path.join(folder_path, new_file_name)

            # rename file
            os.rename(old_path, new_path)
            print(f"Renamed '{file}' to '{new_file_name}'")
        else:
            print(f"Could not extract episode information from '{file}'")

    print("Finished renaming files.")


if __name__ == "__main__":
    main()
    
              # ask user if they want to rename another folder
    another_folder = input("Would you like to rename another folder? (Enter 'y' or 'n') ")
    while another_folder.lower() == "y":
        main()
        another_folder = input("Would you like to rename another folder? (Enter 'y' or 'n') ")
    else:
        sys.exit(0)
        