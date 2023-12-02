import json

with open("user_config.json") as f:
    json_str = f.read()
    json_dict = json.loads(json_str)

USER_TOKEN = json_dict["user_token"]
USER_NAME = json_dict["user_name"]
USER_EMAIL = json_dict["user_email"]
MAIN_DIR = json_dict["main_dir"]
