(function (func) {
    var link=getQueryVariable('link');
    console.log(link);
    $.ajax({
        url: "/search/show?link="+link,
        type: "GET",
        dataType: "json",
        success: function (data) {
            func(data);
        }
    });
})(function (data) { //[{name:"",value:1.0}]
    console.log("data!!!");
    console.log(data);
    var myChart = echarts.init(document.getElementById('searchVideo_show'), 'infographic');
    var myChart1 = echarts3.init(document.getElementById('searcomment_keyword'), 'infographic');
    var myChart2  =  echarts.init(document.getElementById('chart_search_dmdt'), 'infographic');
    var myChart3 = echarts3.init(document.getElementById('chart_search_dmwordcloud'), 'infographic');



     // prettier-ignore
    let dataAxis = data["video_DanmakuDTC"]['x'];
    // prettier-ignore
    let dataY = data["video_DanmakuDTC"]['y'];
    let yMax = 500;
    let dataShadow = [];
    for (let i = 0; i < dataY.length; i++) {
        dataShadow.push(yMax);
    }
    var option1 = {
        series: [{
            type: 'wordCloud',
            // maskImage: maskImage,
            sizeRange: [15, 80],
            rotationRange: [0, 0],
            rotationStep: 45,
            gridSize: 5,
            // left:300,
            shape: 'star',
            width: '100%',
            height: '100%',
            textStyle: {
                normal: {
                    color: function () {
                        return 'rgb(' + [
                            Math.round(Math.random() * 160),
                            Math.round(Math.random() * 160),
                            Math.round(Math.random() * 160)
                        ].join(',') + ')';
                    },
                    fontFamily: 'sans-serif',
                    fontWeight: 'normal'
                },
                emphasis: {
                    shadowBlur: 10,
                    shadowColor: '#333'
                }
            },
            data: data["comment_keyword"]
        }]
    };
    var option2 = {
        title: {
            left:'36%',
            text: '浏览量量化统计',
            subtext: 'Feature Sample: Gradient Color, Shadow, Click Zoom'
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

    var option3 = {
        series: [{
            type: 'wordCloud',
            // maskImage: maskImage,
            sizeRange: [15, 80],
            rotationRange: [0, 0],
            rotationStep: 45,
            gridSize: 5,
            // left:300,
            shape: 'star',
            width: '100%',
            height: '100%',
            textStyle: {
                normal: {
                    color: function () {
                        return 'rgb(' + [
                            Math.round(Math.random() * 160),
                            Math.round(Math.random() * 160),
                            Math.round(Math.random() * 160)
                        ].join(',') + ')';
                    },
                    fontFamily: 'sans-serif',
                    fontWeight: 'normal'
                },
                emphasis: {
                    shadowBlur: 10,
                    shadowColor: '#333'
                }
            },
            data: data["danmaku_keywords"]
        }]
    };


    myChart3.setOption(option3);
    window.addEventListener("resize", function () {
        myChart3.resize();
    });

    // Enable data zoom when user click bar.
    const zoomSize = 6;
    myChart2.on('click', function (params) {
        console.log(dataAxis[Math.max(params.dataIndex - zoomSize / 2, 0)]);
        myChart2.dispatchAction({
            type: 'dataZoom',
            startValue: dataAxis[Math.max(params.dataIndex - zoomSize / 2, 0)],
            endValue:
                dataAxis[Math.min(params.dataIndex + zoomSize / 2, data.length - 1)]
        });
    });

    myChart2.setOption(option2);
    window.addEventListener("resize", function () {
        myChart2.resize();
    });

    myChart1.setOption(option1);
    window.addEventListener("resize", function () {
        myChart1.resize();
    });

});
function getQueryVariable(variable){
       var query = window.location.search.substring(1);
       console.log(query);
       var vars = query.split("&");
       for (var i=0;i<vars.length;i++) {
               var pair = vars[i].split("=");
               if(pair[0] == variable){return pair[1];}
       }
       return(false);
}
