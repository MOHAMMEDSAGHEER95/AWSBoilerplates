import os

import boto3
from botocore.exceptions import NoCredentialsError, PartialCredentialsError

from dotenv import load_dotenv

load_dotenv()



# Define the AWS region and the sender's and receiver's email addresses
AWS_REGION = os.environ.get('AWS_REGION')  # Change to your desired region
SENDER = os.environ.get('SENDER')  # Change to your verified sender's email address
RECIPIENT = os.environ.get('RECIPIENT')  # Change to your recipient's email address
SUBJECT = "Test email from AWS SES"

# The email body for recipients with non-HTML email clients
BODY_TEXT = "This is a test email sent from AWS SES using Boto3."

# The HTML body of the email
BODY_HTML = """<html>
<head></head>
<body>
  <h1>AWS SES Test Email</h1>
  <p>This email was sent with AWS SES using the
    <a href='https://aws.amazon.com/ses/'>AWS SES</a> API and Boto3.
  </p>
</body>
</html>
"""

# The character encoding for the email
CHARSET = "UTF-8"

# Create a new SES resource and specify a region
client = boto3.client('ses', region_name=AWS_REGION)

# Try to send the email
try:
    # Provide the contents of the email
    response = client.send_email(
        Destination={
            'ToAddresses': [
                RECIPIENT,
            ],
        },
        Message={
            'Body': {
                'Html': {
                    'Charset': CHARSET,
                    'Data': BODY_HTML,
                },
                'Text': {
                    'Charset': CHARSET,
                    'Data': BODY_TEXT,
                },
            },
            'Subject': {
                'Charset': CHARSET,
                'Data': SUBJECT,
            },
        },
        Source=SENDER,
    )
except (NoCredentialsError, PartialCredentialsError) as e:
    print(f"Error: {e}")
except Exception as e:
    print(f"Error: {e}")
else:
    print("Email sent! Message ID:"),
    print(response['MessageId'])
