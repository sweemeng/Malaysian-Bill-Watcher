from bottle import static_file,route


@route('/js/<path:filepath>')
def js_views(filepath):
    pass

@route('/css/<path:filepath>')
def css_views(filepath):
    pass
