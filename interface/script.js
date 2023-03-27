// Datatables script
$(document).ready(function () {
    $('#example').DataTable();
});

//Show modal on load
const checkInModal = new bootstrap.Modal('#checkInModal')
window.addEventListener('DOMContentLoaded', () => {
    checkInModal.show()
})

//Get check-in modal buttons to show success toast
// const toastTrigger = document.getElementById('liveToastBtn')
// // const toastTrigger = document.getElementsByClassName('myBtn')[0]
// const toastLiveExample = document.getElementById('liveToast')

// if (toastTrigger) {
//   const toastBootstrap = bootstrap.Toast.getOrCreateInstance(toastLiveExample)
//   toastTrigger.addEventListener('click', () => {
//     toastBootstrap.show()
//   })
// }