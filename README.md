# Soliyev Calculation Platform

A specialized math computation API and interactive web interface developed as a **university project**. This platform provides a suite of mathematical functions served through a high-performance FastAPI backend.

**Live Demo:** [https://project320.onrender.com](https://project320.onrender.com)  
*(Hosted on Render Free Plan - Please allow a few seconds for the instance to spin up on the first request).*

---

## 🚀 Features

* **Cyberpunk UI:** A sleek, modern "Avatar-style" web interface with glassmorphism effects and particle animations.
* **Dual Protocol Support:** All mathematical functions are accessible via both `GET` (query parameters) and `POST` (JSON body) requests.
* **Interactive Documentation:** Automatic Swagger/OpenAPI documentation.
* **Core Functions:**
    * **Hypotenuse Calculation:** Geometric computations.
    * **Multiplication:** Basic product calculation.
    * **Comparison:** Logic-based value comparison.
    * **Division:** Quotient calculation with error handling.
    * **Linear Function:** Specialized formula $f(x, y) = 6x + 7y$.

---

## 🛠 Tech Stack

* **Backend:** FastAPI (Python 3.9+)
* **Validation:** Pydantic models
* **Frontend:** HTML5, CSS3 (Custom animations), Vanilla JavaScript
* **Deployment:** Render

---

## 📖 API Reference

### 1. Interactive Docs
Once the server is running, you can explore the full API schema at:
* **Swagger UI:** `/docs`
* **ReDoc:** `/redoc`

### 2. Available Endpoints
All endpoints accept two variables: `x` and `y` (floats).

| Endpoint | Method | Description |
| :--- | :--- | :--- |
| `/` | GET | Serves the interactive web interface |
| `/ilyas` | GET/POST | Hypotenuse/Basic Math logic |
| `/soliyev` | GET/POST | Number multiplication |
| `/artur` | GET/POST | Comparison/Specific math logic |
| `/inoyatov` | GET/POST | Division of numbers |
| `/Shakirjanov` | GET/POST | Result of $6x + 7y$ |

---

## 💻 Local Setup

1.  **Clone the repository:**
    ```bash
    git clone <your-repo-url>
    cd <project-folder>
    ```

2.  **Install dependencies:**
    *(Ensure you have Python installed)*
    ```bash
    pip install fastapi uvicorn pydantic
    ```

3.  **Run the application:**
    ```bash
    uvicorn main:app --reload
    ```

4.  **Access the app:**
    Open [http://127.0.0.1:8000](http://127.0.0.1:8000) in your browser.

---

## 📂 Project Structure

* `main.py`: The FastAPI application containing all routes and server configurations.
* `functions.py`: The core logic module where mathematical formulas are defined.
* `index.html`: The frontend user interface with embedded CSS/JS.
* `requirements.txt`: List of necessary Python packages.

---

## 🎓 University Project
This project was developed as part of a university assignment to demonstrate skills in **API development**, **Web design**, and **Full-stack integration**.

**Developed by:** Soliyev and Team.