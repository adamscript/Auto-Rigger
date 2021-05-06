import sys
import importlib
sys.path.append('C:/Users/HP/Awan-Auto-Rigger/modules')

from guides import *
from rig import *
from gui import *
#from picker import *

importlib.reload(guides)
importlib.reload(rig)
importlib.reload(gui)