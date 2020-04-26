var clicked = false;
var powerbi = document.getElementById("powerbi");
var exchange = document.getElementById("exchange");
var powerbiInfo = document.getElementById("powerbi-info");

function setInfo(replace_str,target) {
    var infoMsg = powerbiInfo.innerText.replace(replace_str,target);
    powerbiInfo.innerText = infoMsg;
    powerbiInfo.style.display = "block";
    clicked = true;
};

function getReplace(){
    if(powerbiInfo.innerText.search(powerbi.innerText) > 0){
        return powerbi.innerText;
    }
    else if(powerbiInfo.innerText.search(exchange.innerText) > 0){
        return exchange.innerText;
    }
    else{
        return "&feature";
    }    
};

powerbi.onclick = function displayInfo() {
    var replace = getReplace();
    setInfo(replace,powerbi.innerText);
};

exchange.onclick = function displayInfo() {
    var replace = getReplace();
    setInfo(replace,exchange.innerText);
};

document.onclick = function hideInfo() {
    if (! clicked) {
        powerbiInfo.style.display = "none";
    }
    else {
        clicked = false;
    }    
};