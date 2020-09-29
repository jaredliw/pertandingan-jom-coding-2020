function dec2bin(dec){
    return (dec >>> 0).toString(2);
}

function convertBase(hint) {
    var x = document.getElementById("from-value").value;
    var y = document.getElementById("to-value").value;
    var msg = document.getElementById("error-msg");

    if (hint == "from") {
        if (x > 9007199254740991) {
            msg.style.display = "block";
            msg.textContent = "Input asas 10 terlalu besar untuk ditukarkan kepada asas 2. Sila cuba lagi dengan nilai yang lebih kecil.";
            document.getElementById("to-value").value = "";
            return;
        } else if (x == "") {

        } else if (!(/^\d+$/.test(x))) { // check if input only contains digits
            msg.style.display = "block";
            msg.textContent = "Input asas 10 tidak sah. Sila memastikan input anda hanya mengandungi [0, 1, 2, 3, 4, 5, 6, 7, 8, 9].";
            document.getElementById("to-value").value = "";
            return;
        }
        document.getElementById("to-value").value = dec2bin(x);
    } else if (hint == "to") {
        if (x > 11111111111111111111111111111111) {
                msg.style.display = "block";
                msg.textContent = "Input asas 2 terlalu besar untuk ditukarkan kepada asas 10. Sila cuba lagi dengan nilai yang lebih kecil.";
                document.getElementById("to-value").value = "";
                return;
            } else if (x == "") {

            } else if (!(/^\d+$/.test(x))) { // check if input only contains digits
                msg.style.display = "block";
                msg.textContent = "Input asas 2 tidak sah. Sila memastikan input anda hanya mengandungi [0, 1].";
                document.getElementById("to-value").value = "";
                return;
            }
        document.getElementById("from-value").value = parseInt(y, 2);
    }
    msg.style.display = "none";
    return;
}