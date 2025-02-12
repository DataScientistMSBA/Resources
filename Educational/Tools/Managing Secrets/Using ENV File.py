import os
from dotenv import load_dotenv

load_dotenv()

test_token = os.getenv("TEST_TOKEN")
print(test_token)