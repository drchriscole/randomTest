
import numpy as np
import sklearn
from sklearn.datasets import load_breast_cancer
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score

## Interesting explanation of how randomness is used in sklearn:
##
##   https://scikit-learn.org/stable/common_pitfalls.html#randomness


def run_tts(seed=None):
        """Runs a train_test_split and a basic RF cross-validation

        Returns: test set labels, cv scores
        """

        X, y = load_breast_cancer(return_X_y=True, as_frame=False)
        # seed needs specifying here...
        train_X, test_X, train_y, test_y = train_test_split(
            X, y, test_size=0.1, stratify=y, random_state=seed
        )
        
        # ...and here
        rf = RandomForestClassifier(min_samples_leaf=1, 
                                    min_samples_split=2, 
                                    random_state=seed)
        scores = cross_val_score(rf, train_X, train_y, cv=5)
        return(test_y, scores)

if __name__ == "__main__":

    y, scores = run_tts(23)
    print("Test set labels:")
    print(y)
    print("5-fold cross-validation scores:")
    print(scores)
