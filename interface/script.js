// Datatables script
$(document).ready(function () {
    setTimeout(() => {
        var table = $('#datatable').DataTable({
        });

        $('#datatable tbody').on('click', 'tr', function () {
            var data = table.row(this).data();
            // alert('You clicked on ' + data[2] + "'s row");

            const str = data[3];

            // Use the match() method with a regular expression to extract the content within parentheses
            const matches = str.match(/\((.*?)\)/);
            
            // Log the matches to the console
            if (matches && matches.length === 2) {
                const content = matches[1];
                const lat = parseFloat(content.split(',')[0]);
                const lng = parseFloat(content.split(',')[1]);
                console.log(lat); // Output: '48.857, 2.352'
                console.log(lng); // Output: '48.857, 2.352'

                // Destroy the map
                $('#map').empty();
                // Call the function to create the map
                initMap_2(lat, lng);

            } else {
              console.log('No content found within parentheses');
            }
        });
    }, 500);
});


function initMap_2(lat, lng) {
    // The location of SCIS at SMU
    var location_selected = { lat: lat, lng: lng };
    // The map, centered at SCIS
    var map = new google.maps.Map(document.getElementById("map"), {
        zoom: 14,
        center: location_selected,
    });
    // The marker, positioned at SCIS, SMU by default
    var iconBase = '../img/default-marker.png';
    var marker = new google.maps.Marker({
        position: location_selected,
        map,
        icon: iconBase
    });
}

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
for (let status of statusToasts) {
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
for (let report of reportToasts) {
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
for (let volunteer of volunteerPublicToasts) {
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

