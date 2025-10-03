### import library
from pathlib import Path
import sys

### get script folder
FP_THIS_FILE = Path(__file__).resolve()
FD_PRJ = FP_THIS_FILE.parent.parent
FD_EXE = FD_PRJ / "scripts"

### put scripts/ on sys.path
txt_path = str(FD_EXE)
if txt_path not in sys.path:
    sys.path.insert(0, txt_path)

### Import the config and expose it
import config_project_sing as config