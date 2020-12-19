function showDetails(eventtime, eventname, pagename) {     $('#schedule-content').load(pagename + '.html')
    $('#schedule-name').html(eventtime + " - <strong>" + eventname + "</strong>")
}

//color sticky nav
window.onscroll = function() {colorNav()};
$("#nav").css("position", "fixed")
$("#nav").css("z-index", "2")
function colorNav() {
  if (window.pageYOffset != 0) {
    document.getElementById("nav").classList.add("darkened")
  } else {
    document.getElementById("nav").classList.remove("darkened");
  }
}