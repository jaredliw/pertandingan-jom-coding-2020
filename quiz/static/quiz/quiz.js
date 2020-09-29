var t = setInterval(radioCheck, 500);

function radioCheck() {
    var op1_c = document.getElementById('opt1').checked;
    var op2_c = document.getElementById('opt2').checked;
    var op3_c = document.getElementById('opt3').checked;
    var op4_c = document.getElementById('opt4').checked;
    if (document.getElementById('opt1').disabled) {
        document.getElementById('pass_up_ans').disabled = true;
    } else {
        if (op1_c || op2_c || op3_c || op4_c) {
            document.getElementById('pass_up_ans').disabled = false;
        } else {
            document.getElementById('pass_up_ans').disabled = true;
        }
    }
}