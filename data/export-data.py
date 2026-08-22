"""Write the ISLP data sets the course uses to CSV.

Run once, in an environment that has ISLP installed:

    pip install ISLP
    python data/export-data.py

Students never need ISLP. Notebooks read these files straight off the course
site with pandas, which means nothing to install on Colab.
"""

import pathlib
import numpy as np
import pandas as pd
from ISLP import load_data

HERE = pathlib.Path(__file__).parent

FRAMES = [
    "Auto",
    "Boston",
    "Caravan",
    "Carseats",
    "Credit",
    "Default",
    "Hitters",
    "Smarket",
    "Wage",
]

for name in FRAMES:
    df = load_data(name)
    # a few sets carry a meaningful index, such as the car name on Auto, so it
    # is written out as an ordinary first column rather than dropped
    keep_index = df.index.name is not None
    df.to_csv(HERE / f"{name}.csv", index=keep_index)
    cols = df.shape[1] + int(keep_index)
    print(f"{name:10s} {df.shape[0]:6d} x {cols:3d}"
          + (f"   (index '{df.index.name}' kept as a column)" if keep_index else ""))

# NCI60 arrives as a dict of expression matrix plus labels, so it is flattened
# into one wide frame with the cancer type as the first column.
nci = load_data("NCI60")
wide = pd.DataFrame(np.asarray(nci["data"]))
wide.columns = [f"gene_{i}" for i in range(wide.shape[1])]
wide.insert(0, "label", list(nci["labels"].iloc[:, 0]))
wide.to_csv(HERE / "NCI60.csv", index=False)
print(f"{'NCI60':10s} {wide.shape[0]:6d} x {wide.shape[1]:3d}")
