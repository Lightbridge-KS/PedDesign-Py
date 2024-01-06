import sys
from pathlib import Path

sys.path.insert(1, str(Path(".").absolute() / 'src'))

# print(Path(".").absolute()) # Project Root

import peddesign as pd

pd.design_ct("whole_abd", "younger_child", 6)
