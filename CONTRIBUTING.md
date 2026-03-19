# Contributing to AI Touchless Computer Control System

Thank you for your interest in contributing to the AI Touchless Computer Control System! This document provides guidelines and information for contributors.

## 🚀 Ways to Contribute

### Bug Reports and Feature Requests
- Use GitHub Issues to report bugs or suggest features
- Provide detailed descriptions including:
  - Steps to reproduce (for bugs)
  - Expected vs actual behavior
  - System information (OS, Python version, etc.)
  - Screenshots or error messages

### Code Contributions
1. Fork the repository
2. Create a feature branch: `git checkout -b feature/your-feature-name`
3. Make your changes
4. Test thoroughly
5. Commit with clear messages: `git commit -m "Add: brief description of changes"`
6. Push to your fork: `git push origin feature/your-feature-name`
7. Create a Pull Request

## 🛠️ Development Setup

### Prerequisites
- Python 3.7+
- Git
- Webcam and microphone for testing

### Local Development
```bash
# Clone your fork
git clone https://github.com/your-username/AI_Touchless_Control.git
cd AI_Touchless_Control

# Create virtual environment (recommended)
python -m venv venv
venv\Scripts\activate  # Windows
# source venv/bin/activate  # Linux/Mac

# Install dependencies
pip install -r requirements.txt

# Run the application
python backend/main.py
```

## 📝 Code Style Guidelines

### Python Code
- Follow PEP 8 style guidelines
- Use meaningful variable and function names
- Add docstrings to all functions and classes
- Include comments for complex logic
- Keep functions small and focused

### JavaScript Code
- Use modern ES6+ syntax where appropriate
- Follow consistent naming conventions
- Add comments for complex logic
- Keep functions small and focused

### HTML/CSS
- Use semantic HTML elements
- Follow BEM naming convention for CSS classes
- Ensure responsive design
- Maintain accessibility standards

## 🧪 Testing

### Manual Testing Checklist
- [ ] Gesture control works with different lighting conditions
- [ ] Voice commands are recognized accurately
- [ ] Web dashboard loads on different browsers
- [ ] System starts and stops without errors
- [ ] Camera feed updates in real-time
- [ ] Status indicators update correctly

### Performance Testing
- Test with different camera resolutions
- Check memory usage during extended use
- Verify response times for voice commands
- Test concurrent gesture and voice operations

## 📚 Documentation

### Code Documentation
- Update README.md for any new features
- Add docstrings to new functions
- Update requirements.txt if new dependencies are added
- Include usage examples for new features

### User Documentation
- Keep setup instructions current
- Document any new configuration options
- Update troubleshooting section as needed

## 🔧 Feature Development

### Gesture Control Enhancements
- Improve hand detection accuracy
- Add more gesture types (right-click, double-click, etc.)
- Implement calibration for different skin tones
- Add gesture sensitivity settings

### Voice Control Improvements
- Add custom command creation
- Improve recognition accuracy
- Support multiple languages
- Add voice feedback

### UI/UX Improvements
- Add dark mode toggle
- Improve mobile responsiveness
- Add keyboard shortcuts
- Enhance accessibility

## 🚨 Issue Reporting

When reporting issues, please include:
- **Title**: Clear, descriptive title
- **Description**: Detailed explanation of the issue
- **Steps to reproduce**: Step-by-step instructions
- **Expected behavior**: What should happen
- **Actual behavior**: What actually happens
- **Environment**: OS, Python version, browser, etc.
- **Screenshots/Logs**: Visual evidence or error logs

## 📞 Getting Help

- **Documentation**: Check the README.md first
- **Issues**: Search existing issues before creating new ones
- **Discussions**: Use GitHub Discussions for questions
- **Code Review**: All PRs require review before merging

## 🎯 Code of Conduct

- Be respectful and inclusive
- Focus on constructive feedback
- Help newcomers learn and contribute
- Maintain professional communication

Thank you for contributing to make this project better! 🎉