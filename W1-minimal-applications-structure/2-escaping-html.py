#When returning HTML (the default response type in Flask), any user-provided values rendered in the output must be escaped to protect from injection attacks. HTML templates rendered with Jinja, introduced later, will do this automatically.

#escape(), shown here, can be used manually. It is omitted in most examples for brevity, but you should always be aware of how you’re using untrusted data.
from urllib import request
from flask import Flask # type: ignore
from markupsafe import escape # type: ignore
app = Flask(__name__)

@app.route("/<name>")
def hello(name):
    return f"Hello {escape(name)}!"


@app.route('/advanced/<script_value>')
def handle_script_value(script_value):
    escaped_value = escape(script_value)
    return f'Hello, {escaped_value}!'

if __name__ == '__main__':
    app.run(debug=True)
