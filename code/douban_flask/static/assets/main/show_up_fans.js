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
    const countryColors = {
        0:'#f00',
        1:'#00f',
    };
    // 20个up主的名字列表，用于y轴显示
    var nameList = [];
    var negative=[];  // 判断涨粉是否为负数，进行对颜色的选择
    for (let i = 0; i < data.length; i++) {
        nameList.push(data[i][1]);
        negative.push(0);   // 初始化都先设置为正数
    }
    console.log(nameList);
    var data1 = [];   //x轴的数据，每次会根据该值进行坐标的变化
    var data1_abs=[];  // 取绝对值，柱状图的显示的主要依赖数据
    for (let i = 0; i < data.length; i++) {
        if(data[i][2]<0){
            negative[i]=1;
        }
        data1.push(data[i][2]);
        data1_abs.push(Math.abs(data1[i]));
    }
    console.log('初始');
    console.log(data1_abs);
    var index = 2;
    var option = {
        xAxis: {
            max: 'dataMax',
            animationDurationUpdate: 2100,
        },
        yAxis: {
            type: 'category',
            splitLine: {
                show: false
            },
            axisTick: {
                show: false
            },
            axisLine: {
                show: false
            },
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
                data: data1_abs,
                label: {
                    show: true,
                    position: 'right',
                    valueAnimation: true
                },
                itemStyle: {
                    color: function (param) {
                        return countryColors[negative[param['dataIndex']]];
                    }
                },
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
        console.log('data1_abs');
        console.log(data1_abs);
        if (index >= data[0].length - 2) {
            return;
        }
        for (var i = 0; i < data.length; ++i) {   // 下标区分了up主
            data1[i] += data[i][index];    //粉丝增量
                if(data1[i]<0){
                    negative[i]=1;   // 负数柱形条颜色有所变化
                    data1_abs[i]=-data1[i];   // 变为正数显示
                }
                else{
                    negative[i]=0;
                    data1_abs[i]=data1[i];
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
