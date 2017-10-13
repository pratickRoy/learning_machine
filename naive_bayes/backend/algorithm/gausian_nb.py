import pandas
from numpy import array, sqrt, pi, e
import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot
import os

class GaussianNB:

    pretty = False
    axes = None

    class_prior_probability = {}
    mean_dictionary = {}
    standard_deviation_dictionary = {}

    distinct_labels = None

    def fit(self, training_features, training_labels):

        no_of_features = len(training_features[0])

        if self.pretty and no_of_features != 2:

            raise ValueError("Pretty Print only works, if no. of features is 2")

        self.distinct_labels = set(training_labels)

        for label in self.distinct_labels:

            self.class_prior_probability[label] = training_labels.count(label) / len(training_labels)

        features_by_label_dictionary = {distinct_training_label: [[] for i in range(0, no_of_features)] for
                                        distinct_training_label in self.distinct_labels}

        for i in range(0, len(training_labels)):

            features_list = features_by_label_dictionary[training_labels[i]]
            for j in range(0, len(features_list)):
                features_list[j].append(training_features[i][j])

        for label, feature_tuple in features_by_label_dictionary.items():

            for i in range(0, len(feature_tuple)):

                if len(feature_tuple[i]) == 1:

                    self.mean_dictionary[(label, i)] = feature_tuple[i][0]
                    self.standard_deviation_dictionary[(label, i)] = e

                else:

                    self.mean_dictionary[(label, i)] = array(feature_tuple[i]).mean()
                    self.standard_deviation_dictionary[(label, i)] = array(feature_tuple[i]).std(ddof=1)

        if self.pretty:

            features_x = []
            features_y = []
            for i in range(0, len(training_features)):

                features_x.append(training_features[i][0])
                features_y.append(training_features[i][1])

            groups = pandas.DataFrame(dict(x=features_x, y=features_y, label=training_labels)).groupby('label')
            for name, group in groups:
                self.axes.plot(group.x, group.y, marker='o', linestyle='', ms=2, label='train_'+str(name))

    def predict(self, testing_features, testing_labels=None):

        if self.pretty and testing_labels is None:

            raise ValueError("Pretty Print requires testing labels to be present")

        prediction_labels = []
        for feature_tuple in testing_features:

            max_probability = 0
            prediction_label = None
            for label in self.distinct_labels:

                likelihood = 1
                for i in range(0, len(feature_tuple)):
                    m = self.mean_dictionary[label, i]
                    s = self.standard_deviation_dictionary[label, i]
                    likelihood *= 1/(sqrt(2*pi)*s)*e**(-0.5*(float(feature_tuple[i]-m)/s)**2)
                probability = likelihood * self.class_prior_probability[label]
                if probability >= max_probability:
                    prediction_label = label
                    max_probability = probability

            prediction_labels.append(prediction_label)

        if self.pretty:

            features_x = []
            features_y = []
            for i in range(0, len(testing_features)):

                features_x.append(testing_features[i][0])
                features_y.append(testing_features[i][1])

            labels = []
            for i in range(0, len(testing_features)):

                if prediction_labels[i] == testing_labels[i]:
                    labels.append("correct_"+str(prediction_labels[i]))
                else:
                    labels.append("predicted_" + str(prediction_labels[i]) + "_but_real_" + str(testing_labels[i]))

            groups = pandas.DataFrame(dict(x=features_x, y=features_y, label=labels)).groupby('label')

            for name, group in groups:
                self.axes.plot(group.x, group.y, marker='o' if name.startswith("correct_") else '*', linestyle='',
                               ms=4 if name.startswith("correct_") else 6,
                               label=name)

            self.axes.legend()
            file = './learning_machine/static/images/plot.png'
            pyplot.savefig(file)
            pyplot.close()

        return prediction_labels

    def score(self, testing_features, testing_labels):

        prediction_labels = self.predict(testing_features, testing_labels)

        score = 0
        for i in range(0, len(prediction_labels)):

            if testing_labels[i] == prediction_labels[i]:

                score += 1

        return score / len(prediction_labels)

    @staticmethod
    def score_only(prediction_labels, testing_labels):

        score = 0
        for i in range(0, len(prediction_labels)):

            if testing_labels[i] == prediction_labels[i]:

                score += 1

        return score / len(prediction_labels)

    def pretty_print(self):

        self.pretty = True
        figure, self.axes = pyplot.subplots()
