function showDetails(eventtime, eventname, pagename) {
    $('#schedule-content').load(pagename + '.html')
    $('#schedule-name').html(eventtime + " - <strong>" + eventname + "</strong>")
}

//color sticky nav
window.onscroll = function() {colorNav()};
$("#nav").css("position", "fixed")
function colorNav() {
  if (window.pageYOffset != 0) {
      $("#nav").css("color", "black")
      $("#nav").css("background-color", "#f0f4f4")
    //navbar.classList.add("sticky")
  } else {
    //navbar.classList.remove("sticky");
    $("#nav").css("color", "white")
    $("#nav").css("background-color", "transparent ")
}
}