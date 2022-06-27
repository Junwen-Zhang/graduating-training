(function (func) {
    var partition=getQueryVariable("partition");
    var videoid=getQueryVariable("videoid");
    $.ajax({
        url: "/video/keywordAnalyse?partition="+partition+"&videoid="+videoid,
//        url : "/guichu/wordcloudAnalyse",
        type: "GET",
        dataType: "json",
        success: function (data) {
            func(data);
        }
    });
})(function (data) { //[{name:"",value:1.0}]
    console.log("data!!!");
    console.log(data);
    var myChart = echarts3.init(document.getElementById('chart_video_wordcloud'), 'infographic');

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
            data: data
        }]
    };


    myChart.setOption(option);
    window.addEventListener("resize", function () {
        myChart.resize();
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
