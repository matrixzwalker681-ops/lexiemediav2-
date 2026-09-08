from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return """
<html>
<head><title>LEXIEMEDIA by XCLOUD GBL</title>
<style>
body{background:#0f0f0f;color:white;text-align:center;font-family:Arial;padding-top:50px}
h1{font-size:50px;color:#00ff88;text-shadow:0 0 20px #00ff88}
h2{color:#aaa}
.btn{background:#00ff88;color:black;padding:15px 30px;border-radius:30px;text-decoration:none;font-weight:bold;display:inline-block;margin:10px}
.box{border:1px solid #333;padding:20px;margin:20px auto;max-width:400px;border-radius:15px;background:#1a1a1a}
</style>
</head>
<body>
<h1>LEXIEMEDIA</h1>
<h2>by XCLOUD GBL</h2>
<p>Your Premium Media Platform is LIVE!</p>
<a class="btn" href="#">Enter Platform</a>

<div class="box">
<h3>PAYMENT METHODS</h3>
<p><b>M-Pesa:</b> 0795200840</p>
<p><b>PayPal:</b> walker@xcloud.com</p>
<p><b>Bank:</b> KCB - LEXIEMEDIA</p>
</div>

<div class="box">
<h3>CONTACT</h3>
<p>WhatsApp: 0795200840</p>
<p>Email: lexi@media.com</p>
</div>

<p style="margin-top:60px;color:#555">Powered by MatrixZ Walker</p>
</body>
</html>
    """

if __name__ == '__main__':
    app.run()
