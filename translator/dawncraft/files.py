import os
import shutil
import util

def copy_to_working(source: str, paths: list[str]):
  for dawn_path in paths:
    path = os.path.join(source, dawn_path)
    util.cp_tree(path, dawn_path)
