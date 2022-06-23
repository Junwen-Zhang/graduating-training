(function (func) {
    $.ajax({
        url: "/animation/tagsAnalyse",
        type: "GET",
        dataType: "json",
        success: function (data) {
            func(data);
        }
    });
})(function (data) {
    console.log(data);
    var myChart = echarts.init(document.getElementById('chart_animation_tags'), 'infographic');
    var myChart1 = echarts.init(document.getElementById('chart_100anime_tags'), 'infographic');
    var myChart2 = echarts3.init(document.getElementById('word_cloud_anime'), 'infographic');

    var option = {
        tooltip: {
            trigger: 'item'
        },
        legend: {
            top: '5%',
            left: 'center'
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
                        fontSize: '40',
                        fontWeight: 'bold'
                    }
                },
                labelLine: {
                    show: false
                },
                data: data['series1']
            }
        ]
    };

    var option1 = {
        tooltip: {
            trigger: 'item'
        },
        legend: {
            top: '5%',
            left: 'center'
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
                        fontSize: '40',
                        fontWeight: 'bold'
                    }
                },
                labelLine: {
                    show: false
                },
                data: data['series2']
            }
        ]
    };

    // var maskImage = new Image();
    // maskImage.src = 'D:/大三/小学期/term/graduating-training/code/douban_flask/static/assets/img/tree.jpg'
    var option2 = {
        series: [{
            type: 'wordCloud',
            // maskImage: maskImage,
            sizeRange: [15, 80],
            rotationRange: [0, 0],
            rotationStep: 45,
            gridSize: 8,
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
            data: data['series1']
        }]
    };

// 词云图
//     var maskImage = new Image();
//     maskImage.src = 'img/tree.png';


    myChart.setOption(option);
    window.addEventListener("resize", function () {
        myChart.resize();
    });

    myChart1.setOption(option1);
    window.addEventListener("resize", function () {
        myChart1.resize();
    });

    myChart2.setOption(option2);
    window.addEventListener("resize", function () {
        myChart2.resize();
    });
});