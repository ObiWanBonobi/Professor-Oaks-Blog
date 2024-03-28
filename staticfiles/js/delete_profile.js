// Const for delete button for comments
const deleteModal = new bootstrap.Modal(document.getElementById("deleteModal"));
const deleteButtons = document.getElementsByClassName("btn-delete");
const deleteConfirm = document.getElementById("deleteConfirm");


// Initializes deletion functionality for the provided delete button on profile.
for (let button of deleteButtons) {
    button.addEventListener("click", (e) => {
      let userId = e.target.getAttribute("user_id");
      deleteConfirm.href = `user_delete/${userId}`;
      deleteModal.show();
    });
}