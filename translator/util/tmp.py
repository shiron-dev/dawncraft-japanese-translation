import tempfile
import shutil

def mk_tmp():
    return tempfile.mkdtemp()

def rm_tmp():
    shutil.rmtree(tmp_dir)

tmp_dir = mk_tmp()
