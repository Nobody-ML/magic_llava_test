import os

os.system("ls")
os.system("cd /home/xlab-app-center")
os.system("ls")

test = os.getenv("TEST")
print(test)
os.system("cd /home/xlab-app-center/app_test/")
os.system("pip install -r /home/xlab-app-center/app_test/requirements.txt")
os.system("python app_test/download.py")
# os.system("cd /home/xlab-app-center/app_test/internvl_chat_llava")
# os.system("python -m llava.serve.controller --host 0.0.0.0 --port 10000")

# os.system("cd /home/xlab-app-center/app_test/internvl_chat")
# os.system("python -m internvl.serve.model_worker --host 0.0.0.0 --controller http://localhost:10000 --port 40005 --worker http://localhost:40005 --model-path /home/xlab-app-center")

# os.system("cd /home/xlab-app-center/app_test/internvl_chat_llava")
# os.system("python -m llava.serve.gradio_web_server --controller http://localhost:10000 --model-list-mode reload")

# os.system("cd /home/xlab-app-center/app_test/internvl_chat_llava/ && python -m llava.serve.controller --host 0.0.0.0 --port 10000")
# os.system("python -m llava.serve.controller --host 0.0.0.0 --port 10000")

# os.system("cd /home/xlab-app-center/app_test/internvl_chat/ && python -m internvl.serve.model_worker --host 0.0.0.0 --controller http://localhost:10000 --port 40005 --worker http://localhost:40005 --model-path /home/xlab-app-center")
# os.system("python -m internvl.serve.model_worker --host 0.0.0.0 --controller http://localhost:10000 --port 40005 --worker http://localhost:40005 --model-path /home/xlab-app-center")

os.system("bash app_test/create.sh")
os.system("cd /home/xlab-app-center/app_test/internvl_chat_llava/ && python -m llava.serve.gradio_web_server --controller http://localhost:10000 --model-list-mode reload")
# os.system("python -m llava.serve.gradio_web_server --controller http://localhost:10000 --model-list-mode reload")
