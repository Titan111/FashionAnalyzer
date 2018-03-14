import numpy as np
from lightning import Lightning
lgn = Lightning(local=True)
connections = np.matrix("0 0 0 1;0 0 0 0;0 0 0 0;0 0 0 0")
lgn.circle(connections)
