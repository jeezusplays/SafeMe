// Datatables script
$(document).ready(function () {
    $('#example').DataTable();
});

//Get check-in modal buttons to show success toast in disasters near me
const toastTrigger1 = document.getElementById('liveToastBtn1')
const toastLiveExample1 = document.getElementById('liveToast1')
if (toastTrigger1) {
    toastTrigger1.addEventListener('click', () => {
    // const toastBootstrap = bootstrap.Toast.getOrCreateInstance(toastLiveExample)
    const toastBootstrap1 = new bootstrap.Toast(toastLiveExample1)
    toastBootstrap1.show()
    })
}

const toastTrigger2 = document.getElementById('liveToastBtn2')
const toastLiveExample2 = document.getElementById('liveToast2')
if (toastTrigger2) {
    toastTrigger2.addEventListener('click', () => {
    // const toastBootstrap = bootstrap.Toast.getOrCreateInstance(toastLiveExample)
    const toastBootstrap2 = new bootstrap.Toast(toastLiveExample2)
    toastBootstrap2.show()
    })
}

const toastTrigger3 = document.getElementById('liveToastBtn3')
const toastLiveExample3 = document.getElementById('liveToast3')
if (toastTrigger3) {
    toastTrigger3.addEventListener('click', () => {
    // const toastBootstrap = bootstrap.Toast.getOrCreateInstance(toastLiveExample)
    const toastBootstrap3 = new bootstrap.Toast(toastLiveExample3)
    toastBootstrap3.show()
    })
}





//Show modal on load (for some reason if i put this at the top, it will casue other scripts to fail to run)
const checkInModal = new bootstrap.Modal('#checkInModal')
window.addEventListener('DOMContentLoaded', () => {
    checkInModal.show()
})

