var ctx = document.getElementById("myChart").getContext('2d');
var myChart = new Chart(ctx, {
  type: 'doughnut',
  data: {
    labels: ["犬", "猫"],
    datasets: [{
      backgroundColor: [
        "#2ecc71",
        "#95a5a6"
      ],
      data: [77.6, 22.4]
    }]
  },
  options: {
    cutoutPercentage: 65
  },
  afterDatasetsDraw: {
  }
});