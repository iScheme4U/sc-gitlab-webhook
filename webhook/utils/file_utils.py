"""File utilities

Copyright (c) 2021 Scott Lau
"""

import os


def ensure_dir(file_path):
    directory = os.path.dirname(file_path)
    if not os.path.exists(directory):
        os.makedirs(directory)
