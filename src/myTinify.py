import tinify

# Problem: Designers share png images in Zeplin (which are large in size) for Android app
# Solution: Take image from each sub-directory, send to TinyPNG API & save result

# Set below values as per need
tinify.key = "<TingPNG_API_Key>"
dir_i = "/my/input/directory/"
dir_o = "/my/output/directory/"
dir_s = ["drawable-hdpi/", "drawable-mdpi/", "drawable-xhdpi/", "drawable-xxhdpi/", "drawable-xxxhdpi/"]
i_file = "input_filename.png"
o_file = "output_filename.png"


def subdirectory(input_dir, output_dir, sub_dir_list, input_filename, output_filename):
    # Case 1: Same name input_file from multiple subdirectories
    for sub_dir in sub_dir_list:
        source = tinify.from_file(input_dir + sub_dir + input_filename)
        source.to_file(output_dir + sub_dir + output_filename)


subdirectory(dir_i, dir_o, dir_s, i_file, o_file)   # EITHER use this


def single_file(input_dir, output_dir, input_filename, output_filename):
    # Case 2: Single input_file
    source = tinify.from_file(input_dir + input_filename)
    source.to_file(output_dir + output_filename)


single_file(dir_i, dir_o, i_file, o_file)     # OR use this
