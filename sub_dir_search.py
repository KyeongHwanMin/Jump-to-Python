import os


def search(dirname):
    try:
        filenames = os.listdir(dirname)
        for filenames in filenames:
            full_filename = os.path.join(dirname, filenames)
            if os.path.isdir(full_filename): # 재귀 함수
                search(full_filename)
            else :
                ext = os.path.splitext(full_filename)[-1] # 마지막꺼 출력
                if ext == ".py":
                    print(full_filename)
    except PermissionError:
        pass

search("d:/")
