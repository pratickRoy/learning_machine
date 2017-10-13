from django.db import models


class GaussianNaiveBayesData(object):

    def __init__(self,
                 training_features,
                 training_labels,
                 testing_features,
                 testing_labels,
                 sk_prediction_labels,
                 prediction_labels,
                 sk_accuracy,
                 accuracy):

        self.training_features = training_features
        self.training_labels = training_labels
        self.testing_features = testing_features
        self.testing_labels = testing_labels
        self.sk_prediction_labels = sk_prediction_labels
        self.prediction_labels = prediction_labels
        self.sk_accuracy = sk_accuracy
        self.accuracy = accuracy


