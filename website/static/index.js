function deleteNote(noteId) {
  fetch("/delete-note", {
    method: "POST",
    body: JSON.stringify({ noteId: noteId }),
  }).then((_res) => {
    window.location.href = "/";
  });
}

document.addEventListener("DOMContentLoaded", function () {
  // Attach event listener for delete buttons
  attachDeleteListeners();

  function attachDeleteListeners() {
    const deleteButtons = document.querySelectorAll(".close");

    deleteButtons.forEach((button) => {
      button.addEventListener("click", function () {
        const openValues = document.querySelectorAll("#open_values li");
        const closeValues = document.querySelectorAll("#close_values li");
        const highs = document.querySelectorAll("#highs li");
        const lows = document.querySelectorAll("#lows li");

        const open_vId = openValues.length > 0 ? openValues[openValues.length - 1].querySelector(".close").getAttribute("data-id") : null;
        const closeId = closeValues.length > 0 ? closeValues[closeValues.length - 1].querySelector(".close").getAttribute("data-id") : null;
        const highId = highs.length > 0 ? highs[highs.length - 1].querySelector(".close").getAttribute("data-id") : null;
        const lowId = lows.length > 0 ? lows[lows.length - 1].querySelector(".close").getAttribute("data-id") : null;

        fetch("/delete-values", {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({
            open_vId: open_vId,
            closeId: closeId,
            highId: highId,
            lowId: lowId,
          }),
        })
        .then((response) => {
          if (response.ok) {
            // Remove the deleted elements from the DOM without reloading
            if (open_vId) openValues[openValues.length - 1].remove();
            if (closeId) closeValues[closeValues.length - 1].remove();
            if (highId) highs[highs.length - 1].remove();
            if (lowId) lows[lows.length - 1].remove();
          } else {
            console.error("Error deleting values");
          }
        })
        .catch((error) => {
          console.error("Fetch error:", error);
        });
      });
    });
  }
});

const urls = [
  '/chart-data',
  '/chart-name'
];

const fetchPromises = urls.map(url => fetch(url).then(response => {
  if (!response.ok) {
    throw new Error(`Network response was not ok for ${url}`);
  }
  return response.json();
}));

document.addEventListener('DOMContentLoaded', function() {
  Promise.all(fetchPromises)
      .then(([data, note]) => {
          
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
                  text: note,
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




