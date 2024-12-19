document.addEventListener("DOMContentLoaded", () => {

    const deleteModal = new bootstrap.Modal(document.getElementById("deleteModal"));
    const deleteButtons = document.getElementsByClassName("btn-delete");
    const deleteConfirm = deleteModal._element.querySelector("#deleteConfirm");
    
    document.getElementById("deleteModal").addEventListener("hidden.bs.modal", () => {
        deleteConfirm.href = "#"; // Reset the href
        
    });

    console.log("Delete Script Loaded")
    
    for (let button of deleteButtons) {
        button.addEventListener("click", (e) => {
            console.log('Button clicked');
            let ObjID = e.target.getAttribute("data-id");
            let modelType = e.target.getAttribute("data-model");

            console.log(ObjID, modelType);
            if (modelType === "house"){
                deleteConfirm.href = `/delete_house/${ObjID}`;
            } else if (modelType === "kid"){
                deleteConfirm.href = `/delete_kid/${ObjID}`;
                
            }
            console.log(deleteConfirm.href)

            deleteModal.show();
        });
    }
    
    //Toggle status buttons
    // Get all visited checkboxes
    const checkboxes = document.querySelectorAll(".visited-checkbox");
    
    // Update the counters
    const niceCountElement = document.getElementById("nice_counter");
    const naughtyCountElement = document.getElementById("naughty_counter");
    
    checkboxes.forEach(checkbox => {
        checkbox.addEventListener("change", function () {
            const householdId = this.id.split("-")[0];
            const visitedStatus = this.checked;
            const spinner = document.getElementById(`${householdId}-spinner`);
            const label = document.querySelector(`label[for="${this.id}"]`);
            
            // Disable the checkbox to prevent further clicks during loading
            this.disabled = true;

            // Show the spinner
            spinner.style.display = "inline-block";

            fetch("/update-visited/", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                    "X-CSRFToken": "{{ csrf_token }}"
                },
                body: JSON.stringify({ household_id: householdId, visited: visitedStatus })
            })
            .then(response => response.json())
            .then(data => {
                label.textContent = `Visited: ${visitedStatus}`;

                // Dynamically update the Nice and Naughty counters
                if (data.nice_count !== undefined && data.naughty_count !== undefined) {
                    niceCountElement.textContent = `Number of presents needed: ${data.nice_count}`;
                    naughtyCountElement.textContent = `Number of coals needed: ${data.naughty_count}`;
                }
            })
            .catch(error => console.error("Error:", error))
            .finally(() => {
                // Hide the spinner
                spinner.style.display = "none";
                this.disabled = false;
            });
        });
    });

});

setTimeout(function() {
    let messages = document.getElementById("msg");
    let alert = new bootstrap.Alert(messages);
    alert.close();
}, 3000);

function toggleStatus(url) {
    window.location.href = url;
}

document.getElementById("toggleVisibility").addEventListener("click", () => {
    // Get all cards and their associated checkboxes
    const cards = document.querySelectorAll(".card");

    cards.forEach((card) => {
      const checkbox = card.querySelector(".visited-checkbox");
      // Toggle visibility based on checkbox state
      if (checkbox.checked) {
        card.style.display = card.style.display === "none" ? "block" : "none";
      }
    });
  });