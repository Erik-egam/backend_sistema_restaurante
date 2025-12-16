from dotenv import load_dotenv
import os

load_dotenv()

SECRET=os.getenv("SECRET")
ACCESS_TOKEN_DURATION=int(os.getenv("ACCESS_TOKEN_DURATION"))
ALGORITHM=os.getenv("ALGORITHM")