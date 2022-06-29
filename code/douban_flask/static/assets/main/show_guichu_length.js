(function (func) {
  $.ajax({
    url: "/guichu/lengthAnalyse",
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
    color:["#5ba2fa","#a78cf8","#faa9c8","#f6d966","#9dc5f6","#ff9999","#66cc99"],
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