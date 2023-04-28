from flask import Flask, url_for

app = Flask(__name__)


@app.route('/')
@app.route('/carousel')
def carousel():
    return f'''<!doctype html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title>Пейзажи Марса</title>
    <link rel="stylesheet"
          href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
          integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
          crossorigin="anonymous">

    <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}"/>
</head>
<body>
<h1>Пейзажи Марса</h1>
<div id="carouselExampleIndicators" class="carousel slide" data-ride="carousel">
    <ol class="carousel-indicators">
        <li data-target="#carouselExampleIndicators" data-slide-to="0" class="active"></li>
        <li data-target="#carouselExampleIndicators" data-slide-to="1"></li>
        <li data-target="#carouselExampleIndicators" data-slide-to="2"></li>
    </ol>
    <div class="carousel-inner">
        <div class="carousel-item active">
            <img class="d-block w-100" src="{url_for('static', filename='img/mars1.jpg')}" alt="First slide">
        </div>
        <div class="carousel-item">
            <img class="d-block w-100" src="{url_for('static', filename='img/mars2.jpg')}" alt="Second slide">
        </div>
        <div class="carousel-item">
            <img class="d-block w-100" src="{url_for('static', filename='img/mars3.jpg')}" alt="Third slide">
        </div>
    </div>
    <a class="carousel-control-prev" href="#carouselExampleIndicators" role="button" data-slide="prev">
        <span class="carousel-control-prev-icon" aria-hidden="true"></span>
        <span class="sr-only">Previous</span>
    </a>
    <a class="carousel-control-next" href="#carouselExampleIndicators" role="button" data-slide="next">
        <span class="carousel-control-next-icon" aria-hidden="true"></span>
        <span class="sr-only">Next</span>
    </a>
</div>
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
<script src="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/js/bootstrap.min.js"></script>
</body>
</html>'''


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
