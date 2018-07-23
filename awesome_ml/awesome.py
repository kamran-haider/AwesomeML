import numpy as np
from sklearn.base import BaseEstimator

class MajorityClassClassifier(BaseEstimator):
    """
    A majority class classifier
    """

    def __init__(self):
        self.classes = None
        self.majority_class = None

    def fit(self, X, y):
        """
        Parameters
        ----------
        X : numpy.ndarray, shape = n_samples, n_features
            Training examples.
        y : numpy.ndarray, shape = n_samples
            Target class labels.
        """

        classes, counts = np.unique(y, return_counts=True)
        majority_class_index = np.argmax(counts)
        majority_class = classes[majority_class_index]
        self.classes = classes
        self.majority_class = majority_class

    def predict(self, X):
        """
        Parameters
        ----------
        X : numpy.ndarray, shape = n_samples, n_features
            Training examples.

        Returns
        -------
        predictions : numpy.ndarray, shape = n_samples
            predicted class labels.
        """
        predictions = np.zeros((len(X), 1), dtype=np.uint8)
        predictions += self.majority_class
        return predictions