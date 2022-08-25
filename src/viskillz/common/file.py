import os
import shutil


def list_files(path: str, extension: str = None, include_path: bool = False) -> list[str]:
    """
    Returns names of files that are located in the given directory and have the given extension.
    :param path: path of the directory
    :param extension: extension of the files
    :param include_path: whether include path
    :return: names of the files
    """
    return [name if not include_path else os.path.join(path, name) for name in os.listdir(path) if
            extension is None or name.endswith("." + extension)]


def init_dir(path, delete=True):
    if delete:
        try:
            shutil.rmtree(path)
        except FileNotFoundError:
            pass
    os.makedirs(path, exist_ok=True)
