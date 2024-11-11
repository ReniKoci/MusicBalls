# Used to rename the sounds file to match the keynotes
# sounds file: https://freesound.org/people/TEDAgame/packs/25405/
import os

st = "tedagame__"
path = "./Sounds"
for file in os.listdir(path):

    index = file.find(st)
    if index != -1:
        os.rename(path + "/" + file, path + "/" + file[index + len(st):])