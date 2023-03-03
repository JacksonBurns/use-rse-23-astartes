import os
import sys
import unittest

import numpy as np

from astartes import train_test_split
from astartes.samplers import SPXY
from astartes.utils.warnings import ImperfectSplittingWarning


class Test_SPXY(unittest.TestCase):
    """
    Test the various functionalities of SPXY.
    """

    @classmethod
    def setUpClass(self):
        """Convenience attributes for later tests."""
        self.X = np.array(
            [
                [1, 0, 0, 0, 0, 0, 0],
                [1, 1, 0, 0, 0, 0, 0],
                [1, 1, 1, 0, 0, 0, 0],
                [1, 1, 1, 1, 0, 0, 0],
                [1, 1, 1, 1, 1, 1, 0],
                [1, 1, 1, 1, 1, 1, 1],
            ]
        )
        self.y = np.array([1, 2, 3, 4, 5, 6])
        self.labels = np.array(
            [
                "one",
                "two",
                "three",
                "four",
                "five",
                "six",
            ]
        )

    def test_spxy_sampling(self):
        """Use spxy in the train_test_split and verify results."""
        with self.assertWarns(ImperfectSplittingWarning):
            (
                X_train,
                X_test,
                y_train,
                y_test,
                labels_train,
                labels_test,
                clusters_train,
                clusters_test,
            ) = train_test_split(
                self.X,
                self.y,
                labels=self.labels,
                test_size=0.7,
                train_size=0.3,
                sampler="spxy",
                hopts={
                    "metric": "euclidean",
                },
            )
        # test that the known arrays equal the result from above
        self.assertIsNone(
            np.testing.assert_array_equal(
                X_train,
                np.array(
                    [
                        [1, 0, 0, 0, 0, 0, 0],
                        [1, 1, 1, 1, 1, 1, 1],
                        [1, 1, 0, 0, 0, 0, 0],
                        [1, 1, 1, 0, 0, 0, 0],
                    ]
                ),
                "Train X incorrect.",
            ),
        )
        self.assertIsNone(
            np.testing.assert_array_equal(
                X_test,
                np.array(
                    [
                        [1, 1, 1, 1, 0, 0, 0],
                        [1, 1, 1, 1, 1, 1, 0],
                    ]
                ),
                "Test X incorrect.",
            ),
        )
        self.assertIsNone(
            np.testing.assert_array_equal(
                y_train,
                np.array([1, 6, 3, 2]),
                "Train y incorrect.",
            ),
        )
        self.assertIsNone(
            np.testing.assert_array_equal(
                y_test,
                np.array([4, 5]),
                "Test y incorrect.",
            ),
        )
        self.assertIsNone(
            np.testing.assert_array_equal(
                labels_train,
                np.array(["one", "six", "three", "two"]),
                "Train labels incorrect.",
            ),
        )
        self.assertIsNone(
            np.testing.assert_array_equal(
                labels_test,
                np.array(["four", "five"]),
                "Test labels incorrect.",
            ),
        )

    def test_spxy(self):
        """Directly instantiate and test SPXY"""
        spxy_instance = SPXY(
            self.X,
            self.y,
            self.labels,
            {},
        )
        self.assertIsInstance(
            spxy_instance,
            SPXY,
            "Failed instantiation.",
        )
        self.assertFalse(
            len(spxy_instance.get_clusters()),
            "Clusters should not have been set.",
        )
        self.assertFalse(
            len(spxy_instance.get_sorted_cluster_counter()),
            "Sorted cluster Counter should not be found.",
        )
        self.assertTrue(
            len(spxy_instance._samples_idxs),
            "Sample indices not set.",
        )


if __name__ == "__main__":
    unittest.main()
