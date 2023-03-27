// Datatables script
$(document).ready(function () {
    $('#example').DataTable();
});

//Adds event listeners to 'Disasters Near Me' modals to trigger toasts
const statusToasts = [
    {
        buttonID: 'liveToastBtn1',
        toastID: 'okay'
    },
    {
        buttonID: 'liveToastBtn2',
        toastID: 'mildlyInjured'
    },
    {
        buttonID: 'liveToastBtn3',
        toastID: 'severelyInjured'
    },
]
for (let status of statusToasts){
    console.log('HI')
    const toastTrigger = document.getElementById(status.buttonID)
    const toastLiveExample = document.getElementById(status.toastID)
    if (toastTrigger) {
        toastTrigger.addEventListener('click', () => {
            const toastBootstrap = new bootstrap.Toast(toastLiveExample)
            toastBootstrap.show()
        })
    }
}





//Show modal on load (for some reason if i put this at the top, it will casue other scripts to fail to run)
const checkInModal = new bootstrap.Modal('#checkInModal')
window.addEventListener('DOMContentLoaded', () => {
    checkInModal.show()
})

