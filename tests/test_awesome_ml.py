import numpy as np
from sklearn import datasets
from sklearn.model_selection import train_test_split
from awesome_ml.awesome import MajorityClassClassifier

def load_iris_mdoel():
    """
    A utility function that loads iris dataset from sklearn and returns
    fitted majority class model and its predictions on the test set.
    """
    iris = datasets.load_iris()
    X, y = iris.data, iris.target
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1)
    model = MajorityClassClassifier()
    model.fit(X_train, y_train)
    predictions = model.predict(X_test)
    return model, predictions

def test_fit_classes():
    """
    Tests if the MajorityClassClassifier model fits properly
    and generates classes from training data.
    """
    model, _ = load_iris_mdoel()
    np.testing.assert_array_equal(model.classes, np.array([0, 1, 2]))


def test_fit_majority_class():
    """
    Tests if the MajorityClassClassifier model fits properly
    and generates majority class from training data.
    """
    model, _ = load_iris_mdoel()
    np.testing.assert_array_equal(model.majority_class, 2)


def test_predict():
    """
    Tests if the MajorityClassClassifier model correctly predicts
    majority class for Iris dataset.
    """
    _, test_predictions = load_iris_mdoel()
    reference_predictions = np.zeros(test_predictions.shape, dtype=np.uint8) + 2
    np.testing.assert_array_equal(test_predictions, reference_predictions)
