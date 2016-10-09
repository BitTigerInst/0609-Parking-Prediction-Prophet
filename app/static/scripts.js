$(function () {
    
    var predict = [];
    var real = [];
    var score = 0;
    
    $('#score').hide();
    $('#chart_container').hide();
    $('.footer').hide();
    
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
    

    $('#upload-icon').hover(function(){ 
        $('#upload-icon > img').attr('src', "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEAAAABACAYAAACqaXHeAAAB7klEQVR4Xu2ZW07DMBBFHYmFNKILgSWgwj+sDPhGFVtgIa3SlTRokCKZNInH9jwU5eaztce+Z1520oSNP83G9QcAQARsnABSYOMB4FsE77vjKzng3B4+vBzhlgIkvgnhnYT3Ibx5QXABEIsfPO8FwRzAlHhPCKYAlsR7QTADwBHvAcEEQI54awjqAErEW0JQBTAnnir+0AJjsePfLFqkGoAl8dTz992xjw8/p/bQpOZoHJZUAHCETAEggZy5kiDEAXAFzAGwhiAKgCueRC4BsIQgBiBHPAeAFQQRALniuQAsIFQD2HXfu7tw7caFKXW5SaVAbG/+LHF9PLUvPzVFsRrAlJdS4nMiYBA3htCH/vPcPv+9T6h5RADEEDjiSwD8X0NGPNkUA0DGKB0u7dOF45GcFIjt7buvh9qwj+2JAuAIH8aUAshZgzMWADiUNMYgAiYuQxqgUzaRAilCWv8jBZACty9EtKJtyS5qgAf10qOwxl4RARpUOTbRBdAF0AVuvgtwUkd6DIqgNFGuPRRBFEEUQRTBuF7Q12Fu/ZAc57Io7gKSLqy05RYBlfsWmw4AYihXaqg4AsYnOW/9pV0EAEo9hwgYneVLQUrNM08BqY172ymuAd4bl1ofAKRIrtUOImCtnpPaNyJAiuRa7fwCT2o/UDUTaZoAAAAASUVORK5CYII=");
//        console.log($('#upload-label').attr('display'));
        $('#upload-label').show();
    }, function(){
        $('#upload-icon > img').attr('src', "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEAAAABACAYAAACqaXHeAAAB4ElEQVR4Xu2a4XHDIAyF0SYZJd2kmazpJt2k3YQeObvnONgW8kM6188/ExB6H9LD4SLp5I+cXH8iAFbAyQmwBU5eALEmmHN+LxsgIveojQhrgUH8xyD8FgUhBMBM/Lj5IRDcASyID4PgCmBDfAgENwBK8e4QXAA0ineF0B2AUbwbhK4AVsTfUkrjEfgntvJZ+a7r6dANwJr4cubnnPP05UdEZGtOj5elLgA0QmoAikDNXCQIOACtgCUA3hCgALTiB5EvLTDd2ZZYeyoCBqA14bUKGAW1xrSAgACwJKoB4NEOuwHknC8ppe8K/dXjSwtgA8KbiHxZdn6csxvAQoKbZ3cLgIU1PkXkcZ+w54EAmCW4KV5jgjVRk1aDiC9rwAAMoi4i8qPZkdYKmBjjdW/ZP72AaZLtMcYKAJ0LtAJakiOAym+BFoCosawAFMnWOGwBtsDrfUBrFSHG0wMQFC0x6AH0AHrA6o2Qpa0sc2iCFmqIOTRBmiBNkCb4dDMjEmLIIYta7wQR5juPQQA9qGpi8hg8+zGoqRKPMWEe4CFOswYBaCj95zHmCpi7eDSk8h8jSw6mSbUXGcviyDkEwApwbgFk+UbGMntAZNLItQkASfOIsVgBR9w1ZM6sACTNI8b6BRrGIFC28/3NAAAAAElFTkSuQmCC");
        $('#upload-label').hide();
    }
    );

    // Method that checks that the browser supports the HTML5 File API
    function browserSupportFileUpload() {
        var isCompatible = false;
        if (window.File && window.FileReader && window.FileList && window.Blob) {
        isCompatible = true;
        }
        return isCompatible;
    }
    
    $('#upload').change(function(e){
        if (!browserSupportFileUpload()) {
            alert('The File APIs are not fully supported in this browser!');
        } else {
            var data = null;
            var file = e.target.files[0];
            var reader = new FileReader();
            reader.readAsText(file);
            reader.onload = function(event) {
                var csvData = event.target.result.split('\n');
                
                for(var i in csvData){
//                console.log(i)
//                }
//                csvData.map(function(row){
                    var item = [];
                    csvData[i] = csvData[i].split(',');
                    
                    var time = new Date(csvData[i][1]).getTime();
                    if(!Number.isNaN(time)){
                        item.push(time);
                        item.push(Number(csvData[i][0]));
                    }
                    if(item.length > 0){
                        real.push(item);
                        if(predict[i]){
                            var s = 100 - (item[1] - predict[i-1][1])*(item[1] - predict[i-1][1])*100 / (item[1]*item[1]);
                            score += s;
                        }
                        
                    } 
                }
                score = score / real.length;
                
                var chart = $("#chart_container").highcharts();
                if (chart.series.length > 2) {
                    chart.series[2].remove();  
                }
                
                chart.addSeries({
                    name: 'real',
                    data: real,
                    marker: {
                        enabled: false
                    },
                    shadow: false,
                    color: '#eb9b49',
                    tooltip: {
                        valueDecimals: 0
                    }
                });
                $('#score > span').html(score);
                $('#score').show();
                
            };
            reader.onerror = function() {
                alert('Unable to read ' + file.fileName);
            };
        }
    
    });
    
    $("#date-selector").submit(function(event){
        event.preventDefault();
        $.get( '/test', $('#date-selector').serialize(), function(data) {
            
            for(var i in data) {
                var item = data[i];
                var myItem = [];
                myItem.push(new Date(item.time).getTime());
                myItem.push(item.occupancy);
                predict.push(myItem);
            }
            console.log(predict);
            // Create the chart
            $('#chart_container').highcharts('StockChart', {

    //            title: {
    //                text: 'Parking Occupancy Prediction',
    //                style: {
    ////                    color: '#FF00FF',
    ////                    fontWeight: 'bold',
    //                    fontSize: '32px'
    //                },
    //                margin: 60
    //            },
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
                    name: 'predict',
                    data: predict,
                    color: '#ffffff',
                    marker: {
                        enabled: true,
                        radius: 3
                    },
                    shadow: false,
                    tooltip: {
                        valueDecimals: 0
                    }
                }],
                navigator: {
                    series: {
                        color: '#d4fff1'
                    }
                },

            });  
            $('#date_container').hide();
            $('#chart_container').show();
            $('.footer').show();
        },
       'json' // I expect a JSON response
        );
    });

});
