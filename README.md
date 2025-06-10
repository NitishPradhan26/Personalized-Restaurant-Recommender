
# TasteMatch – Personalized Restaurant Recommender
[![React](https://img.shields.io/badge/frontend-react-blue?logo=react)](#)
[![Flask](https://img.shields.io/badge/backend-flask-black?logo=flask)](#)
[![Python](https://img.shields.io/badge/ML-scikit--learn-yellow?logo=python)](#)
[![License: MIT](https://img.shields.io/badge/license-MIT-green)](#)

A lightweight web app that turns your **past orders** into a **taste profile** and instantly recommends restaurants that match your palate.  
Built as a portfolio project to demonstrate full-stack skills and recommender-system design.

---

## ✨ Highlights
- **Personalized recommendations** using a content-based filtering model (no user ratings required).  
- **Taste profile visualization** so users understand *why* each restaurant is suggested.  
- **Sub-second response time** thanks to pre-computed feature vectors and cosine-similarity lookup.  
- **Modern stack:** React(frontend), Flask REST API (backend), Scikit-learn model.  
- **Zero sensitive data:** ships with a tiny synthetic sample so anyone can run the demo locally.

---

## 🔥 Demo
<!-- Replace with your own links / GIFs -->
[Live Demo](https://your-demo-url.com)



## 🚀 Quick Start

1. Make sure you have installed Node.js and npm installer on your machine.

2. Make sure you have python 3, pip installer, and python sklearn on your machine.

3. Run 

        pip install flask python-dotenv
   
   in your terminal to install flask
   
4. Clone the github repository on your machine.

5. For Backend (Open first terminal), 

        cd Website/main
        
        flask --app index.py run
        
   in your terminal to start flask backend. This flask uses localhost:5000 
   
6. For Frontend (Open second terminal), 
  
        cd Website/my-app
        
        npm install
        
  This will automatically help you to install all the necessary components.
  
  Then
      
        npm start
        
  This will start the react website. This react uses localhost:3000 
  
  7. Have Fun!
