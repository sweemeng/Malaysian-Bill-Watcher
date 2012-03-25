from bottle import static_file,route


@route('/js/<filepath:path>')
def js_views(filepath):
    return static_file(filepath,root='js/')

@route('/css/<filepath:path>')
def css_views(filepath):
    return static_file(filepath,root='css/')
