document.addEventListener("DOMContentLoaded", () => {

    // Existing Delete Modal functionality
    const deleteModalElement = document.getElementById("deleteModal");
    if (!deleteModalElement) {
        console.warn("Delete modal not found.");
    }
    const deleteModal = new bootstrap.Modal(deleteModalElement);
    const deleteButtons = document.getElementsByClassName("btn-delete");
    const deleteConfirm = deleteModal._element.querySelector("#deleteConfirm");

    document.getElementById("deleteModal").addEventListener("hidden.bs.modal", () => {
        deleteConfirm.href = "#"; // Reset the href

    });

    console.log("Delete Script Loaded")

    for (let button of deleteButtons) {
        button.addEventListener("click", (e) => {
            console.log('Delete Button clicked');
            let ObjID = e.target.getAttribute("data-id");
            let modelType = e.target.getAttribute("data-model");

            console.log(ObjID, modelType);
            if (modelType === "house") {
                deleteConfirm.href = `/delete_house/${ObjID}`;
            } else if (modelType === "kid") {
                deleteConfirm.href = `/delete_kid/${ObjID}`;
            }
            console.log(`Delete Confirm Href: ${deleteConfirm.href}`);

            deleteModal.show();
        });
    }


    // Existing Alert Closing Functionality
    setTimeout(function() {
        let messages = document.getElementById("msg");
        if (messages) { // Ensure the element exists
            let alert = new bootstrap.Alert(messages);
            alert.close();
        }
    }, 3000);


});

setTimeout(function () {
    let messages = document.getElementById("msg");
    let alert = new bootstrap.Alert(messages);
    alert.close();
}, 3000);

/**
 * Existing Toggle Status Function
 */
function toggleStatus(url) {
    window.location.href = url;
}

// Toggle household visibility
document.getElementById("toggleVisibility").addEventListener("click", () => {
    // Get all cards and their associated checkboxes
    console.log("Toggle visibility loaded")
    const housecards = document.querySelectorAll(".household-item");

    housecards.forEach((hcard) => {
        const visitcheckbox = hcard.querySelector(".visited-checkbox");
        console.log(visitcheckbox)
        // Toggle visibility based on checkbox state
        if (visitcheckbox.checked) {
            hcard.style.display = hcard.style.display === "none" ? "block" : "none";
        }
        console.log("Toggle visibility clicked")
    });
});