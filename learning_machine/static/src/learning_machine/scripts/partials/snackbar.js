let snackbar = new function () {

    let self = this;

    self.show = function (message) {

        self.$snackbar.text(message);
        self.$snackbar.addClass("show");
        setTimeout(function () {
           self.$snackbar.removeClass("show")
        }, 3000);
    };

    self.showStillUnderConstructionError = function () {

        self.show('Sorry! This feature is still under construction.')
    };


    let initComponents = function () {
        self.$snackbar = $('#lm-page-snackbar');
    };
    let initListeners = function () {
        // Nothing Yet
    };
    self.init = function () {

        initComponents();
        initListeners();
    };
};

$(document).ready(function(){
    snackbar.init()
});