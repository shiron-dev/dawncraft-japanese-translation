import shutil
import os
import util

def copy(src: str, dist: str):
  dist_path = os.path.join(util.tmp_dir, dist)
  shutil.copy2(src, dist_path)

def cp_tree(src: str, dist: str):
  dist_path = os.path.join(util.tmp_dir, dist)
  shutil.copytree(src, dist_path)
