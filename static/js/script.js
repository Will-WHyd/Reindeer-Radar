//Toggle status buttons

function toggleStatus(url) {
    window.location.href = url;
}


// Function for adding numbers (total cost)

function calculateTotal() {

    const rows = document.querySelectorAll("#expenseTable tbody tr");
    let totalCost = 0;

    rows.forEach(row => {
        const cost = parseFloat(row.querySelector(".cost").textContent) || 0;
        totalCost += cost;
    });

    document.getElementById("totalCost").textContent = totalCost.toFixed(2);
}

document.addEventListener('DOMContentLoaded', function () {
    calculateTotal();
});