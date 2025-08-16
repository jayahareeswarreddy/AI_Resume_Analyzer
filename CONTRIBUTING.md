# 🤝 Contributing to AI Resume Analyzer & LinkedIn Scraper

We love your input! We want to make contributing to this project as easy and transparent as possible, whether it's:

- 🐛 Reporting a bug
- 💡 Discussing the current state of the code
- 📝 Submitting a fix
- 🚀 Proposing new features
- 📖 Becoming a maintainer

## 🚀 Quick Start

### **Fork & Clone**
```bash
# 1. Fork the repository on GitHub
# 2. Clone your fork locally
git clone https://github.com/yourusername/AI-Resume-Analyzer.git
cd AI-Resume-Analyzer

# 3. Add the original repository as upstream
git remote add upstream https://github.com/original-owner/AI-Resume-Analyzer.git
```

### **Setup Development Environment**
```bash
# 1. Create a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run the status checker
python check_status.py

# 4. Start the development server
python -m streamlit run app.py
```

## 📝 Development Workflow

### **1. Create a Feature Branch**
```bash
# Always work on a new branch
git checkout -b feature/amazing-feature
# or
git checkout -b fix/bug-fix
```

### **2. Make Your Changes**
- Write clean, readable code
- Add comments where necessary
- Follow the existing code style
- Test your changes thoroughly

### **3. Commit Your Changes**
```bash
# Use conventional commit messages
git commit -m "feat: add new resume analysis feature"
git commit -m "fix: resolve Chrome driver issue"
git commit -m "docs: update README with new features"
```

### **4. Push and Create Pull Request**
```bash
git push origin feature/amazing-feature
# Then create a Pull Request on GitHub
```

## 📋 Pull Request Guidelines

### **Before Submitting**
- [ ] Code follows the existing style
- [ ] All tests pass
- [ ] Documentation is updated
- [ ] No sensitive data is included
- [ ] Changes are tested locally

### **Pull Request Template**
```markdown
## Description
Brief description of changes

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Documentation update
- [ ] Performance improvement

## Testing
- [ ] Tested locally
- [ ] All existing tests pass
- [ ] New tests added (if applicable)

## Screenshots (if applicable)
Add screenshots to help explain your changes

## Checklist
- [ ] My code follows the style guidelines
- [ ] I have performed a self-review
- [ ] I have commented my code where necessary
- [ ] I have made corresponding changes to documentation
```

## 🐛 Reporting Bugs

### **Bug Report Template**
```markdown
## Bug Description
Clear and concise description of the bug

## Steps to Reproduce
1. Go to '...'
2. Click on '...'
3. Scroll down to '...'
4. See error

## Expected Behavior
What you expected to happen

## Actual Behavior
What actually happened

## Environment
- OS: [e.g. Windows 10, macOS, Ubuntu]
- Python Version: [e.g. 3.8, 3.9, 3.10]
- Browser: [e.g. Chrome, Firefox, Safari]

## Additional Context
Any other context about the problem
```

## 💡 Suggesting Enhancements

### **Feature Request Template**
```markdown
## Problem Statement
Is your feature request related to a problem? Please describe.

## Proposed Solution
Describe the solution you'd like to see.

## Alternative Solutions
Describe any alternative solutions you've considered.

## Additional Context
Add any other context or screenshots about the feature request.
```

## 📚 Code Style Guidelines

### **Python Code Style**
- Follow PEP 8 guidelines
- Use meaningful variable names
- Add docstrings to functions and classes
- Keep functions small and focused

### **Example**
```python
def analyze_resume(pdf_file, api_key):
    """
    Analyze a resume PDF using AI.
    
    Args:
        pdf_file: Uploaded PDF file
        api_key: Groq API key for analysis
        
    Returns:
        dict: Analysis results including strengths, weaknesses, and suggestions
    """
    # Implementation here
    pass
```

## 🧪 Testing

### **Running Tests**
```bash
# Run status checker
python check_status.py

# Test the application
python -m streamlit run app.py

# Test specific components
python -c "import app; print('App imports successfully')"
```

### **Adding Tests**
- Add tests for new features
- Ensure existing tests still pass
- Test edge cases and error conditions

## 📖 Documentation

### **Updating Documentation**
- Update README.md for new features
- Add inline code comments
- Update requirements.txt if dependencies change
- Keep setup instructions current

## 🚀 Deployment

### **Testing Before Deployment**
```bash
# 1. Test locally
python -m streamlit run app.py

# 2. Check all dependencies
python check_status.py

# 3. Test with sample data
# Use demo_resume.txt for testing

# 4. Verify no sensitive data is committed
git diff --cached
```

## 🤝 Community Guidelines

### **Be Respectful**
- Be kind and respectful to other contributors
- Provide constructive feedback
- Help others learn and grow

### **Communication**
- Use clear, concise language
- Ask questions when unsure
- Share knowledge and best practices

## 📞 Getting Help

### **Resources**
- [GitHub Issues](https://github.com/yourusername/AI-Resume-Analyzer/issues)
- [GitHub Discussions](https://github.com/yourusername/AI-Resume-Analyzer/discussions)
- [Documentation](README.md)

### **Contact**
- Open an issue for bugs or feature requests
- Use discussions for general questions
- Tag maintainers for urgent issues

## 🎉 Recognition

### **Contributors**
All contributors will be recognized in:
- README.md contributors section
- GitHub contributors page
- Release notes

### **Types of Contributions**
- 🐛 Bug reports
- 💡 Feature requests
- 📝 Documentation improvements
- 🧪 Testing and quality assurance
- 🚀 Code contributions

---

**Thank you for contributing to AI Resume Analyzer & LinkedIn Scraper!** 🚀

Your contributions help make this tool better for job seekers worldwide. 