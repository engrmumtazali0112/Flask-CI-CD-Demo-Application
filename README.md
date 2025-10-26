

A simple Flask web application demonstrating Continuous Integration and Continuous Deployment (CI/CD) using GitHub Actions.

## 🚀 Features

- Simple REST API with Flask
- Automated testing with pytest
- CI/CD pipeline with GitHub Actions
- Automatic deployment on push to main branch

## 📋 Prerequisites

- Python 3.10 or higher
- Git
- GitHub account

## 🛠️ Installation

1. Clone the repository:
```bash
git clone https://github.com/YOUR_USERNAME/flask-cicd-demo.git
cd flask-cicd-demo
```

2. Create virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## 🏃 Running the Application

Start the Flask development server:
```bash
python app.py
```

The application will be available at `http://localhost:5000`

## 🧪 API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/` | GET | Welcome message with app info |
| `/health` | GET | Health check endpoint |
| `/add/<a>/<b>` | GET | Add two numbers |

### Example Requests
```bash
# Home endpoint
curl http://localhost:5000/

# Health check
curl http://localhost:5000/health

# Add numbers
curl http://localhost:5000/add/10/20
```

## 🧪 Running Tests

Run all tests:
```bash
pytest tests/ -v
```

Run with coverage:
```bash
pytest tests/ --cov=app
```

## 🔄 CI/CD Pipeline

The project uses GitHub Actions for automated CI/CD:

### Pipeline Stages:

1. **Test** 🧪
   - Checkout code
   - Setup Python environment
   - Install dependencies
   - Run pytest tests

2. **Build** 🔨
   - Build application
   - Create artifacts

3. **Deploy** 🚀
   - Deploy to production (simulated)
   - Only runs on main/master branch

### Triggering the Pipeline

The pipeline automatically runs when:
- Code is pushed to `main` or `master` branch
- Pull request is created to `main` or `master` branch

## 📂 Project Structure
```
flask-cicd-demo/
│
├── .github/
│   └── workflows/
│       └── ci-cd.yml          # CI/CD pipeline configuration
│
├── tests/
│   └── test_app.py            # Application tests
│
├── app.py                      # Main Flask application
├── requirements.txt            # Python dependencies
├── .gitignore                  # Git ignore file
└── README.md                   # This file
```

## 🧩 Dependencies

- Flask 3.0.0 - Web framework
- pytest 7.4.3 - Testing framework

## ✅ CI/CD Workflow Verification

To verify the CI/CD pipeline is working:

1. Make a change to the code
2. Commit and push to GitHub
3. Go to the "Actions" tab in your GitHub repository
4. Watch the pipeline execute automatically
5. All stages should pass with green checkmarks ✅

## 🎯 Testing the Application

After deployment, test the endpoints:
```bash
# Test home endpoint
curl https://your-app.com/

# Test health endpoint
curl https://your-app.com/health

# Test addition
curl https://your-app.com/add/15/25
```

## 🐛 Troubleshooting

**Tests failing?**
- Check Python version: `python --version`
- Reinstall dependencies: `pip install -r requirements.txt`
- Run tests locally: `pytest tests/ -v`

**Pipeline not triggering?**
- Ensure you're pushing to `main` or `master` branch
- Check GitHub Actions is enabled in repository settings
- Verify `.github/workflows/ci-cd.yml` file exists

## 📝 License

MIT License - feel free to use this project for learning!

## 👨‍💻 Author

Your Name - CI/CD Demo Project

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Run tests locally
5. Submit a pull request

---

**Happy Learning! 🎉**

*This project demonstrates a complete CI/CD pipeline from code commit to deployment.*
