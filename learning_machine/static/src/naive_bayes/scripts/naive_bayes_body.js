let naiveBayes = new function () {

    let self = this;

    let state;
    let onGaussianNaiveBayesButtonListener = function () {
        state = $('#lm-gaussian-card-running-results').html();
        self.$gaussianNaiveBayes.addClass('is-active').removeClass('lm-hide');
        self.$multinomialNaiveBayes.addClass('lm-hide').removeClass('is-active');
        openRunningDiv(true)
        gaussianRun()
    };

    let onMultinomialNaiveBayesButtonListener = function () {
        snackbar.showStillUnderConstructionError()
        //self.$multinomialNaiveBayes.addClass('is-active').removeClass('lm-hide');
        //self.$gaussianNaiveBayes.addClass('lm-hide').removeClass('is-active');
        //openRunningDiv(true)
    };
    let onGaussianNaiveBayesCardCloseButtonListener = function () {
        $('#lm-gaussian-card-running-results').html(state);
        self.$gaussianNaiveBayes.removeClass('is-active');
        self.$multinomialNaiveBayes.removeClass('lm-hide');
        openRunningDiv(false)
    };

    let onMultinomialNaiveBayesCardCloseButtonListener = function () {
        self.$multinomialNaiveBayes.removeClass('is-active');
        self.$gaussianNaiveBayes.removeClass('lm-hide');
        openRunningDiv(false)
    };
    
    let openRunningDiv = function (makeActive) {

        if(makeActive) {
            $('.lm-card-cover').addClass('lm-hide');
            $('.lm-card-running').removeClass('lm-hide');
        } else {
            $('.lm-card-cover').removeClass('lm-hide');
            $('.lm-card-running').addClass('lm-hide');
        }
    }

    let gaussianRun = function () {
        $.ajax({
            dataType: 'json',
            url: "gaussian/",
            cache: false,
            success: function(json){

                let trainingFeatures = json.gaussianNaiveBayesData.training_features;
                let trainingLabels = json.gaussianNaiveBayesData.training_labels;

                let testingFeatures = json.gaussianNaiveBayesData.testing_features;
                let testingLabels = json.gaussianNaiveBayesData.testing_labels;
                let predictionLabels = json.gaussianNaiveBayesData.prediction_labels;
                let sklearnPredictionLabels = json.gaussianNaiveBayesData.sk_prediction_labels;

                for (i = 0; i < trainingLabels.length; i++) {
                    $("#grade").append('<div>' + trainingFeatures[i][0].toFixed(2) + '</div>');
                    $("#bumpy").append('<div>' + trainingFeatures[i][1].toFixed(2) + '</div>');
                    $("#speed").append('<div class=' + trainingLabels[i] + '>' + trainingLabels[i] + '</div>');
                }
                for (i = 0; i < testingLabels.length; i++) {
                    $("#grade_result").append('<div>' + testingFeatures[i][0].toFixed(2) + '</div>');
                    $("#bumpy_result").append('<div>' + testingFeatures[i][1].toFixed(2) + '</div>');

                    let correctLabel = trainingLabels[i];
                    let predictedLabel = predictionLabels[i];
                    let skLearnPredictedLabel = sklearnPredictionLabels[i];

                    $("#correct_speed_result").append('<div class=' + correctLabel + '>' + correctLabel + '</div>');
                    if(predictedLabel === correctLabel) {
                        $("#predicted_speed_result").append('<div class=' + predictedLabel + '>' + predictedLabel + '</div>');
                    } else {
                        $("#predicted_speed_result").append('<div class="error">' + predictedLabel + '</div>');
                    }
                    if(skLearnPredictedLabel === correctLabel) {
                        $("#sklearn_predicted_speed_result").append('<div class=' + skLearnPredictedLabel + '>' + skLearnPredictedLabel + '</div>');
                    } else {
                        $("#sklearn_predicted_speed_result").append('<div class="error">' + skLearnPredictedLabel + '</div>');
                    }

                }
                $('#impl-accuracy-value').append(json.gaussianNaiveBayesData.accuracy)
                $('#skLearn-accuracy-value').append(json.gaussianNaiveBayesData.sk_accuracy)

                $.ajax({
                    url : "gaussian/plot",
                    cache: true,
                    processData : false,
                }).always(function(){
                    $("#image-plot").attr("src", "gaussian/plot").fadeIn();
                });
            }
        });
    };

    let initComponents = function () {
        self.$gaussianNaiveBayes = $('#lm-gaussian-naive-bayes-card');
        self.$multinomialNaiveBayes = $('#lm-multinomial-naive-bayes-card');
        self.$gaussianNaiveBayesCloseButton = $('#lm-gaussian-naive-bayes-card-close-button');
        self.$multinomialNaiveBayesCloseButton = $('#lm-multinomial-naive-bayes-card-close-button');
        self.$gaussianNaiveBayesButton = $('#lm-gaussian-naive-bayes-button');
        self.$multinomialNaiveBayesButton = $('#lm-multinomial-naive-bayes-button');
    };
    let initListeners = function () {
        self.$gaussianNaiveBayesButton.on("click", onGaussianNaiveBayesButtonListener);
        self.$multinomialNaiveBayesButton.on("click", onMultinomialNaiveBayesButtonListener);
        self.$gaussianNaiveBayesCloseButton.on("click", onGaussianNaiveBayesCardCloseButtonListener);
        self.$multinomialNaiveBayesCloseButton.on("click", onMultinomialNaiveBayesCardCloseButtonListener);
    };
    self.init = function () {

        initComponents();
        initListeners();
    };
};

$(document).ready(function(){
    naiveBayes.init()
});


