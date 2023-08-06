import os
import pandas as pd


test_dir = os.path.dirname(os.path.abspath(__file__))

# testing files
f1 = pd.read_csv(os.path.join(test_dir, "f1.csv"))
f2 = pd.read_csv(os.path.join(test_dir, "f2.csv"))
f3 = pd.read_excel(os.path.join(test_dir, "f3.xls"), skiprows=[0])
f4 = pd.read_excel(os.path.join(test_dir, "f4.xls"), skiprows=[0])
