function showDetails(eventname, pagename) {
    $('#schedule-content').load(pagename + '.html')
    $('#schedule-name').html(eventname)
}