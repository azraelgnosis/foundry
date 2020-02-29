$(document).ready(function() {
    // ensures all <input> and <select> elements have the 'form-control' class
    $('input,select').addClass('form-control'); 

    // displays the appropriate location selects depending on what level of location is chosen
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

    $('select#landmass, select#region').change(function() {
        var landmass = $('select#landmass').val();

        var region_select = $('select#region');
        var regions = Object.keys(locations[landmass].regions);
        $('select#region option').remove();
        regions.forEach(function(region) {
            region_select.append(new Option(region, region));
        });

        var zone_select = $('select#zone');
        var zones = Object.keys(locations[landmass].regions[region_select.val()].zones);
        $('select#zone option').remove();        
        zones.forEach(function(zone) {
            zone_select.append(new Option(zone, zone));
        });
    });
});