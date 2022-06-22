(function (func) {
    $.ajax({
        url: "/animationScoreAnalyse",
        type: "GET",
        dataType: "json",
        success: function (data) {
            func(data);
        }
    });
})(function (data) {

    var myChart = echarts.init(document.getElementById('chart_animation_score'), 'infographic');

    var option = {
        title: {
            text: 'Distribution of Electricity',
            subtext: 'Fake Data'
        },
        tooltip: {
            trigger: 'axis',
            axisPointer: {
                type: 'cross'
            }
        },
        toolbox: {
            show: true,
            feature: {
                saveAsImage: {}
            }
        },
        xAxis: {
            type: 'category',
            boundaryGap: false,
            // prettier-ignore
            data: data['x']
        },
        yAxis: {
            type: 'value',
            axisLabel: {
                formatter: '{value} W'
            },
            axisPointer: {
                snap: true
            }
        },
        visualMap: {
            show: false,
            dimension: 0,
            // pieces: [
            //     {
            //         lte: 6,
            //         color: 'green'
            //     },
            //     {
            //         gt: 6,
            //         lte: 8,
            //         color: 'red'
            //     },
            //     {
            //         gt: 8,
            //         lte: 14,
            //         color: 'green'
            //     },
            //     {
            //         gt: 14,
            //         lte: 17,
            //         color: 'red'
            //     },
            //     {
            //         gt: 17,
            //         color: 'green'
            //     }
            // ]
        },
        series: [
            {
                name: 'Electricity',
                type: 'line',
                smooth: true,
                // prettier-ignore
                data: data['y'],
                markArea: {
                    itemStyle: {
                        color: 'rgba(255, 173, 177, 0.4)'
                    },
                    // data: [
                    //     [
                    //         {
                    //             name: 'Morning Peak',
                    //             xAxis: '07:30'
                    //         },
                    //         {
                    //             xAxis: '10:00'
                    //         }
                    //     ],
                    //     [
                    //         {
                    //             name: 'Evening Peak',
                    //             xAxis: '17:30'
                    //         },
                    //         {
                    //             xAxis: '21:15'
                    //         }
                    //     ]
                    // ]
                }
            }
        ]
    };


    myChart.setOption(option);
    window.addEventListener("resize", function () {
        myChart.resize();
    });

});