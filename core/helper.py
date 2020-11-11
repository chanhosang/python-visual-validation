from pathlib import Path


def get_resources_dir_path():
    return str(Path(__file__).parent.parent.resolve()) + '/resources'


def get_libs_dir_path():
    return str(Path(__file__).parent.parent.resolve()) + '/libs'

