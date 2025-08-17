🖼️ Text-to-Image Generator
A modern, AI-powered web application that transforms text prompts into stunning images using FastAPI and Hugging Face's Inference API. Built with a clean, modular architecture and deployed seamlessly on Render.

✨ Features
AI-Powered Generation: Create high-quality images from text descriptions
Modular Architecture: Clean separation of concerns for easy maintenance
Responsive Web Interface: Simple, intuitive HTML-based frontend
Secure Configuration: Environment-based API key management
Cloud Ready: One-click deployment on Render
🏗️ Project Structure
image_generator_app/
├── app/
│   ├── __init__.py
│   ├── main.py             # FastAPI application & routes
│   ├── image_service.py    # Core image generation logic
│   └── templates/
│       └── index.html      # User interface
├── run.py                  # Local development server
├── requirements.txt        # Python dependencies
├── .env.example           # Environment variables template
└── README.md              # Project documentation
🚀 Quick Start
Prerequisites
Python 3.8 or higher(prefere 3.10)
Git
Hugging Face account
Installation
Clone the repository
bash
git clone https://github.com/22bsm056/text-to-image-generator.git
cd image_generator_app
Set up virtual environment
python -m venv venv

# Activate virtual environment
# On macOS/Linux:
source venv/bin/activate
# On Windows:
venv\Scripts\activate
Install dependencies
bash
pip install -r requirements.txt
Configure environment variables
bash
cp .env.example .env
# Edit .env and add your Hugging Face token:
# HF_TOKEN=your_actual_token_here
Running Locally
bash
python run.py
Open your browser and navigate to http://127.0.0.1:8000 to start generating images!

☁️ Deployment
Deploy on Render
Push to GitHub
bash
git add .
git commit -m "Initial commit"
git push origin main
Create Render Service
Go to Render Dashboard
Click "New" → "Web Service"
Connect your GitHub repository
Configure Settings
Build Command: pip install -r requirements.txt
Start Command: uvicorn app.main:app --host 0.0.0.0 --port $PORT
Environment Variables: Add HF_TOKEN with your API key
Deploy
Click "Create Web Service"
Wait for deployment to complete
🔧 Configuration
Environment Variables
Variable	Description	Required
HF_TOKEN	Hugging Face API token	Yes
MODEL_ID	Hugging Face model ID	No (default: stable-diffusion)
Supported Models
stabilityai/stable-diffusion-2-1
runwayml/stable-diffusion-v1-5
CompVis/stable-diffusion-v1-4
📖 API Documentation
Generate Image
Endpoint: POST /generate-image

Request Body:

json
{
  "prompt": "A serene sunset over mountains with a lake reflection"
}
Response:

json
{
  "image_url": "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAA..."
}
🛠️ Development

Code Structure
app/main.py: FastAPI application with route handlers
app/image_service.py: Core business logic for image generation
app/templates/: Frontend templates and static assets
run.py: Development server entry point
🔒 Security Best Practices
Never commit API keys to version control
Use environment variables for sensitive configuration
Add .env to your .gitignore file
Regularly rotate API tokens
🐛 Troubleshooting
Common Issues
"Invalid API token"

Verify your Hugging Face token is correct
Ensure the token has proper permissions
"Model not found"


🤝 Contributing
Fork the repository
Create a feature branch (git checkout -b feature/amazing-feature)
Commit your changes (git commit -m 'Add amazing feature')
Push to the branch (git push origin feature/amazing-feature)
Open a Pull Request

🙏 Acknowledgments
Hugging Face for providing the inference API
FastAPI for the excellent web framework
Render for seamless deployment

Issues
Hugging Face Documentation
FastAPI Documentation
Made with ❤️ for the AI community

