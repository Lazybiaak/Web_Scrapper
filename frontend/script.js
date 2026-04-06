const checkBtn = document.getElementById('checkBtn');
const resultsDiv = document.getElementById('results');

checkBtn.addEventListener('click', async () => {
  const boids = document.getElementById('boids').value
    .split('\n')
    .map(b => b.trim())
    .filter(b => b);

  const companyShareId = document.getElementById('ipoSelect').value;

  resultsDiv.innerHTML = "Checking...";

  const results = [];

  for (let boid of boids) {
    // Fake fetch, since we can’t hit CDSC API directly from browser without CORS
    const isAllotted = Math.random() > 0.5;
    results.push({
      boid,
      status: isAllotted ? 'Allotted' : 'Not Allotted',
      units: isAllotted ? Math.floor(Math.random() * 10 + 1) : 0
    });
  }

  resultsDiv.innerHTML = "";
  results.forEach(item => {
    const div = document.createElement('div');
    div.className = 'card';
    div.innerHTML = `<b>${item.boid}</b><br/><span class="${item.status === 'Allotted' ? 'allotted' : 'not'}">${item.status} (${item.units})</span>`;
    resultsDiv.appendChild(div);
  });
});