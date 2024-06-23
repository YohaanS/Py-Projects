$('#soda').hide()

sodaproject = function() {
    $('#cal').hide()
    $('#soda').show()
}

calproject = function() {
    $('#cal').show()
    $('#soda').hide()
}

let clickcount = 0

$("#project-button").on("click", function() {
    clickcount++

    if (clickcount % 2 == 1) {
        // First click (or odd-numbered clicks)
        console.log("Next Project")
        sodaproject()
    } else {
        // Second click (or even-numbered clicks)
        console.log("Next Project")
        calproject()
    }
})