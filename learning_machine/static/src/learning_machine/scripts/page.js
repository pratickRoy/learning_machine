let page = new function () {

    let self = this;

    let onSignInIconClickListener = function () {

        snackbar.showStillUnderConstructionError();
    };

    let scrollComplete = false;
    let navigationWasActive = false;
    let onWindowScrollListener = function () {

        if(!scrollComplete && $(document).scrollTop() > 0) {
            scrollComplete = true;
            self.$actionBar.addClass('fixed');
            if(self.$navigationDrawer.hasClass('is-active')) {
                navigationWasActive = true;
                $('#lm-action-bar-menu-button').click()
            }

        }

        else if($(document).scrollTop() <= 0){
            scrollComplete = false;
            self.$actionBar.removeClass('fixed');
            if(navigationWasActive) {
                navigationWasActive = false;
                $('#lm-action-bar-menu-button').click()
            }
        }
    };

    let initComponents = function () {
        self.$signInIcon = $('#lm-navigation-drawer-account-sign-in-icon');
        self.$navigationDrawer = $('#lm-page-navigation-container');
        self.$actionBar = $('.lm-action-bar');
    };
    let initListeners = function () {
        self.$signInIcon.on("click", onSignInIconClickListener);
         $(window).scroll(onWindowScrollListener)
    };
    self.init = function () {

        initComponents();
        initListeners();
    };
};

$(document).ready(function(){
    page.init()
});


