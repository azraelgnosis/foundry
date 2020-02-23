$(document).ready(function() {

    // displays inputs based on type when appropriate action type selector is chosen
    $('#action_type').change(function() {
        $('.action_type_inputs').css('display', 'none');

        var type = $(this).val();
        $('#'+type).css('display', 'flex');
    });
});