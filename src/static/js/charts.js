// Global variables to store chart data
var ordersPerMonth, ordersPerMonthData, ordersPerMonthLabels;
var ordersPerDish, ordersPerDishData, ordersPerDishLabels;
var bookingsPerRestaurant, bookingsPerRestaurantData, bookingsPerRestaurantLabels;

// Init function. Labels and data processed in the same order as present in JSON object
function sendData(ordersMonth, ordersDish, bookingRestaurant) { //stockRestaurant 

    ordersPerMonth = JSON.parse(ordersMonth);
    console.log(ordersPerMonth)
    
    ordersPerMonthData = [];
    ordersPerMonthLabels = [];
    for (var key in ordersPerMonth) {
        ordersPerMonthLabels.push(key);
        ordersPerMonthData.push(ordersPerMonth[key]);
    }

    ordersPerDish = JSON.parse(ordersDish);
    console.log(ordersPerDish)

    ordersPerDishData = [];
    ordersPerDishLabels = [];
    for (var key in ordersPerDish) {
        ordersPerDishLabels.push(ordersPerDish[key].course_name);
        ordersPerDishData.push(ordersPerDish[key].amount_sold);
    }

    bookingsPerRestaurant = JSON.parse(bookingRestaurant);
    console.log(bookingsPerRestaurant)

    bookingsPerRestaurantData = [];
    bookingsPerRestaurantLabels = [];
    for (var key in bookingsPerRestaurant){
        bookingsPerRestaurantLabels.push(bookingsPerRestaurant[key].restaurant_id);
        bookingsPerRestaurantData.push(bookingsPerRestaurant[key].total_bookings);
    }

    /* 
    stockPerRestaurant = JSON.parse(stockRestaurant);
    console.log(stockPerRestaurant)

    stockPerRestaurantData = [];
    stockPerRestaurantLabels = [];
    for (var key in stocksPerRestaurant){
        stockPerRestaurantLabels.push(stockPerRestaurant[key].ingredient_name);
        stockPerRestaurantData.push(stockPerRestaurant[key].quantity);
    } 
    */
};


var random = function random() {
    return Math.round(Math.random() * 100);
};

$(document).ready(function(){
    var lineChart = new Chart($('#canvas-1'), {
        type: 'line',
        data: {
            labels: ordersPerMonthLabels,
            datasets: [{
                label: '# of orders',
                backgroundColor: 'rgba(151, 187, 205, 0.2)',
                borderColor: 'rgba(151, 187, 205, 1)',
                pointBackgroundColor: 'rgba(151, 187, 205, 1)',
                pointBorderColor: '#fff',
                data: ordersPerMonthData
            }]
        },
        options: {
            responsive: true,
        }
    });
    var doughnutChart = new Chart($('#canvas-2'), {
        type: 'doughnut',
        data: {
            labels: ['Red', 'Green', 'Yellow'],
            datasets: [{
                data: [300, 50, 100],
                backgroundColor: ['#FF6384', '#36A2EB', '#FFCE56'],
                hoverBackgroundColor: ['#FF6384', '#36A2EB', '#FFCE56']
            }]
        },
        options: {
            responsive: true,
        }
    });
    var barChart = new Chart($('#canvas-3'), {
        type: 'bar',
        data: {
            labels: ordersPerDishLabels,
            datasets: [{
                label: "# of orders",
                backgroundColor: 'rgba(220, 220, 220, 0.5)',
                borderColor: 'rgba(220, 220, 220, 0.8)',
                highlightFill: 'rgba(220, 220, 220, 0.75)',
                highlightStroke: 'rgba(220, 220, 220, 1)',
                data: ordersPerDishData
            }]
        },
        options: {
            responsive: true,
            scales: {
                xAxes: [{   // In order to show disable auto skip feature so all labels are visible
                    stacked: false,
                    beginAtZero: true,
                    scaleLabel: {
                        labelString: 'Month'
                    },
                    ticks: {
                        stepSize: 1,
                        min: 0,
                        autoSkip: false
                    }
                }],
                yAxes: [{   // Set y-axis to begin at zero
                    ticks: {
                        beginAtZero: true
                    }
                }]
            }
        }
    });
    barChart.update();

    var radarChart = new Chart($('#canvas-4'), {
        type: 'radar',
        data: {
            labels: ['Eating', 'Drinking', 'Sleeping', 'Designing', 'Coding', 'Cycling', 'Running'],
            datasets: [{
                label: 'My First dataset',
                backgroundColor: 'rgba(220, 220, 220, 0.2)',
                borderColor: 'rgba(220, 220, 220, 1)',
                pointBackgroundColor: 'rgba(220, 220, 220, 1)',
                pointBorderColor: '#fff',
                pointHighlightFill: '#fff',
                pointHighlightStroke: 'rgba(220, 220, 220, 1)',
                data: [65, 59, 90, 81, 56, 55, 40]
            }, {    
                label: 'My Second dataset',
                backgroundColor: 'rgba(151, 187, 205, 0.2)',
                borderColor: 'rgba(151, 187, 205, 1)',
                pointBackgroundColor: 'rgba(151, 187, 205, 1)',
                pointBorderColor: '#fff',
                pointHighlightFill: '#fff',
                pointHighlightStroke: 'rgba(151, 187, 205, 1)',
                data: [28, 48, 40, 19, 96, 27, 100]
            }]
        },
        options: {
            responsive: true
        }
    });    
    var pieChart = new Chart($('#canvas-5'), {
        type: 'pie',
        data: {
            labels: bookingsPerRestaurantLabels,
            datasets: [{
                backgroundColor: ['#FF6384', '#36A2EB', '#FFCE56'],
                hoverBackgroundColor: ['#FF6384', '#36A2EB', '#FFCE56'],
                data: bookingsPerRestaurantData
            }]
        },
        options: {
            responsive: true
        }
    });
    /*
    var polarAreaChart = new Chart($('#canvas-6'), {
        type: 'polarArea',
        data: {
            labels: ['Red', 'Green', 'Yellow', 'Grey', 'Blue'],
            datasets: [{
                data: [11, 16, 7, 3, 14],
                backgroundColor: ['#FF6384', '#4BC0C0', '#FFCE56', '#E7E9ED', '#36A2EB']
            }]
        },
        options: {
            responsive: true
        }
    });
    */
})