# -*- coding: utf-8 -*-
"""
Created on Wed Oct 18 12:31:31 2017

@author: El Pentagono
"""

import numpy as np
from sklearn.base import BaseEstimator, ClassifierMixin
from sklearn.utils.validation import check_X_y, check_array, check_is_fitted
from sklearn.utils.multiclass import unique_labels, check_classification_targets

class ScoreClassifier(BaseEstimator, ClassifierMixin):
    """ A binary classifier which implements the Score algorithm 
    (Christopher et al.).

    Parameters
    ----------
    weighted : str, optional
        A parameter to implement Weighted or regular classification.

    Attributes
    ----------
    X_ : array, shape = [n_samples, n_features]
    y_ : array, shape = [n_samples]
    """
    def __init__(self, weighted=None):
        self.weighted = weighted
    
    # Warning The estimator tags are experimental and is subject to change.    
    def _more_tags(self):
        return {'non_deterministic': False,
                'requires_positive_X': False,
                'requires_positive_y': False,
                'X_types': ['2darray'],
                'poor_score': False,
                'no_validation': False,
                'multioutput': False,
                'allow_nan': False,
                'stateless': False,
                'multilabel': False,
                '_skip_test': False,
                'multioutput_only': False,
                'binary_only': True, # This is a binary-only classifier
                'requires_fit': True}

    def fit(self, X, y, weight=None):
        """A reference implementation of a fitting function for the classifier.

        Parameters
        ----------
        X : array-like, shape = [n_samples, n_features]
            The training input samples.
        y : array-like, shape = [n_samples]
            The target values. An array of int or str.
        weight: array-like. shape = [n_samples]
                weights vector.

        Returns
        -------
        self : object
            Returns self.
        """
        # Check that X and y have correct shape
        X, y = check_X_y(X, y)
        check_classification_targets(y)
        self.n_samples, self.n_features = X.shape
        
        # Store the classes seen during fit
        #self.classes_ = unique_labels(y)
        self.classes_, indices = np.unique(y, return_inverse=True)
        
        # Check if classes_ are equal to 2
        # TO DO: Remove it when making it multiclass
        if len(self.classes_) != 2:
            print("number of classes not supported: expected 2 classes, got {}".format(len(self.classes_)))
            assert len(self.classes_) == 2

        self.X_ = X
        self.y_ = y

        # Frequency dictionaries for each feature
        self.nx_ = [None for _ in range(self.n_features)]
        self.ncx_ = [None for _ in range(self.n_features)]

        # Given this is a binary classifier 1 is assigned to the second class value
        self.nc_ = sum(indices == True)

        for i in range(self.n_features):
            x = X[:,i]
            unique_elements, counts_elements = np.unique(x, return_counts=True)
            self.nx_[i] = dict(zip(unique_elements, counts_elements))

            cx = X[indices == True, i]
            unique_elements, counts_elements = np.unique(cx, return_counts=True)
            self.ncx_[i] = dict(zip(unique_elements, counts_elements))
            for key in self.nx_[i].keys():
                if key not in self.ncx_[i]:
                    self.ncx_[i][key] = 0

        # TO DO
        # if weighted:
        #     self.nx_ = _Subset_weighted(X)
        #     self.n_ = df[weight].sum()
        #     self.nc_ = criterio[weight].sum()
        #
        # else:
        #     self.nx_ = self._getSubset(X)
        #     self.n_  = len(X)
        #     self.nc_ = sum(y)

        # Return the classifier
        return self

    def predict(self, X):
        """
        Parameters
        ----------
        X : array-like of shape = [n_samples, n_features]
            The input samples.

        Returns
        -------
        y : array of int of shape = [n_samples]
            The label for each sample is the label of the highest
            decision function value during fit.
        """
        # Check is fit had been called
        check_is_fitted(self, ['X_', 'y_'])

        # Input validation
        X = check_array(X)
        
        D = self.decision_function(X)
        
        # The following is just an attemp to pass the estimator checker
        if len(self.classes_) == 1: 
            return np.full((len(X), ), self.classes_[0])
        else:
            return np.where(D > 0 , self.classes_[1], self.classes_[0])
        
        #return np.where(D > 0 , self.classes_[1], self.classes_[0])
        #return self.classes_[np.argmax(D, axis=1)]
        #return np.zeros((len(X), ), dtype=bool)


    def decision_function(self, X):
        """Score of the samples X to predict the likelihood.
        Parameters
        ----------
        X : array-like, shape (n_samples, n_features)
        Returns
        -------
        X : array of float of shape = [n_samples]
            positive values are for class members, zero and negative
            values for others
            If decision_function='ovo' the shape is
            (n_samples, n_classes * (n_classes-1) / 2)
            Returns the decision function of the sample for each class
            in the model.
            If decision_function='ovr', the shape is (n_samples, n_classes)
        """

#        scores =  np.asanyarray([sum([np.log(((self.ncx_[dic][i] + 1) / float(self.nc_ + 2)) / 
#                                             (((self.nx_[dic][i] - self.ncx_[dic][i]) + 1) / 
#                                              float((self.n_samples - self.nc_) + 2))) for dic, i in enumerate(row)]) for row in X])
    
        aux = []
        for row in X:
            aux2 = []
            for dic, i in enumerate(row):
                if i in self.ncx_[dic].keys():
                    clase = ((self.ncx_[dic][i] + 1) / float(self.nc_ + 2))
        
                    anticlase = (((self.nx_[dic][i] - self.ncx_[dic][i]) + 1) / 
                                float((self.n_samples - self.nc_) + 2))
        
                    aux2.append(np.log(clase / anticlase))
        
                else: aux2.append(0)

            aux.append(sum(aux2))
        
        scores =  np.asanyarray(aux)
    
        return scores
