var clicked = false;
var powerbiInfo = document.getElementById("powerbi-info");
var baseDate = document.getElementById("baseline-date");
var endDate = document.getElementById("enddate");
var today = new Date();

baseDate.value = "2010-01-01";
if ( (today.getMonth()+1).toString().length == 1 ) {
    var month = "0"+today.getMonth();
}
else {
    month = today.getMonth();
}
if ( (today.getDate()).toString().length == 1 ) {
    var date_today = "0"+today.getDate();
}
else {
    date_today = today.getDate();
}

endDate.value = today.getFullYear()+'-'+month+'-'+date_today;

// update.onclick = function setActions() {
//     if (powerbiInfo.style.display == "block") {
//         powerbiInfo.style.display = "none";
//     }
//     document.getElementById("exchange-info").style.display = "block";   
// } 

powerbi.onclick = function displayInfo() {
    if (document.getElementById("exchange-info").style.display == "block"){
        document.getElementById("exchange-info").style.display = "none" 
    }
    powerbiInfo.style.display = "block";
    clicked = true;
};

exchange.onclick = function updateExchangeRates() {
    if (powerbiInfo.style.display == "block") {
        powerbiInfo.style.display = "none";
    }
    // document.getElementById("exchange-info").style.display = "block";
};

document.onclick = function hideInfo() {
    if (! clicked) {
        powerbiInfo.style.display = "none";
    }
    else {
        clicked = false;
    }    
};