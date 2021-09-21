import os
import shutil

def main():
    global categoris_name
    os.chdir('FilesToSort')
    type_categoris = {"Spreadsheets": {"xls", "xlsx"}, "Images": {"jpg", "png", "gif"}, "Docs": {"txt", "docx", "doc"}}
    for key in type_categoris:
        try:
            os.mkdir("{}".format(key))
        except FileExistsError:
            pass

    for value in type_categoris.values():
        for i in value:
            print("What category would you like to sort {} files into?".format(i),end="")
            categoris_name = input(" ")

        for filename in os.listdir('.'):
            if os.path.isdir(filename):
                continue
            file_type = filename.split(".")[-1]
            if file_type in type_categoris[categoris_name]:
                shutil.move(filename, categoris_name)













main()