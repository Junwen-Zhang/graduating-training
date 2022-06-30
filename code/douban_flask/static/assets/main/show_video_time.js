(function (func) {
    
    var script=document.getElementsByTagName("script");
    // console.log("1 script:",script);
    script=script[script.length-1]; 
    var partition=script.getAttribute("partition");
    // console.log("1 script:",script);
    // console.log("1 partition:",partition);

    $.ajax({
        url: "/video/timeAnalyse?partition="+partition,
        type: "GET",
        dataType: "json",
        success: function (data) {
            func(data);
        }
    });
})(function (data) {
    var script=document.getElementsByTagName("script");
    // console.log("2 script:",script);
    script=script[script.length-2];
    var partition=script.getAttribute("partition");
    // console.log("2 script:",script);
    // console.log("2 partition:",partition);

    for(var i=1;i<=100;i++){
        console.log('chart_video_time'+partition+String(i));
        var myChart = echarts.init(document.getElementById('chart_video_time'+partition+String(i)), 'infographic');
        // console.log("@@@");
        // prettier-ignore
        let dataAxis = data[i]['x'];
        // prettier-ignore
        let dataY = data[i]['y'];
        let yMax = 500;
        let dataShadow = [];
        for (let i = 0; i < dataY.length; i++) {
            dataShadow.push(yMax);
        }
        var option = {
            title: {
                left:'36%',
                text: '视频浏览量变化趋势',
                // subtext: 'Feature Sample: Gradient Color, Shadow, Click Zoom'
            },
            xAxis: {
                data: dataAxis,
                axisLabel: {
                    inside: true,
                    color: '#fff'

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
                            { offset: 0, color: '#83bff6' },
                            { offset: 0.5, color: '#188df0' },
                            { offset: 1, color: '#188df0' }
                        ])
                    },
                    emphasis: {
                        itemStyle: {
                            color: new echarts.graphic.LinearGradient(0, 0, 0, 1, [
                                { offset: 0, color: '#2378f7' },
                                { offset: 0.7, color: '#2378f7' },
                                { offset: 1, color: '#83bff6' }
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
        // console.log("end!!!");
    }

});