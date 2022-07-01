(function (func) {
    $.ajax({
        url: "/animation/scoreAnalyse",
        type: "GET",
        dataType: "json",
        success: function (data) {
            func(data);
        }
    });
})(function (data) {
    var myChart = echarts.init(document.getElementById('chart_animation_score'), 'infographic');

    var option = {
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
        },
        series: [
            {
                name: '数量',
                type: 'line',
                smooth: true,
                // prettier-ignore
                data: data['y'],
                markArea: {
                    itemStyle: {
                        color: 'rgb(48,204,123)'
                    },

                },
                itemStyle: {
                    normal: {
                        // color: "#386db3",//折线点的颜色
                        lineStyle: {
                            color: "rgb(48,204,123)"//折线的颜色
                        }
                    }
                },

            }
        ]
    };


    myChart.setOption(option);
    window.addEventListener("resize", function () {
        myChart.resize();
    });

});