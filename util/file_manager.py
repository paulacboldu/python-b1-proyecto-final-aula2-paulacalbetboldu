import pandas as pd

class CSVFileManager:
  def __init__(self, path:str):
    self.path = path

  def read(self) -> pd.DataFrame:
    return pd.read_csv(self.path)  
  
  def write(self, dataFrame):
    dataFrame.to_csv(self.path, index=False)