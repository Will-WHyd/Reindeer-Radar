document.addEventListener("DOMContentLoaded", () => {

    const deleteModal = new bootstrap.Modal(document.getElementById("deleteModal"));
    const deleteButtons = document.getElementsByClassName("btn-delete");
    const deleteConfirm = deleteModal._element.querySelector("#deleteConfirm");
    
    document.getElementById("deleteModal").addEventListener("hidden.bs.modal", () => {
        deleteConfirm.href = "#"; // Reset the href
        
    });
    
    for (let button of deleteButtons) {
        button.addEventListener("click", (e) => {
            console.log('Button clicked');
            let ObjID = e.target.getAttribute("data-id");
            let modelType = e.target.getAttribute("data-model");

            console.log(ObjID, modelType);
            if (modelType === "house"){
                deleteConfirm.href = /delete_house/${ObjID};
            } else if (modelType === "kid"){
                deleteConfirm.href = /delete_kid/${ObjID};
                
            }
            console.log(deleteConfirm.href)

            deleteModal.show();
        });
    }
    
    });

    setTimeout(function() {
        let messages = document.getElementById("msg");
        let alert = new bootstrap.Alert(messages);
        alert.close();
    }, 3000);

    //Toggle status buttons

function toggleStatus(url) {
    window.location.href = url;
}  