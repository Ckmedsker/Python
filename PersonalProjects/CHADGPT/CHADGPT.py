import creds
import openai

openai.api_key = creds.API_KEY
adjective = "sandwich"

# recipient_name = input("To whom is this email addressing?\n")
# email_subject = input("What is the subject of this email?\n")
subject = input("What would you like CHAD GPT to write about?\n")
additional = input("Anything else chad GPT needs to know?\n")


# user_message = (f"Write a grammatically incorrect {adjective}, passive aggressive email complaining and expressing a problem to {recipient_name} about {email_subject}. From Karen.")
user_message = (f"Write a inspiration speech about {subject} in the tone of a cool college frat guy. Also, {additional}")

response = openai.ChatCompletion.create(
    model = 'gpt-3.5-turbo', 
    messages = [
    {'role': 'user', 'content': user_message}
    ]
)

# print(response.choices[0].message.content)