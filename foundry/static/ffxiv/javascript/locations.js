$(document).ready(function() {
    // ensures all <input> and <select> elements have the 'form-control' class
    $('input,select').addClass('form-control'); 

    // displays the appropriate location selects depending on what level of location is chosen
    $('select#type').change(function() {
        let type = $(this).val();

        $('td#region').css('display', 'none');  
        $('td#zone').css('display', 'none');

        switch (type) {            
            case 'Area':
                $('td#zone').css('display', 'table-cell');                
            case 'Zone':
                $('td#region').css('display', 'table-cell');
            case 'Region':                 
                $('td#landmass').css('display', 'table-cell');
                $('tr#within').css('display', 'flex');  
                break;
            case 'Landmass':
                $('tr#within').css('display', 'none');
                break;
        }
    });

    $('select#landmass, select#region').change(function() {
        var landmass = $('select#landmass').val();

        // clears Region and Zone <select>
        $('select#region option').remove();
        $('select#zone option').remove(); 

        var region_select = $('select#region');
        
        if (landmass) {
            var regions = Object.keys(locations[landmass].subregions);        
            regions.forEach(function(region) {
                region_select.append(new Option(region, region));
            });

            var region = region_select.val();
            if (region) {
                
                var zone_select = $('select#zone');
                var zones = Object.keys(locations[landmass].subregions[region].subregions);               
                zones.forEach(function(zone) {
                    zone_select.append(new Option(zone, zone));
                });
            }
        }
    });
});