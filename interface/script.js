// Datatables script
$(document).ready(function () {
    setTimeout(() => {
        $('#datatable').DataTable({
            // delay datatable loading until all data is loaded
            stateSave: true,
        });
    }, 500);
});

//Adds event listener to  buttons in 'Disasters Near Me' modal to trigger toasts
const statusToasts = [
    {
        buttonID: 'liveToastBtn1',
        toastID: 'safe'
    },
    {
        buttonID: 'liveToastBtn2',
        toastID: 'injured'
    },
    // {
    //     buttonID: 'liveToastBtn3',
    //     toastID: 'severelyInjured'
    // },
]
for (let status of statusToasts){
    const toastTrigger = document.getElementById(status.buttonID)
    const toastLiveExample = document.getElementById(status.toastID)
    if (toastTrigger) {
        toastTrigger.addEventListener('click', () => {
            const toastBootstrap = new bootstrap.Toast(toastLiveExample)
            toastBootstrap.show()
        })
    }
}

//Adds event listener to buttons in 'Family' cards to trigger toasts upon escalation
const reportToasts = [
    {
        buttonID: '001',
        toastID: 'A'
    },
    {
        buttonID: '002',
        toastID: 'B'
    },
    {
        buttonID: '003',
        toastID: 'C'
    },
    {
        buttonID: '004',
        toastID: 'E'
    },
    {
        buttonID: '005',
        toastID: 'You'
    },
]
for (let report of reportToasts){
    const toastTrigger = document.getElementById(report.buttonID)
    const toastLiveExample = document.getElementById(report.toastID)
    if (toastTrigger) {
        toastTrigger.addEventListener('click', () => {
            const toastBootstrap = new bootstrap.Toast(toastLiveExample)
            toastBootstrap.show()
        })
    }
}


//Adds event listener to buttons in 'Family' cards to trigger toasts upon escalation
const volunteerPublicToasts = [
    {
        buttonID: '1',
        toastID: 'a'
    },
    {
        buttonID: '2',
        toastID: 'b'
    },
    {
        buttonID: '3',
        toastID: 'c'
    },
    {
        buttonID: '4',
        toastID: 'd'
    },
    {
        buttonID: '5',
        toastID: 'e'
    },
]
for (let volunteer of volunteerPublicToasts){
    const toastTrigger = document.getElementById(volunteer.buttonID)
    const toastLiveExample = document.getElementById(volunteer.toastID)
    if (toastTrigger) {
        toastTrigger.addEventListener('click', () => {
            const toastBootstrap = new bootstrap.Toast(toastLiveExample)
            toastBootstrap.show()
        })
    }
}

//Show modal on load (for some reason if i put this at the top, it will cause other scripts to fail to run)
const checkInModal = new bootstrap.Modal('#checkInModal')
window.addEventListener('DOMContentLoaded', () => {
    checkInModal.show()
})

