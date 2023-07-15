import sys
sys.path.insert(1, '..') # '/Users/kittipos/Documents/Radio-local/rad-proj/PedDesign-Py'
# print(sys.path)
import peddesign as pd


# Design CT
pd.design_ct("whole_abd", "younger_child", 6, "delay", 65)

# Design Chest
pd.design_chest("younger_child", 12)