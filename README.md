# Task 4.2 — Flask Hello World App

This repository contains a simple **Flask-based Hello World web application**, created as part of the deployment portfolio.  
The application demonstrates how a minimal Python web service can be containerized and deployed using Docker.

---

## 📂 Code Overview
- **app.py**  
  The main Flask application. It defines a single route (`/`) which returns a simple "Hello, World!" message.  
- **Dockerfile**  
  Instructions for building a Docker image that packages the Flask app inside a container.  
- **requirements.txt**  
  Lists the dependencies needed to run the application (`Flask`).

---

## ▶️ Running the App Locally (without Docker)

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/<your-username>/flask-hello-world.git
   cd flask-hello-world
   ```
2. ** Set up a Python environment **
   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```
3. ** Install reuirements **
   ```bash
   pip install -r requirements.txt\
   ```     
4. ** Run the app **
   ```bash
   python app.py
   ```
5. Visit http://localhost:4000 in your browser to see it running

## 🐳Pulling from Docker Hub

   ```bash
    docker login
    docker pull eshita20/py-hello:1.1
    docker run -d -p 4000:80 eshita20/py-hello:1.1

   ```

   


   
   
