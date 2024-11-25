from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


@app.route('/')
def form():
    return render_template('pagina1.html')


if __name__ == '__main__':
    app.run()
