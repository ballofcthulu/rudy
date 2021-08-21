import json
import sys

class Config:
  def __init__(self, filepath: str):
    self.filepath = filepath

    try:
      with open(filepath, "r") as f:
        self.__dict__.update(json.load(f))
    except:
      print("Unable to open config file! {path}".format(path=self.filepath))
      sys.exit(1)
