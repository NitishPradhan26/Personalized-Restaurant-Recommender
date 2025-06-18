
# TasteMatch – Personalized Restaurant Recommender
[![React](https://img.shields.io/badge/frontend-react-blue?logo=react)](#)
[![Flask](https://img.shields.io/badge/backend-flask-black?logo=flask)](#)
[![Python](https://img.shields.io/badge/ML-scikit--learn-yellow?logo=python)](#)
[![License: MIT](https://img.shields.io/badge/license-MIT-green)](#)

A lightweight web app that turns your **past orders** into a **taste profile** and instantly recommends restaurants that match your palate.  

---

## ✨ Highlights
- **Hybrid recommendations:** Combines content-based matching **and** a lightweight collaborative layer.  
  - *Content-based* → selects restaurants from a **dummy dataset that mirrors real menus and cuisines**, identifying those that best fit the user’s taste vector.  
  - *Collaborative* → adds “explore” options enjoyed by customers with **similar profiles**, widening variety.  
- **Taste-profile visualization** so users can see *why* each restaurant is suggested.  
- **Sub-second response time** thanks to pre-computed vectors and fast cosine-similarity lookup.  
- **Modern stack:** React, Flask REST API (backend), Scikit-learn model.  
- **Zero sensitive data:** ships with a tiny synthetic sample—original fields are anonymized and identifiers renamed—so anyone can run the demo locally without exposing real data.

---

## 🔥 Demo
<!-- Replace with your own links / GIFs -->
![Live Demo](assets/demo.gif)


## 🚀 Quick Start

1. Make sure you have installed Node.js and npm installer on your machine.

2. Make sure you have python 3, pip installer on your machine.

3. Clone the github repository on your machine.

4. For Backend (Open first terminal), 

        cd Website/main
        python -m venv venv && source venv/bin/activate
        pip install -r requirements.txt
        flask --app index.py run
        
   in your terminal to start flask backend. This flask uses localhost:5000 
   
5. For Frontend (Open second terminal), 
  
        cd Website/my-app
        npm install
        npm start
        
  This will start the react website. This react uses localhost:3000 
  
