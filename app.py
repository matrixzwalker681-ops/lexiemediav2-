from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return """
    <html>
    <head><title>LEXIEMEDIA by XCLOUD GBL</title>
    <style>
    body{background:#0f0f0f;color:white;text-align:center;font-family:sans-serif;padding-top:80px}
    h1{font-size:50px;color:#00ff88;text-shadow:0 0 20px #00ff88}
    h2{color:#aaa}
    .btn{background:#00ff88;color:black;padding:15px 30px;border-radius:30px;text-decoration:none;font-weight:bold;font-size:20px}
    </style>
    </head>
    <body>
    <h1>LEXIEMEDIA</h1>
    <h2>by XCLOUD GBL</h2>
    <p>Your Premium Media Platform is LIVE!</p><br><br>
    <a class="btn" href="#">Enter Platform</a>
    <p style="margin-top:60px;color:#555">Powered by MatrixZ Walker</p>
    </body>
    </html>
    """

if __name__ == '__main__':
    app.run()
