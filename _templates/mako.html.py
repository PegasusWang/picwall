# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1440940675.270408
_enable_loop = True
_template_filename = '/Users/pegasus/Program/py_test/picwall/templates/mako.html'
_template_uri = 'mako.html'
_source_encoding = 'utf-8'
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        static_url = context.get('static_url', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'<!doctype html>\n<html lang="zh-CN">\n<head>\n    <meta charset="UTF-8">\n    <title>infinitescroll</title>\n    <link rel="stylesheet" href="')
        __M_writer(unicode( static_url("css/reset.css") ))
        __M_writer(u'">\n    <link rel="stylesheet" href="')
        __M_writer(unicode( static_url("css/reset.css") ))
        __M_writer(u'">\n    <link rel="stylesheet" href="')
        __M_writer(unicode( static_url("css/waterfall.css") ))
        __M_writer(u'">\n</head>\n<body>\n<div id="header">\n    <h1>infinitescroll</h1>\n</div>\n<div id="container"></div>\n<script type="text/x-handlebars-template" id="waterfall-tpl">\n\n')
        __M_writer(u'\n{{#result}}\n    <div class="item">\n        <img src="{{image}}" width="{{width}}" height="{{height}}" />\n    </div>\n{{/result}}\n')
        __M_writer(u'\n\n</script>\n<script src="')
        __M_writer(unicode( static_url("js/libs/jquery/jquery.js") ))
        __M_writer(u'"></script>\n<script src="')
        __M_writer(unicode( static_url("js/libs/handlebars/handlebars.js") ))
        __M_writer(u'"></script>\n<script src="')
        __M_writer(unicode( static_url("js/waterfall.min.js") ))
        __M_writer(u'"></script>\n<script>\n$(\'#container\').waterfall({\n    itemCls: \'item\',\n    colWidth: 222,\n    gutterWidth: 15,\n    gutterHeight: 15,\n    checkImagesLoaded: false,\n    path: function(page) {\n        return \'data/data1.json?page=\' + page;\n    }\n});\n</script>\n<script type="text/javascript">\nvar _gaq = _gaq || [];\n_gaq.push([\'_setAccount\', \'UA-1245097-16\']);\n_gaq.push([\'_trackPageview\']);\n_gaq.push([\'_trackPageLoadTime\']);\n(function() {\n    var ga = document.createElement(\'script\'); ga.type = \'text/javascript\'; ga.async = true;\n    ga.src = \'https://ssl.google-analytics.com/ga.js\';\n    var s = document.getElementsByTagName(\'script\')[0]; s.parentNode.insertBefore(ga, s);\n})();\n</script>\n</body>\n</html>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"32": 26, "33": 27, "34": 27, "35": 28, "36": 28, "42": 36, "16": 0, "22": 1, "23": 6, "24": 6, "25": 7, "26": 7, "27": 8, "28": 8, "29": 17, "30": 23, "31": 26}, "uri": "mako.html", "filename": "/Users/pegasus/Program/py_test/picwall/templates/mako.html"}
__M_END_METADATA
"""
