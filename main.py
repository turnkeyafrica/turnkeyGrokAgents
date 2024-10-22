import os
from dotenv import load_dotenv
import time
# import csv
import pandas as pd
from crewai import Crew
from langchain_groq import ChatGroq
from agents import EmailAgents, RFPAgent
# from groq import Groq
from tasks import PersonalizeEmailTask, RFPExtractionTask

load_dotenv()


api_key = os.getenv("GROQ_API_KEY")

email_template = """
Subject: Thank You for Considering Turnkey for Your RFP

Hi [Name],

I hope this message finds you well! 

Thank you for the opportunity to submit our proposal for your recent Request for Proposal (RFP). At Turnkey, we are dedicated to providing innovative software solutions tailored specifically for the insurance industry. Our team is committed to helping you navigate the complexities of insurance systems with cutting-edge technology and exceptional service.

We understand the importance of addressing your unique needs, and we are excited about the prospect of partnering with you. Our proposal includes AI integration and guaranteed maintenance, which we believe will greatly enhance your operations.

If you have any questions or would like to discuss our proposal further, please don't hesitate to reach out. We are here to support you every step of the way and ensure that you receive the best possible solutions for your business.

Looking forward to your feedback!

Best regards,

Austine Jack Were
Software Engineer | Turnkey
"""

rfp_agent = RFPAgent()

tasks = PersonalizeEmailTask()
rfp_extraction_task = RFPExtractionTask()
rfp_file_path = 'data/SampleRFP.txt'

rfp_info = rfp_agent.extract_rfp_info(rfp_file_path)
rfp_agent_instance = rfp_agent.extract_rfp_info_agent()


agents = EmailAgents()
email_personalizer = agents.personalize_email_agent()
ghostwriter = agents.ghostwrite_email_agent()



# personalize_email_tasks = []
# ghostwrite_email_tasks = []


# excel_file_path = 'data/clients.xlsx'

# # Reading Excel file into a DataFrame
# df = pd.read_excel(excel_file_path)

# for index, row in df.iterrows():
#     recipient = {
#         'first_name': row['first_name'],
#         'last_name': row['last_name'],
#         'email': row['email'],
#         'last_conversation': row['last_conversation']
#     }

#     personalize_email_task = tasks.personalize_email(
#         agent=email_personalizer,
#         recipient=recipient,
#         email_template=email_template
#     )

#     ghostwrite_email_task = tasks.ghostwrite_email(
#         agent=ghostwriter,
#         draft_email=personalize_email_task,
#         recipient=recipient
#     )

#     personalize_email_tasks.append(personalize_email_task)
#     ghostwrite_email_tasks.append(ghostwrite_email_task)

# Task to extract RFP information

extract_rfp_task = rfp_extraction_task.extract_rfp_info(
    agent=rfp_agent_instance,
    file_path=rfp_file_path
)

recipient = {
    'first_name': "Team",
    'last_name': rfp_info['company_name'],
    'email': rfp_info['email'],
    'last_conversation': rfp_info['project_scope']
}


personalize_email_task = tasks.personalize_email(
    agent=email_personalizer,
    recipient=recipient,
    email_template=email_template
)

ghostwrite_email_task = tasks.ghostwrite_email(
    agent=ghostwriter,
    draft_email=personalize_email_task,
    recipient=recipient
)


crew = Crew(
    agents=[
        rfp_agent_instance,
        email_personalizer,
        ghostwriter
    ],
    tasks=[
        extract_rfp_task,
        personalize_email_task,
        ghostwrite_email_task
    ],
    max_rpm=29
)

start_time =time.time()

results = crew.kickoff()
print(f"Generated email response: {results}")

end_time = time.time()
elapsed_time = end_time - start_time

print(f"Crew kickoff took {elapsed_time} seconds.")
print("Crew usage", crew.usage_metrics)
