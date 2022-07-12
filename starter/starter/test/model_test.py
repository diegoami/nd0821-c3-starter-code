import unittest
import pytest
from ml.model import train_model, compute_model_metrics
import numpy as np



class ModelTestCase(unittest.TestCase):
    def test_create_model(self):
        X = np.array([[1, 2], [3, 4], [5, 6], [7, 8]])
        y = np.array([0, 0, 0, 1])
        model = train_model(X, y)
        self.assertIsNotNone(model)

if __name__ == '__main__':
    unittest.main()
