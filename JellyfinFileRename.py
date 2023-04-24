import os
import sys
import re

# function to extract season number and episode number from filename
def extract_episode_info(filename):
    # match the pattern of season number and episode number
    pattern = r"S(\d{2})E(\d{2})"
    match = re.search(pattern, filename)

    if match:
        season_number = match.group(1)
        episode_number = match.group(2)
        return season_number, episode_number
    else:
        return None, None

# main function
def main():
    # get folder path and tags from user input
    folder_path = input("Enter the folder path: ")
    tags_input = input("Enter tags separated by ';': ")

    # check if tags are provided
    if tags_input:
        # split tags by semicolon and add square brackets around each tag
        tags = "[" + "][".join(tags_input.split(";")) + "]"
    else:
        # if no tags provided, set tags to empty string
        tags = ""

    # get a list of all files in the specified folder
    files = os.listdir(folder_path)

    # loop through each file and rename if it matches the pattern
    for filename in files:
        # get the current file path
        current_path = os.path.join(folder_path, filename)

        # check if file is a directory
        if not os.path.isdir(current_path):
            # extract season number and episode number from filename
            season_number, episode_number = extract_episode_info(filename)

            # check if season number and episode number exist
            if season_number and episode_number:
                # create new filename with season number, episode number, and tags
                new_filename = f"Episode S{season_number}E{episode_number} {tags}.mp4"

                # create new file path
                new_path = os.path.join(folder_path, new_filename)

                # rename the file
                os.rename(current_path, new_path)

                # print success message
                print(f"{filename} renamed to {new_filename}")
            else:
                # print error message
                print(f"{filename} does not match the pattern SXXEXX and was not renamed")

    # print completion message
    print("All files completed.")

if __name__ == "__main__":
    main()



