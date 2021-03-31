var chartJsPluginCenterLabel = {
  labelShown: false,

  afterRender: function (chart) {
    // afterRender は何度も実行されるので、２回目以降は処理しない
    if (this.labelShown) {
      return;
    }
    this.labelShown = true;
    // ラベルの HTML
    var value = chart.data.datasets[0].data[0];
    var animal = document.getElementById("animal").value;
    var labelBox = document.createElement('div');
    labelBox.classList.add('label-box');
    labelBox.innerHTML = '<div class="label">'
      + '<div class="chart-title">'
      + animal
      + '</div>'
      + '<div class="chart-value">'
      + value
      + '<span class="per">%</span>'
      + '</div>';
      + '</div>';
    // ラベル描画
    var canvas = chart.ctx.canvas;
    canvas.parentNode.insertBefore(labelBox, canvas.nextElementSibling);
  },
};

// 上記プラグインの有効化
Chart.plugins.register(chartJsPluginCenterLabel);