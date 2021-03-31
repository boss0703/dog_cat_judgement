(function() {

  var result = document.getElementById("result").value;
  var purple = 'rgb(173, 173, 255)';
  var gray = 'rgb(211, 211, 211)';

  var data = {
    datasets: [{
      data: [result, 100-result],
      backgroundColor: [purple, gray],
    }],
  };

  // グラフオプション
  var options = {
    // グラフの太さ（中央部分を何％切り取るか）
    cutoutPercentage: 75,
    // 凡例を表示しない
    legend: { display: false },
    // 自動サイズ変更をしない
    responsive: false,
    // マウスオーバー時に情報を表示しない
    tooltips: { enabled: false },
  };

  // グラフ描画
  var ctx = document.getElementById('chart-area').getContext('2d');
  new Chart(ctx, {
    type: 'doughnut',
    data: data,
    options: options
  });
})();