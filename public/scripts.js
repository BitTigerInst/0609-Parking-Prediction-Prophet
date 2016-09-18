$(function () {
    $.getJSON('predict.json', function (data) {
        
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
        $('#container').highcharts('StockChart', {

            rangeSelector: {
                selected: 1
            },

            title: {
                text: 'Parking Pccupancy Prediction'
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
