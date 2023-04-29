import openai
import creds

openai.api_key = creds.API_KEY
adjective = "sandwich"

recipient_name = input("To whom is this email addressing?\n")
email_subject = input("What is the subject of this email?\n")

user_message = (f"Write a grammatically incorrect {adjective}, passive aggressive email complaining and expressing a problem to {recipient_name} about {email_subject}. From Karen.")

response = openai.ChatCompletion.create(
    model = 'gpt-3.5-turbo', 
    messages = [
    {'role': 'user', 'content': user_message}
    ]
)

print(response.choices[0].message.content)