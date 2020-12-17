function showDetails(eventtime, eventname, pagename) {
    $('#schedule-content').load(pagename + '.html')
    $('#schedule-name').html(eventtime + " - <strong>" + eventname + "</strong>")
}

