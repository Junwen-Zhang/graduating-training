(function (func) {
    $.ajax({
        url: "/up/getUpTags",
        type: "GET",
        dataType: "json",
        success: function (data) {
            func(data);
        }
    });
})(function (data) {
    console.log('data');
    console.log(data);
    for (var i = 0; i < data.length; i++) {
        var myChart = echarts.init(document.getElementById('chart_up_tags'+data[i]['uid']), 'infographic');
        delete data[i].uid;
        var option = {
            tooltip: {
                trigger: 'item'
            },
            legend: {
                top: '5%',
                left: 'center',
                show:false
            },
            series: [
                {
                    name: 'Access From',
                    type: 'pie',
                    radius: ['40%', '70%'],
                    avoidLabelOverlap: false,
                    itemStyle: {
                        borderRadius: 10,
                        borderColor: '#fff',
                        borderWidth: 2
                    },
                    label: {
                        show: false,
                        position: 'center'
                    },
                    emphasis: {
                        label: {
                            show: true,
                            fontSize: '20',
                            fontWeight: 'bold'
                        }
                    },
                    labelLine: {
                        show: false
                    },
                    data: data[i]['data']
                }
            ]
        };


        myChart.setOption(option);
        window.addEventListener("resize", function () {
            myChart.resize();
        });
    }


});
