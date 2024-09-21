# Resume Processor

This is a repository for a Resume Processor project.

## Description

Extract the main info from resumes and return it as JSON

## Features
- Upload resume files in PDF format
- Extract key information from resumes
- Display extracted information in a JSON

## Requirements
- PostgreSQL
- Python
- venv

## Installation
1. Clone the repository: https://gitlab.com/x4695537/ResumeProcessor.git
2. Install the required dependencies: 
```
pip install -r requirements.txt
```
3. Activate the virtual environment.
create the virtual environment with:
```
python3 -m venv venv
```
I am using macOS so I can activate it with:
```
source venv/bin/activate
```

4. Configure your PostgreSQL Database
if you don't have PostgreSQL already installed make sure to install it and start it.
after that configure with the DATABASES in ResumeProcessor/settings.py to match the credentials

5. Apply Migrations
```
python manage.py makemigrations
python manage.py migrate
```
6. Download spaCy Model
```
pip install -U spacy
python -m spacy download en_core_web_sm
```
7. Run the Server
```
python manage.py runserver
```
## note to Mac users
if you are on macOS run 
```
cd /Users/yourusername/Dev/ResumeProcessor/venv/lib/python3.12/site-packages/pyresparser
```
and create a file called config.cfg and add to it:
```
[DEFAULT]
language = en

[RESUME_PARSER]
# Example options for resume parsing
include_contact_info = true
include_education = true
include_experience = true
```
these are features that I am planning to add in the future.

## Usage with Postman

1. create a new POST request and set the URL to http://127.0.0.1:8000/api/extract_resume/
2. in the body tab select form-data
3. add a key named resume and set its type to file
4. choose and upload the resume
5. click send.

## Contributing

Contributions are welcome! If you would like to contribute to this project, please follow these steps:

1. Fork the repository.
2. Create a new branch: `git checkout -b feature/your-feature`
3. Make your changes and commit them: `git commit -m 'Add some feature'`
4. Push to the branch: `git push origin feature/your-feature`
5. Submit a pull request.

## License

This project is licensed under the GNU GENERAL PUBLIC LICENSE Version 2. See the [LICENSE](LICENSE) file for more details.
