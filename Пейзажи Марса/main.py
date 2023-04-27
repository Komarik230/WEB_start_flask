from flask import Flask, url_for

app = Flask(__name__)

@app.route('/')
@app.route('/carousel')
def carousel():
    return f'''<!doctype html>
                    <html lang="en">
                      <head>
                        <meta charset="utf-8">
                        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">
                        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-ka7Sk0Gln4gmtz2MlQnikT1wXgYsOg+OMhuP+IlRH9sENBO0LRn5q+8nbTov4+1p" crossorigin="anonymous"></script>

                        <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                        <title>Пейзажи Марса</title>
                      </head>
                      <body>
                        <h1 class='text'>Пейзажи Марса</h1>
                        <div id="carouselExampleControls" class="carousel slide" data-bs-ride="carousel">
                          <div class="carousel-inner">
                            <div class="carousel-item active image">
                              <img src="static/img/i.png" class="d-block w-100" alt="...">
                            </div>
                            <div class="carousel-item image">
                              <img src="static/img/i.jpg" class="d-block w-100" alt="...">
                            </div>
                            <div class="carousel-item image">
                              <img src="static/img/i(2).jpg" class="d-block w-100" alt="...">
                            </div>
                            <div class="carousel-item image">
                              <img src="static/img/i(3).jpg" class="d-block w-100" alt="...">
                            </div>
                            <div class="carousel-item image">
                              <img src="static/img/i(4).jpg" class="d-block w-100" alt="...">
                            </div>
                          </div>
                          <button class="carousel-control-prev" type="button" data-bs-target="#carouselExampleControls" data-bs-slide="prev">
                            <span class="carousel-control-prev-icon" aria-hidden="true"></span>
                            <span class="visually-hidden">Previous</span>
                          </button>
                          <button class="carousel-control-next" type="button" data-bs-target="#carouselExampleControls" data-bs-slide="next">
                            <span class="carousel-control-next-icon" aria-hidden="true"></span>
                            <span class="visually-hidden">Next</span>
                          </button>
                        </div>
                      </body>
                    </html>'''


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
