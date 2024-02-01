# ATSPro: The Ultimate ATS Companion

ATSPro is a state-of-the-art Streamlit application designed to empower job seekers in conquering Applicant Tracking Systems (ATS) with unmatched precision and insight. This README provides comprehensive guidance on setting up and utilizing ATSPro to enhance your job application process.

Access the ATSPro Here: [ATSPro](https://atspro-75be453458c3.herokuapp.com/)

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
    git clone https://github.com/TVR28/ATSPro
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
```



## Usage

ATSPro facilitates a variety of functionalities tailored to enhance your resume and prepare you for job applications:

- **Resume Analysis**: Upload your resume and paste the job description to receive detailed feedback on how well your resume matches the job requirements.

- **Match Percentage**: Get a quantifiable match percentage indicating how closely your resume aligns with the job description, along with matched and missing keywords.

- **Skills Improvement**: Receive suggestions on skills to improve or acquire based on the job description and your current resume.

- **Customization Tips**: Obtain tailored advice on editing your resume bullet points to better match the job description.

- **Interview Prep**: Access custom-generated interview questions and suggested answers based on your resume and the job role.

## Features

- **Resume to Job Description Matching**: Utilizes Google's Generative AI to compare your resume against job descriptions, identifying strengths and areas for improvement.

- **Interactive UI**: Streamlit-powered interface for easy upload of resumes, input of job descriptions, and interaction with the application's features.

- **Dynamic Content Generation**: Generates custom content such as interview prep questions and resume customization tips using advanced AI models.

- **Visual Customizations**: Supports background image customization and CSS styling for a personalized user experience.

## Contributing

Contributions to ATSPro are welcome! If you'd like to contribute, please follow these steps:

1. Fork the repository to your own GitHub account.
2. Create a new branch for your feature or bug fix.
3. Commit your changes and push them to your fork.
4. Submit a pull request with a clear description of your changes.
