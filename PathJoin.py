import os


def path_join(dir_path):
    FileList = os.listdir(dir_path)
    PathList =[]

    for FileName in FileList:
        FilePath = os.path.join(dir_path, FileName)
        PathList.append(FilePath)
    return PathList


if __name__ == '__main__':
    dir_path = './java-jar/'
    print(path_join(dir_path))
