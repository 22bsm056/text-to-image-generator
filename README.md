Text-to-Image Generator
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
