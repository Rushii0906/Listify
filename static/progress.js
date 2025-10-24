const scriptTag = document.currentScript;
const urlParams = new URLSearchParams(scriptTag.src.split('?')[1]);

const totalTodos = parseInt(urlParams.get('total')) || 0;
const completedTodos = parseInt(urlParams.get('completed')) || 0;
const incompleteTodos = Math.max(totalTodos - completedTodos, 0);

const ctx = document.getElementById('progressChart').getContext('2d');

new Chart(ctx, {
  type: 'doughnut',
  data: {
    labels: ['Completed', 'Incomplete'],
    datasets: [{
      data: [completedTodos, incompleteTodos],
      backgroundColor: ['#00FFAB', '#FF5F7E'],
      borderWidth: 1
    }]
  },
  options: {
    cutout: '70%',
    plugins: {
      legend: {
        labels: {
          color: '#fff',
          font: {
            size: 13
          }
        }
      }
    }
  }
});
