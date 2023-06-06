import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


def get_key(env_file):
    with open(env_file) as f:
        for line in f:
            if line.startswith('OPENAI_API_KEY'):
                key = line.split('=')[1].strip()
                return key
            else:
                raise ValueError('OPENAI_API_KEY not found in .env file')