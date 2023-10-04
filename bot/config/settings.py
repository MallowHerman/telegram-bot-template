import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

BASE_DIR = Path(__file__).parent.parent.resolve()


BOT_TOKEN = os.environ.get('BOT_TOKEN')

with open(
    os.path.join(BASE_DIR, 'config', 'chat_messages.yml'), 'r', encoding='utf-8'
) as f:
    chat_messages = yaml.safe_load(f)