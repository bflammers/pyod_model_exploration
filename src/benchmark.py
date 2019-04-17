
import json
import os

from time import gmtime, strftime

import pandas as pd
import numpy as np

from pyod.models.abod import ABOD
from pyod.models.cblof import CBLOF
from pyod.models.feature_bagging import FeatureBagging
from pyod.models.hbos import HBOS
from pyod.models.iforest import IForest
from pyod.models.mcd import MCD
from pyod.models.ocsvm import OCSVM
from pyod.models.pca import PCA



from src.dataloading import DataLoader, download_all

class BenchMark:

    def __init__(self, dataset_exclude=None, model_exclude=None,
                 output_dir=None):

        self.output_dir = self._set_output_dir(output_dir)
        self.datasets = download_all(dataset_exclude)

        # TODO: copy from https://github.com/yzhao062/pyod/blob/master/notebooks/benchmark.py
        # TODO: same format as https://pyod.readthedocs.io/en/latest/benchmark.html




    @staticmethod
    def _set_output_dir(output_dir):

        if output_dir is None:
            suffix = strftime("%Y-%m-%d-%H-%M", gmtime())
            output_dir = os.path.join("../benchmark", suffix)

        os.makedirs(output_dir, exist_ok=True)

        return output_dir







if __name__ == "__main__":

    datasets = download_all()

    print(datasets)

    benchmark = BenchMark(output_dir="../benchmark")

    print('0')
