let navigationDrawer = new function () {

    let self = this;
    let ACTIVE_CLASS = "is-active"
    self.toggle = function () {

        if(self.isActive()) {
            self.$navigationDrawer.removeClass(ACTIVE_CLASS)
        } else {
            self.$navigationDrawer.addClass(ACTIVE_CLASS);
        }

    };

    self.isActive = function () {

        return self.$navigationDrawer.hasClass(ACTIVE_CLASS);
    };

    let onNavigationDrawerItemOthersClickListener = function () {

        snackbar.showStillUnderConstructionError()
    };
    let onNavigationDrawerItemNaiveBayesClickListener = function () {

        $('#lm-action-bar-menu-button').click()
    };


    let initComponents = function () {
        self.$navigationDrawer = $('#lm-page-navigation-container');
        self.$navigationDrawerItemNaiveBayes = $('#lm-navigation-algorithms-naive-bayes');
        self.$navigationDrawerItemOthers = $('#lm-navigation-algorithms-others');
    };
    let initListeners = function () {
        self.$navigationDrawerItemNaiveBayes.on("click", onNavigationDrawerItemNaiveBayesClickListener);
        self.$navigationDrawerItemOthers.on("click", onNavigationDrawerItemOthersClickListener);
    };
    self.init = function () {

        initComponents();
        initListeners();
    };
};

$(document).ready(function(){
    navigationDrawer.init()
});