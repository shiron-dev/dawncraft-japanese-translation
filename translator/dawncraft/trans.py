import dawncraft
import util
import os
import tempfile
import json

COPY_PATHS = [
  "config/dcclasses/assets/dawncraft/lang",
  "config/ftbquests/quests",
  "global_packs/required_data/DawnCraft_Datapack/data/quest_giver/quests",
]

out_dir = tempfile.mkdtemp()

def trans(work_path: str):
  dawncraft.copy_to_working(work_path, COPY_PATHS)

  ex_kv = dawncraft.extract_key_value_pairs(get_in_path("config/dcclasses/assets/dawncraft/lang/en_us.json"))
  for key, value in ex_kv:
    util.set_trans_text(key, value)

  trans_path = util.write_data()
  input(f"plz translate {trans_path} then press enter to continue...")
  util.read_data()

  en_path = get_in_path("config/dcclasses/assets/dawncraft/lang/en_us.json")
  ja_path = get_out_path("config/dcclasses/assets/dawncraft/lang/ja_jp.json")
  with open(en_path, "r") as fr, open(ja_path, "w") as fw :
      ja_json = json.load(fr)
      for key, _ in ex_kv:
        ja_json[key] = util.get_trans_text(key)
        print(util.get_trans_text(key))
      json.dump(ja_json, fw, ensure_ascii=False, indent=2)
  print(ja_path)

def get_in_path(file_path: str):
  return os.path.join(util.tmp_dir, file_path)
def get_out_path(file_path: str):
  return os.path.join(util.tmp_dir, file_path)
