import numpy as np
import logging
from pathlib import Path
import unittest
import urllib.request

from seistools.reader import SegyReader, bcd2dec

TEST_DATA_FOLDER = Path(__file__).parent.joinpath('data')
logger = logging.getLogger(__name__)


class TestBcd(unittest.TestCase):

    def test_bcd2dec(self):
        assert np.isnan(bcd2dec(12))
        assert bcd2dec(22) == 16
        assert bcd2dec(np.array([1, 22])) == 116


class TestReaderSegy(unittest.TestCase):

    def setUp(self) -> None:
        self.segy_file_int = TEST_DATA_FOLDER.joinpath('l10f1.sgy')
        if not self.segy_file_int.exists():
            logger.warning(f'Downloading {self.segy_file_int}')
            urllib.request.urlretrieve(
                "https://pubs.usgs.gov/of/1999/of99-449/disc2/seg_y/l10f1.sgy",
                self.segy_file_int
            )

    def test_segy_int(self):
        sr = SegyReader(self.segy_file_int)
        data, th = sr.read()
        assert data.shape == (100, 10000) == (sr.ntr, sr.ns)

    def test_segy_float(self):
        segy_file = "/Users/olivier/Documents/datadisk/das/segy_samples/" \
                    "q004d_lmostack_a1_prm1_rl68.sgy"
        sr = SegyReader(segy_file)
        assert sr.si == .002
        data, th = sr.read()
        assert data.shape == (96, 151) == (sr.ntr, sr.ns)
        # from easyqc.gui import viewseis
        # eqc = viewseis(data.view('<f'), sr.si)


if __name__ == '__main__':
    unittest.main()
