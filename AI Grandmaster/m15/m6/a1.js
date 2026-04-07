// dice image from value 1 to 6 are given in an array, codes are from Die face Emojipedia
var dices = ['&#9856;', '&#9857;', '&#9858;', '&#9859;', '&#9860;', '&#9861;'];
var stopped = true;

// for keep on changing the dice emojis
function change() {
    var random = Math.floor(Math.random() * 6);
    dice.innerHTML = dices[random];
}

function stopStart() {
    if (stopped) {
        stopped = false;
        // change function is called here to change the image for every 0.1 seconds
        t = setInterval(change, 100);
    } else {
        clearInterval(t);
        stopped = true;
    }
}

// invoking function
window.onload = function() {
    dice = document.getElementById("dice");
    stopStart();
}
