import peddesign as pd
#print(sys.path)

# Design CT
pd.design_ct("whole_abd", "younger_child", 6, "delay", 65)

# Design Chest
pd.design_chest("younger_child", 12)