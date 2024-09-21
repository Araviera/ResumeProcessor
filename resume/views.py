from django.http import JsonResponse
from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import re
import PyPDF2

@method_decorator(csrf_exempt, name='dispatch')
class ExtractResumeView(View):
    def post(self, request, *args, **kwargs):
        resume_file = request.FILES.get('resume')
        if not resume_file:
            return JsonResponse({'error': 'No file uploaded'}, status=400)

        try:
            resume_info = extract_resume_info(resume_file)
            return JsonResponse(resume_info)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

def extract_resume_info(resume_file):
    # Read the PDF file
    pdf_reader = PyPDF2.PdfReader(resume_file)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text()

    # Extract information using regular expressions
    name = extract_name(text)
    email = extract_email(text)
    mobile_number = extract_mobile_number(text)

    return {
        "first_name": name,
        "email": email,
        "mobile_number": mobile_number
    }


def extract_name(text):
    match = re.search(r'\b\w+\b', text)
    return match.group(0) if match else "Unknown"

def extract_email(text):
    match = re.search(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', text)
    return match.group(0) if match else "Unknown"

def extract_mobile_number(text):
    match = re.search(r'\+\d{1,3}[-.]?\d{3}[-.]?\d{3}[-.]?\d{4}\b', text)
    return match.group(0) if match else "Unknown"