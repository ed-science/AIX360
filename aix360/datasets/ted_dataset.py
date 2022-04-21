import os,sys

import pandas as pd


class TEDDataset():
    """
    The goal of this synthetic dataset is to predict employee attrition from a
    fictious company.  The dataset is generated by a python file called
    ``GenerateData.py`` in the ``aix360/data/ted_data/`` directory.

    Like most datasets, each instance consists of a feature vector and a Y
    label, which represents whether the employee associated with the feature
    vector will leave the company.  However, unlike most datasets, each instance
    will also have an Explanation (E). This is motivated by the TED framework,
    which requires explanations in its training data, but can be used by other
    explainability algorithms as a metric for explainability.

    See also:
        * AIES'19 paper by Hind et al. [#]_ for more information on the TED
          framework.
        * The tutorial notebook ``TED_Cartesian_test.ipynb`` for information
          about how to use this dataset and the TED framework.
        * ``GenerateData.py`` for more information on how the dataset is
          generated or to created a tailored version of the dataset.

    References:
        .. [#] `Michael Hind, Dennis Wei, Murray Campbell, Noel C. F. Codella,
           Amit Dhurandhar, Aleksandra Mojsilovic, Karthikeyan Natesan Ramamurthy,
           Kush R. Varshney, "TED: Teaching AI to Explain its Decisions,"
           AAAI /ACM Conference on Artificial Intelligence, Ethics,
           and Society (AIES-19), 2019.
           <http://www.aies-conference.com/wp-content/papers/main/AIES-19_paper_128.pdf>`_
    """

    def __init__(self, dirpath=None):
        self._dirpath = dirpath
        if not self._dirpath:
            self._dirpath = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                '..', 'data','ted_data')


    def load_file(self, fileName='Retention.csv'):
        """ Open dataset file and populate X, Y, and E

        Args:
            fileName (String) : filename of dataset, a structured (CSV) dataset where

                - The first N-2 columns are the features (X).
                - The next to last column is the label (Y) {0, 1}
                - The last column gives the explanations (E) {0, 1, ..., MaxE}.  We assume the explanation space
                  is dense, i.e., if there are MaxE+1 unique explanations, they will be given IDs from 0 .. MaxE
                - first row contains header information for each column and should be "Y" for labels and "E" for explanations
                - each row is an instance
        Returns:
            tuple:
                * **X** -- list of features vectors
                * **Y** -- list of labels
                * **E** -- list of explanations
        """
        self._filepath = os.path.join(self._dirpath, fileName)

        try:
            data = pd.read_csv(self._filepath)
            X = data.iloc[:,:-2]   # Choose all rows and all cols, except for the last 2 cols
            Y = data['Y']          # Choose col with header 'Y'
            E = data['E']          # Choose col with header 'E'

            return X, Y, E

        except IOError as err:
            print(f"IOError: {err}")
            sys.exit(1)
