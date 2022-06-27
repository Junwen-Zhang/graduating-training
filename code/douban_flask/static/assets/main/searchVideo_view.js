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
