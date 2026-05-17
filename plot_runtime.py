import os
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent
MPLCONFIG_DIR = BASE_DIR / ".mplconfig"
OUTPUT_DIR = BASE_DIR / "outputs"

MPLCONFIG_DIR.mkdir(exist_ok=True)
OUTPUT_DIR.mkdir(exist_ok=True)
os.environ["MPLCONFIGDIR"] = str(MPLCONFIG_DIR)

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt


def save_current_figure(filename):
    plt.savefig(OUTPUT_DIR / filename, bbox_inches="tight")
    plt.close()
