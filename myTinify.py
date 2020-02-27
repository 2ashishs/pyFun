import tinify

# Problem: Designers share png images in Zeplin (which are large in size) for Android app
# Solution: Take image from each sub-directory, send to TinyPNG API & save result

tinify.key = "<TingPNG_API_Key>"

dir_i = "/my/input/directory/"
dir_o = "/my/output/directory/"
dir_sub = ["drawable-hdpi/", "drawable-mdpi/", "drawable-xhdpi/", "drawable-xxhdpi/", "drawable-xxxhdpi/"]
for sub in dir_sub:
    source = tinify.from_file(dir_i+sub+"input_filename.png")
    source.to_file(dir_o+sub+"output_filename.png")