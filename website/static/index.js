function deleteNote(noteId) {
  fetch("/delete-note", {
    method: "POST",
    body: JSON.stringify({ noteId: noteId }),
  }).then((_res) => {
    window.location.href = "/";
  });
}

function deleteDrink(drinkId) {
  fetch("/delete-drink", {
    method: "POST",
    body: JSON.stringify({ drinkId: drinkId }),
  }).then((_res) => {
    window.location.href = "/";
  });
}

function deleteDrink2(drink2Id) {
  fetch("/delete-drink2", {
    method: "POST",
    body: JSON.stringify({ drink2Id: drink2Id }),
  }).then((_res) => {
    window.location.href = "/";
  });
}

// Function to delete values from Chart 1
function deleteChart1Values(open_vId, closeId) {
  fetch("/delete-values", {
      method: "POST",
      headers: {
          "Content-Type": "application/json",
      },
      body: JSON.stringify({ open_vId: open_vId, closeId: closeId }),
  })
  .then((response) => {
      if (response.ok) {
          // Remove the corresponding list items in Chart 1 (both open and close)
          const openElem = document.querySelector(`#open_values .close[data-id-open="${open_vId}"]`);
          const closeElem = document.querySelector(`#close_values .close[data-id-close="${closeId}"]`);
          if (openElem) openElem.parentElement.remove();
          if (closeElem) closeElem.parentElement.remove();
      } else {
          console.error("Error deleting values for Chart 1");
      }
  })
  .catch((error) => console.error("Fetch error for Chart 1:", error));
}

// Function to delete values from Chart 2
function deleteChart2Values(open_v2Id, close2Id) {
  fetch("/delete-values2", {
      method: "POST",
      headers: {
          "Content-Type": "application/json",
      },
      body: JSON.stringify({ open_v2Id: open_v2Id, close2Id: close2Id }),
  })
  .then((response) => {
      if (response.ok) {
          // Remove the corresponding list items in Chart 2 (both open and close)
          const openElem = document.querySelector(`#open_values2 .close[data-id-open="${open_v2Id}"]`);
          const closeElem = document.querySelector(`#close_values2 .close[data-id-close="${close2Id}"]`);
          if (openElem) openElem.parentElement.remove();
          if (closeElem) closeElem.parentElement.remove();
      } else {
          console.error("Error deleting values for Chart 2");
      }
  })
  .catch((error) => console.error("Fetch error for Chart 2:", error));
}

// Function to delete values from Chart 3
function deleteChart3Values(open_v3Id, close3Id) {
  fetch("/delete-values3", {
      method: "POST",
      headers: {
          "Content-Type": "application/json",
      },
      body: JSON.stringify({ open_v3Id: open_v3Id, close3Id: close3Id }),
  })
  .then((response) => {
      if (response.ok) {
          // Remove the corresponding list items in Chart 3 (both open and close)
          const openElem = document.querySelector(`#open_values3 .close[data-id-open="${open_v3Id}"]`);
          const closeElem = document.querySelector(`#close_values3 .close[data-id-close="${close3Id}"]`);
          if (openElem) openElem.parentElement.remove();
          if (closeElem) closeElem.parentElement.remove();
      } else {
          console.error("Error deleting values for Chart 3");
      }
  })
  .catch((error) => console.error("Fetch error for Chart 3:", error));
}


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

const urls2 = [
  '/chart-data2',
  '/chart-name2'
];

const fetchPromises2 = urls2.map(url => fetch(url).then(response => {
  if (!response.ok) {
    throw new Error(`Network response was not ok for ${url}`);
  }
  return response.json();
}));

document.addEventListener('DOMContentLoaded', function() {
  Promise.all(fetchPromises2)
      .then(([data2, drink]) => {
          
          const chartData = {
              series: [{
                  name: 'Price Data',
                  data: data2
              }],
              chart: {
                  type: 'candlestick',
                  height: 350
              },
              title: {
                  text: drink,
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

          var chart2 = new ApexCharts(document.querySelector("#chart2"), chartData);
          chart2.render();
      })
      .catch(error => console.error('Error fetching or processing data:', error));
});



const urls3 = [
  '/chart-data3',
  '/chart-name3'
];

const fetchPromises3 = urls3.map(url => fetch(url).then(response => {
  if (!response.ok) {
    throw new Error(`Network response was not ok for ${url}`);
  }
  return response.json();
}));

document.addEventListener('DOMContentLoaded', function() {
  Promise.all(fetchPromises3)
      .then(([data3, drink2]) => {
          
          const chartData = {
              series: [{
                  name: 'Price Data',
                  data: data3
              }],
              chart: {
                  type: 'candlestick',
                  height: 350
              },
              title: {
                  text: drink2,
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

          var chart3 = new ApexCharts(document.querySelector("#chart3"), chartData);
          chart3.render();
      })
      .catch(error => console.error('Error fetching or processing data:', error));
});







