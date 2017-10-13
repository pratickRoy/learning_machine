let actionBar = new function () {

    let self = this;
    let onMenuButtonClickListener = function () {

        if(navigationDrawer.isActive()) {
            self.$menuButton.removeClass('is-active')
        } else {
            self.$menuButton.addClass('is-active');
        }
        navigationDrawer.toggle()
    };

    let initComponents = function () {
        self.$menuButton = $('#lm-action-bar-menu-button');
    };
    let initListeners = function () {
        self.$menuButton.on("click", onMenuButtonClickListener);
    };
    self.init = function () {

        initComponents();
        initListeners();
    };
};

$(document).ready(function(){
    actionBar.init()
});