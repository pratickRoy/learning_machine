$(document).ready(function() {

    // features
    requirejs(['src/learning_machine/scripts/page']);
    requirejs(['src/naive_bayes/scripts/naive_bayes_body']);

    // partials
    requirejs(['src/learning_machine/scripts/partials/snackbar']);
    requirejs(['src/learning_machine/scripts/partials/actionBar']);
    requirejs(['src/learning_machine/scripts/partials/navigationDrawer']);
});