from seistools.reader import SegyReader
sgy_file = '/datadisk/Echo/tests/segy/00063102.sgy'
sr = SegyReader(sgy_file)
data, th = sr.read()

# to run this line, `pip install easyqc` is necessary. Will add pyqt5 and scipy to environment
from easyqc.gui import viewseis  # noqa
eqc = viewseis(data, sr.si)
