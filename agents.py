import os
from crewai import Agent
from langchain_groq import ChatGroq
# from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import re
import PyPDF2


load_dotenv()
# API_KEY = os.getenv("GROQ_API_KEY")

class RFPAgent:
    def __init__(self):
        self.llm = ChatGroq(
            api_key="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",
            model="mixtral-8x7b-32768"
        )
    
    def extract_rfp_info_agent(self):
        return Agent(
            role="RFP Information Extractor",
            goal="""I want you to extract critical information such as title, company name, email, requirements, and project scope from uploaded RFP files (PDF or TXT).""",
            backstory="""As an RFP Information Extractor, you are responsible for identifying and extracting key details from RFP documents to assist in personalized responses.""",
            verbose=True,
            llm=self.llm,
            max_iter=2,
        )

    def extract_rfp_info(self, file_path):
        if file_path.endswith('.pdf'):
            return self._extract_from_pdf(file_path)
        elif file_path.endswith('.txt'):
            return self._extract_from_txt(file_path)
        else:
            raise ValueError("Unsupported file type")

    def _extract_from_pdf(self, file_path):
        rfp_text = ''
        with open(file_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            for page in reader.pages:
                rfp_text += page.extract_text()
        return self._extract_info(rfp_text)
    
    def _extract_from_txt(self, file_path):
        with open(file_path, 'r') as file:
            rfp_text = file.read()
        return self._extract_info(rfp_text)

    def _extract_info(self, rfp_text):
        title = re.search(r"Title:(.*)", rfp_text)
        company_name = re.search(r"Company Name:(.*)", rfp_text)
        email = re.search(r"Email:(.*)", rfp_text)
        requirements = re.search(r"Requirements:(.*)", rfp_text)
        project_scope = re.search(r"Project Scope:(.*)", rfp_text)

        return {
            'title': title.group(1).strip() if title else "N/A",
            'company_name': company_name.group(1).strip() if company_name else "_",
            'email': email.group(1).strip() if email else "N/A",
            'requirements': requirements.group(1).strip() if requirements else "N/A",
            'project_scope': project_scope.group(1).strip() if project_scope else "N/A",
        }

class EmailAgents():
    def __init__(self):
        self.llm = ChatGroq(
            api_key="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",
            model="mixtral-8x7b-32768"
        )
    def personalize_email_agent(self):
        return Agent(
            role="Email Personalizer",
            goal=f""" I want you to personalize template emails for recipients using their information. Given a template email and recipient information (name, email, last conversation), personalize the email by incorporating the recipient's details into the email while maintaining the core message and structure of the original email. This involves updating the introduction, body, and closing of the email to make it more personal and engaging for each recipient.""",
            backstory=""" As an Email Personalizer, you are responsible for customizing template emails for individual recipients based on their information and previous interactions   """,
            verbose=True,
            llm=self.llm,
            max_iter=2,
        )

    def ghostwrite_email_agent(self):
        return Agent(
            role="Ghost writer",
            goal=f""" Revise draft emails to adopt the ghostwriter's writing style. Use an informal, engaging, and slightly sales-oriented tone, mirroring the Ghostwriter's final email communication style. """,
            backstory=""" As a Ghostwriter, you are responsible for revising draft emails to match the Ghostwriter's writing style, focusing on clear, direct communication with a friendly and approachable tone   """,
            verbose=True,
            llm=self.llm,
            max_iter=2,

        )
        
    
class FollowUpAgent():
    def __init__(self):
        self.llm = ChatGroq(
            api_key="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",
            model="mixtral-8x7b-32768"
        )
    def answer_rfp_questions(self):
        return Agent(
            role="RFP Question Answerer",
            goal="""Answer any follow-up questions related to the RFP in a clear, concise, and informative manner. Make sure the answers are aligned with Turnkey's services and capabilities.""",
            backstory="As an RFP Question Answerer, you're responsible for addressing any questions that the client has about the RFP or the proposal submitted.",
            verbose=True,
            llm=self.llm,
            max_iter=2,
        )
