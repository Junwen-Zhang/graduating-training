(function (func) {
    $.ajax({
        url: "/up/getUpFans",
        type: "GET",
        dataType: "json",
        success: function (data) {
            func(data);
        }
    });
})(function (data) {
    // console.log(data);
    var myChart = echarts.init(document.getElementById('chart_up_fans'), 'infographic');


    // data = [];
    // for (let i = 0; i < 5; ++i) {
    //     data.push(Math.round(Math.random() * 200));
    // }
    // 20个up主的名字列表，用于y轴显示
    var nameList=[];
    for (let i=0;i<data.length;i++){
        nameList.push(data[i][1]);
    }
    console.log(nameList);
    var option = {
        xAxis: {
            max: 'dataMax'
        },
        yAxis: {
            type: 'category',
            data: nameList,
            inverse: true,
            animationDuration: 300,
            animationDurationUpdate: 300,
            max: data.length-1 // only the largest 3 bars will be displayed
        },
        series: [
            {
                realtimeSort: true,
                name: 'X',
                type: 'bar',
                data: data,
                label: {
                    show: true,
                    position: 'right',
                    valueAnimation: true
                }
            }
        ],
        legend: {
            show: true
        },
        animationDuration: 0,
        animationDurationUpdate: 3000,
        animationEasing: 'linear',
        animationEasingUpdate: 'linear'
    };
    function run() {
        console.log('running');
        // for (var i = 0; i < data.length; ++i) {
        //     if (Math.random() > 0.9) {
        //         data[i] += Math.round(Math.random() * 2000);
        //     } else {
        //         data[i] += Math.round(Math.random() * 200);
        //     }
        // }
        myChart.setOption(option);
    }

    setTimeout(function () {
        run();
    }, 0);
    setInterval(function () {
        run();
    }, 3000);

});
