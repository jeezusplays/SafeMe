// Datatables script
$(document).ready(function () {
    $('#example').DataTable();
});

//Load modal on load
const checkInModal = new bootstrap.Modal('#checkInModal')
window.addEventListener('DOMContentLoaded', () => {
    checkInModal.show()
})
