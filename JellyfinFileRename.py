import os
import sys
import re


def extract_episode_info(filename):
    # match the pattern of season number and episode number
    pattern = r"S(\d{2})E(\d{2})"
    match = re.search(pattern, filename, re.IGNORECASE)

    if match:
        season_number = match.group(1)
        episode_number = match.group(2)
        return season_number, episode_number
    else:
        return None, None


def is_video_file(filename):
    # check if file is a video file
    video_extensions = {".mp4", ".avi", ".mkv", ".wmv", ".flv", ".m4v"}
    extension = os.path.splitext(filename)[1].lower()
    return os.path.isfile(filename) and extension in video_extensions


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

    for filename in [f for f in files if is_video_file(os.path.join(folder_path, f))]:
        season_number, episode_number = extract_episode_info(filename)

        if season_number and episode_number:
            # create new filename with season number, episode number, and tags
            new_filename = f"Episode S{season_number}E{episode_number}{tags}.mp4"

            # create new file path
            new_path = os.path.join(folder_path, new_filename)

            # rename the file
            os.rename(os.path.join(folder_path, filename), new_path)

            # print success message
            print(f"{filename} renamed to {new_filename}")
        else:
            # print error message
            print(f"{filename} does not match the pattern SXXEXX and was not renamed")

    # print completion message
    print("All files completed.")


if __name__ == "__main__":
    main()
