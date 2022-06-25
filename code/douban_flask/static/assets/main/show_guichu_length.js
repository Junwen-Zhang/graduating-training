(function (func) {
  $.ajax({
    url: "/timeAnalyse/"+partition+"/"+videoid,
    type: "GET",
    dataType: "json",
    success: function (data) {
      func(data);
    }
  });
})(function (data) {
  var myChart = echarts.init(document.getElementById('chart_guichu_length'), 'infographic');

  var option = {
    tooltip: {
      trigger: 'item'

    },
    legend: {
      top: '90%',
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
        data: data
      }
    ]
  };

  myChart.setOption(option);
  window.addEventListener("resize", function () {
    myChart.resize();
  });

});