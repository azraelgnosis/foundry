$(document).ready(function() {
    $('select#type').change(function() {
        let type = $(this).val();

        switch (type) {            
            case 'Area':
                $('tr#within').css('display', 'flex');
                $('td#landmass').css('display', 'table-cell');
                $('td#region').css('display', 'table-cell');
                $('td#zone').css('display', 'table-cell');                
                break;
            case 'Zone':
                $('tr#within').css('display', 'flex');
                $('td#landmass').css('display', 'table-cell');
                $('td#region').css('display', 'table-cell');
                $('td#zone').css('display', 'none');
                break;
            case 'Region':
                $('tr#within').css('display', 'flex');
                $('td#landmass').css('display', 'table-cell');
                $('td#region').css('display', 'none');
                $('td#zone').css('display', 'none');
                break;
            case 'Landmass':
                $('tr#within').css('display', 'none');
                break;
            
        }
    });
});