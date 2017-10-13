import numpy
from sklearn.metrics import accuracy_score
from sklearn.naive_bayes import GaussianNB as SkLearnGaussianNB
from naive_bayes.backend.data_generator import continous_data_generator
from naive_bayes.backend.algorithm.gausian_nb import GaussianNB
from naive_bayes.models import GaussianNaiveBayesData


class Manager:
    training_features, training_labels, testing_features, testing_labels = continous_data_generator \
        .generate(n_points=10000)

    @classmethod
    def run_gaussian_naive_bayes(cls):
        sk_classifier = SkLearnGaussianNB()
        sk_classifier.fit(cls.training_features, cls.training_labels)

        sk_prediction_labels = list(sk_classifier.predict(cls.testing_features))
        sk_accuracy = str(accuracy_score(sk_prediction_labels, cls.testing_labels) * 100) + "%"

        classifier = GaussianNB()
        classifier.pretty_print()
        classifier.fit(cls.training_features, cls.training_labels)

        prediction_labels = classifier.predict(cls.testing_features, cls.testing_labels)
        accuracy = str(classifier.score_only(prediction_labels, cls.testing_labels) * 100) + "%"
        return GaussianNaiveBayesData(cls.training_features,
                                      cls.training_labels,
                                      cls.testing_features,
                                      cls.testing_labels,
                                      sk_prediction_labels,
                                      prediction_labels,
                                      sk_accuracy,
                                      accuracy)
