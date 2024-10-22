from crewai import Task



class PersonalizeEmailTask():
    def personalize_email(self, agent, recipient, email_template):
        return Task(
            description=f"""
                Personalize the template email for recipient using their information.

                - Name: {recipient['first_name']} {recipient['last_name']}
                - Email: {recipient['email']}
                - Last conversation: {recipient['last_conversation']}

                Important Info to consider:
                - When personalizing the email, only use one sentence from the last conversation. 
                    And make sure to incorporate it naturally into the email.  without going too much in to detail.
                - Make sure to keep the updated email roughly the same same length as the template email.
                
                The template email is as follows:

                ```
                {email_template}
                ```
            """,
            agent=agent,
            expected_output=f"Personalized email draft.",
            async_execution=True,
        )

    def ghostwrite_email(self, agent, draft_email, recipient):
        return Task(
            description=f"""
                Revise the draft email to adopt the following writing style.

                Writing Style:
                - Use a more informal, engaging, and slightly sales-oriented tone, mirroring ghost writer's final email communication style. 
                - This approach prioritizes clear, direct communication while maintaining a friendly and approachable tone. 
                - Use straightforward language, including phrases like "Hey [Name]!" to start emails or messages. 
                - The tone will be optimistic and encouraging, aiming to build rapport and motivate action, while staying grounded in practical advice.

                Important Notes:
                - Do not use emojis.
            """,
            agent=agent,
            context=[draft_email],
            expected_output=f"A revised email draft in ghost writer's specified tone and style, without any emojis or special characters.",
            output_file=f"output/{recipient['first_name']}_{recipient['last_name']}.txt",
        )

class RFPExtractionTask():
    def extract_rfp_info(self, agent, file_path):
        return Task(
            description=f"""
                Extract all the critical information from the RFP document.
                
                File Path: {file_path}

                Extract the following information:
                - Title
                - Company Name
                - Email of the sender
                - Requirements
                - Project Scope
            """,
            agent=agent,
            expected_output="Extracted RFP information",
            async_execution=True,
        )