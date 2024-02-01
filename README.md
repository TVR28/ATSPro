# ATSPro: The Ultimate ATS Companion

ATSPro is a state-of-the-art Streamlit application designed to empower job seekers in conquering Applicant Tracking Systems (ATS) with unmatched precision and insight. This README provides comprehensive guidance on setting up and utilizing ATSPro to enhance your job application process.

## Table of Contents

- [Introduction](#atspro-the-ultimate-ats-companion)
- [Table of Contents](#table-of-contents)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Features](#features)
- [Contributing](#contributing)
- [License](#license)

## Prerequisites

Before you begin with ATSPro, ensure you have the following prerequisites on your system:

- Python 3.7 or higher
- An active Google Cloud account with access to the Generative AI services
- Streamlit installed and configured
- The following Python packages (installable via pip):
    - `streamlit`
    - `PyPDF2` - for processing PDF files
    - `Pillow` - for image processing
    - `python-dotenv` - for environment variable management
    - `pybase64` - for encoding images in base64 format
    - Google Generative AI SDK

## Installation

To install ATSPro, follow these steps:

1. Clone the ATSPro repository to your local machine:

    ```bash
    git clone https://github.com/YourUsername/ATSPro
    cd ATSPro
    ```

2. Set up a Python virtual environment (recommended):

    ```bash
    python -m venv venv
    source venv/bin/activate  # For Windows, use `venv\Scripts\activate`
    ```

3. Install the required Python packages:

    ```bash
    pip install -r requirements.txt
    ```

4. Create a `.env` file in the root directory and add your `GOOGLE_API_KEY`:

    ```
    GOOGLE_API_KEY='YourGoogleAPIKeyHere'
    ```

5. (Optional) Customize the `background.JPG` and any CSS styles in the `styles/main.css` file to personalize your application.

## Getting Started

After installation, you can start ATSPro by running the Streamlit application:

```bash
streamlit run app.py
