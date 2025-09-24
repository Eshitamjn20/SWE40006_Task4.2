from flask import Flask
app = Flask(__name__)

@app.get("/")
def hello():
    return """
    <html>
      <head>
        <title>Dockerized Flask App</title>
        <style>
          body {
            background-color: #f4f4f9;
            font-family: Arial, sans-serif;
            text-align: center;
            padding: 50px;
          }
          h1 {
            color: #2F4F4F;
          }
          p {
            color: #555;
            font-size: 18px;
          }
          .container {
            background: white;
            border-radius: 10px;
            box-shadow: 0 4px 8px rgba(0,0,0,0.1);
            padding: 30px;
            display: inline-block;
          }
        </style>
      </head>
      <body>
        <div class="container">
          <h1>Hello, world !</h1>
          <p>This Flask app is running inside a Docker container!</p>
        </div>
      </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
