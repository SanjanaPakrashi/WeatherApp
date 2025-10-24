# WeatherApp ☀️🌧️

A simple and interactive **Weather Web Application** built with **Flask** and the **OpenWeatherMap API**.  
It allows users to enter a city name and instantly view current weather details such as temperature, humidity, and conditions — complete with dynamic icons that change according to the weather.

### 🌐 Live Demo  
Try the app here: [https://weatherapp-prmh.onrender.com/](https://weatherapp-prmh.onrender.com/)

---

## 📖 Features

- Real-time weather updates using OpenWeatherMap API  
- Responsive interface built with HTML, CSS, and Flask templates  
- Dynamic weather icons that change based on conditions  
- Fully deployed on Render with auto-deployment from GitHub  
- Environment variable protection for sensitive API keys  

---

## ⚙️ Tech Stack

- **Frontend:** HTML, CSS, JavaScript  
- **Backend:** Python (Flask Framework)  
- **API:** OpenWeatherMap API  
- **Hosting:** Render (Free Tier)  
- **Version Control:** Git & GitHub  

---

## 🚀 Getting Started (Run Locally)

### 1. Clone this repository
git clone https://github.com/SanjanaPakrashi/WeatherApp.git
cd WeatherApp


### 2. Setup virtual environment
python -m venv venv
source venv/bin/activate # On Windows: venv\Scripts\activate


### 3. Install dependencies
pip install -r requirements.txt


### 4. Add your OpenWeatherMap API key  
Create a `.env` file in your root directory and add:  
API_KEY=your_api_key_here


### 5. Run the app locally
python app.py


The app will be available at:  
http://127.0.0.1:5000/

---

## 🧩 Deployment on Render

This app is ready to deploy to Render, including:
- `Procfile` for Gunicorn web server  
- `requirements.txt` with dependencies  
- Environment variable setup for secure API keys

Render auto-deploys from your GitHub repo whenever you push changes to `main`.

---

## 🛠️ Project Structure

WeatherApp/
│
├── static/ # CSS, images, JS files
├── templates/ # HTML templates
├── app.py # Main Flask application
├── requirements.txt # Python dependencies
├── Procfile # Render start command
└── README.md # This file

---

## 🧠 Future Enhancements

- Add 7-day weather forecast support  
- Geolocation-based weather auto detection  
- Dockerize app & improve CI/CD workflows  
- Temperature unit toggle (°C / °F)

---

## 🤝 Contributing

Contributions are welcome!  
1. Fork the repo  
2. Create your feature branch: `git checkout -b feature-name`  
3. Commit your changes: `git commit -m "Add feature"`  
4. Push to the branch: `git push origin feature-name`  
5. Open a Pull Request  

---

## 📜 License

This project is licensed under the MIT License.

---

## 👩‍💻 About the Author

**Sanjana Pakrashi**  
Computer Science Engineering Student  
GitHub: [SanjanaPakrashi](https://github.com/SanjanaPakrashi)
