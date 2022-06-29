(function (func) {
    $.ajax({
        url: "/guichu/submitHourAnalyse",
        type: "GET",
        dataType: "json",
        success: function (data) {
            func(data);
        }
    });
})(function (data) {
    var myChart = echarts.init(document.getElementById('chart_guichu_submithour'), 'infographic');

    // prettier-ignore
    let dataAxis = data['x'];
    // prettier-ignore
    let dataY = data['y'];
    let yMax = 500;
    let dataShadow = [];
    for (let i = 0; i < dataY.length; i++) {
        dataShadow.push(yMax);
    }
    var option = {
        title: {
            left:'36%',


        },
        xAxis: {
            data: dataAxis,
            axisLabel: {
                inside: true,
                color: '#070707'

            },
            axisTick: {
                show: false
            },
            axisLine: {
                show: false
            },
            z: 10
        },
        yAxis: {
            axisLine: {
                show: false
            },
            axisTick: {
                show: false
            },
            axisLabel: {
                color: '#999'
            }
        },
        dataZoom: [
            {
                type: 'inside'
            }
        ],
        series: [
            {
                type: 'bar',
                showBackground: true,

                itemStyle: {

                    color: new echarts.graphic.LinearGradient(0, 0, 0, 1, [
                        { offset: 0, color: '#C6FFDD' },
                        { offset: 0.5, color: '#FBD786' },
                        { offset: 1, color: '#f7797d' }
                    ])
                },
                emphasis: {
                    itemStyle: {
                        color: new echarts.graphic.LinearGradient(0, 0, 0, 1, [
                            { offset: 0, color: '#2ebf91' },
                            { offset: 0.7, color: '#5ab790' },
                            { offset: 1, color: '#8af5c8' }
                        ])
                    }
                },
                data: dataY
            }
        ]
    };
    // Enable data zoom when user click bar.
    const zoomSize = 6;
    myChart.on('click', function (params) {
        console.log(dataAxis[Math.max(params.dataIndex - zoomSize / 2, 0)]);
        myChart.dispatchAction({
            type: 'dataZoom',
            startValue: dataAxis[Math.max(params.dataIndex - zoomSize / 2, 0)],
            endValue:
                dataAxis[Math.min(params.dataIndex + zoomSize / 2, data.length - 1)]
        });
    });

    myChart.setOption(option);
    window.addEventListener("resize", function () {
        myChart.resize();
    });

});