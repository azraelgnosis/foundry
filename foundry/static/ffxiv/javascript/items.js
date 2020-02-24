$(document).ready(function() {

    $('#item_type').change(function() {
        $('.item_type_form').css('display', 'none');

        var item_type = $(this).val()
        $("#"+item_type).css('display', 'table-row');
    });
});