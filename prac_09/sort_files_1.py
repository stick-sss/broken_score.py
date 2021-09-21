import os
import shutil


def main():
    os.chdir('FilesToSort')
    for filename in os.listdir('.'):
        if os.path.isdir(filename):
            continue
        file_type = filename.split(".")[-1]
        try:
            os.mkdir(file_type)

        except FileExistsError:
            pass

        if file_type in filename:
            shutil.move(filename, file_type)


main()








