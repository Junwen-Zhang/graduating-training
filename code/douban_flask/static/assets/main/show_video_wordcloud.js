(function (func) {
    var script=document.getElementsByTagName("script");
    script=script[script.length-1];
    var partition=script.getAttribute("partition");
    var videoid=script.getAttribute("videoid");
    // console.log("1 partition:",partition);
    
    $.ajax({
        url: "/video/keywordAnalyse?partition="+partition,
        type: "GET",
        dataType: "json",
        success: function (data) {
            func(data);
        }
    });
})(function (data) { 
    // console.log("222 ",data);
    var script=document.getElementsByTagName("script");
    script=script[script.length-2];
    var partition=script.getAttribute("partition");
    // console.log("2 partition:",partition);

    for(var i=1;i<=100;i++){
        var myChart = echarts3.init(document.getElementById('chart_video_wordcloud'+partition+String(i)), 'infographic');

        var option = {
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
                data: data[i]
            }]
        };

        myChart.setOption(option);
        window.addEventListener("resize", function () {
            myChart.resize();
        });
    }

});
