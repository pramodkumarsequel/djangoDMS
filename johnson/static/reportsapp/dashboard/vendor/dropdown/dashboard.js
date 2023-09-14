window.onload = function() {
    var chart = new CanvasJS.Chart("chartContainer", {
        animationEnabled: true,
        theme: "light2",
        title: {
            text: "Retailer Wise Invoice Amount"
        },
        data: [{
            type: "{{chart}}",
            dataPoints: {{ data_points|safe }}
        }]
    });
    chart.render();
}