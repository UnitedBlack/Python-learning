import os


def clear(directory):
    hueta = "[SW.BAND] "

    for name in os.listdir(directory):
        path = os.path.join(directory, name)
        for folder_name in os.listdir(path):
            path_dir = f"{path}/{folder_name}"
            print()
            if hueta in path_dir:
                old_filename = os.path.basename(path_dir)
                new_filename = old_filename.replace(hueta, "")
                os.rename(path_dir, new_filename)


clear("FilesToClear")
