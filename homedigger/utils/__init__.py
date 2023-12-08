import sys
from pathlib import Path

x = Path(__file__).parent.parent.parent.as_posix()
sys.path.append(x)
