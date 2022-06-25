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
    var myChart = echarts.init(document.getElementById('chart_up_fans'), 'infographic');

    // 20个up主的名字列表，用于y轴显示
    var nameList = [];
    for (let i = 0; i < data.length; i++) {
        nameList.push(data[i][1]);
    }
    console.log(nameList);
    var data1 = [];   //x轴的数据，每次会根据该值进行坐标的变化
    for (let i = 0; i < data.length; i++) {
        data1.push(data[i][2]);
    }
    var index = 2;
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
            max: data.length - 1 // only the largest 3 bars will be displayed
        },
        series: [
            {
                realtimeSort: true,
                name: 'X',
                type: 'bar',
                data: data1,
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
        if (index >= data[0].length - 2) {
            return;
        }
        for (var i = 0; i < data.length; ++i) {   // 下标区分了up主
            if (i == 0) {
            } else {
                data1[i] += data[i][index];    //粉丝增量

            }
        }
        index++;
        myChart.setOption(option);
    }

    setTimeout(function () {
    }, 0);
    setInterval(function () {
        run();
    }, 1000);

});
