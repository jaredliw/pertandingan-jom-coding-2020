$("#one-line-js").keypress(function(event) {
    if (event.which == 13) {
        alert("Function is Called on Enter");
        event.preventDefault(); //Add this line to your code
    }
});