$(function () {
    $('.datepicker-from').pickadate({
        format: 'mmm dd, yyyy',
        formatSubmit: 'yyyy/mm/dd'
    });
    $('.datepicker-to').pickadate({
        format: 'mmm dd, yyyy',
        formatSubmit: 'yyyy/mm/dd'
//        ,
//        min: start_date
    });
    
    
    //$.getJSON('predict.json', function (data) {
    $SCRIPT_ROOT = {{ request.script_root|tojson|safe }};
    $.getJSON($SCRIPT_ROOT + "/predict.json", function (data) {    
        var myData = [];
        for(var i in data){
            var item = data[i];
            var myItem = [];
            myItem.push(new Date(item.time).getTime());
            myItem.push(item.occupancy);
            myData.push(myItem);
        }
        console.log(myData);
        // Create the chart
        $('#chart_container').highcharts('StockChart', {

            title: {
                text: 'Parking Occupancy Prediction',
                style: {
//                    color: '#FF00FF',
//                    fontWeight: 'bold',
                    fontSize: '32px'
                },
                margin: 40
            },
            rangeSelector: {
                allButtonsEnabled: true,
                buttons: [{
                    type: 'day',
                    count: 1,
                    text: 'today',
                    dataGrouping: {
                        forced: true,
                        units: [['hour', [1]]]
                    }
                }, {
                    type: 'day',
                    count: 3,
                    text: 'last 3 days',
                    dataGrouping: {
                        forced: true,
                        units: [['hour', [1]]]
                    }
                }, {
                    type: 'day',
                    count: 7,
                    text: 'last week',
                    dataGrouping: {
                        forced: true,
                        units: [['hour', [1]]]
                    }
                }, {
                    type: 'month',
                    count: 1,
                    text: 'last month',
                    dataGrouping: {
                        forced: true,
                        units: [['day', [1]]]
                    }
                }],
                buttonTheme: {
                    width: 100
                },
                selected: 1
            },

            series: [{
                name: 'occupancy',
                data: myData,
                marker: {
                    enabled: true,
                    radius: 3
                },
                shadow: true,
                tooltip: {
                    valueDecimals: 0
                }
            }]
            
        });
    });
});
