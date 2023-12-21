function updateLocalStorage() {
    calculatePercentages();
}

function calculatePercentages() {
    console.log("calculating percentages");

    const tot = parseInt(localStorage.getItem('totalPuzzles')) || 0;
    const blueCount = parseInt(localStorage.getItem('Blue')) || 0;
    const purpleCount = parseInt(localStorage.getItem('Purple')) || 0;
    const yellowCount = parseInt(localStorage.getItem('Yellow')) || 0;
    const greenCount = parseInt(localStorage.getItem('Green')) || 0;

    // Calculate percentages
    const bluePercentage = (blueCount / tot) * 100;
    const purplePercentage = (purpleCount / tot) * 100;
    const yellowPercentage = (yellowCount / tot) * 100;
    const greenPercentage = (greenCount / tot) * 100;

    document.getElementById('blueProgressBar').style.width = bluePercentage + '%';
    document.getElementById('blueProgressBar').innerText = bluePercentage + '%';

    document.getElementById('purpleProgressBar').style.width = purplePercentage + '%';
    document.getElementById('purpleProgressBar').innerText = purplePercentage + '%';

    document.getElementById('yellowProgressBar').style.width = yellowPercentage + '%';
    document.getElementById('yellowProgressBar').innerText = yellowPercentage + '%';

    document.getElementById('greenProgressBar').style.width = greenPercentage + '%';
    document.getElementById('greenProgressBar').innerText = greenPercentage + '%';
}