$(document).ready(function() {
    $('#action_type').change(function() {
        var type = $(this).val();

        $('#'+type).css('display', 'none');

    });
});