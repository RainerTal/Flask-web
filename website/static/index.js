function deleteNote(noteId) {
  fetch("/delete-note", {
    method: "POST",
    body: JSON.stringify({ noteId: noteId }),
  }).then((_res) => {
    window.location.href = "/";
  });
}

function deleteValues(open_vId, closeId, highId, lowId) {
  fetch("/delete-values", {
    method: "POST",
    body: JSON.stringify({
       open_vId: open_vId,
       closeId: closeId,
       highId: highId,
       lowId: lowId
      }),
  }).then((_res) => {
    window.location.href = "/";
  });
}

document.addEventListener('DOMContentLoaded', function() {
  fetch('/chart-data')
      .then(response => {
          if (!response.ok) {
              throw new Error('Network response was not ok');
          }
          return response.json();
      })
      .then(data => {
          const chartData = {
              series: [{
                  name: 'Price Data',
                  data: data
              }],
              chart: {
                  type: 'candlestick',
                  height: 350
              },
              title: {
                  text: 'Candlestick Chart',
                  align: 'left'
              },
              xaxis: {
                  type: 'datetime'
              },
              yaxis: {
                  tooltip: {
                      enabled: true
                  }
              }
          };

          var chart = new ApexCharts(document.querySelector("#chart"), chartData);
          chart.render();
      })
      .catch(error => console.error('Error fetching or processing data:', error));
});




