function updateProgressBars(categoryCounts, totalPuzzles) {
    const categories = ['yellow', 'green', 'blue', 'purple'];
    const categoryNames = ['Yellow', 'Green', 'Blue', 'Purple'];

    categories.forEach((color, index) => {
        const count = categoryCounts[categoryNames[index]] || 0;
        const percentage = totalPuzzles > 0 ? ((count / totalPuzzles) * 100).toFixed(2) : '0.00';

        const progressBar = document.getElementById(color + 'ProgressBar');
        if (progressBar) {
            progressBar.style.width = percentage + '%';
            progressBar.innerText = percentage + '%';
        }
    });
}

function clearContents(element) {
    element.value = '';
}
