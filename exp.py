

from openai import OpenAI

from aider import env
from aider.coders.base_coder import Coder
from aider.models import Model
OPENAI_API_KEY = ''
BASE_URL = 'https://api.openai.com/v1'
BASE_MODEL = 'gpt-4o'
task = '''Modify the Settings.js component to render the list of studios and add a delete button next to each studio.'''
files=['/Users/metehanoz/FumeData/a1723821574-fume-metehanozmtf-27f9cb8b/fume-auth/src/pages/Settings.js']
task_id = 'a1723821574-fume-metehanozmtf-27f9cb8b'


model = Model(model=BASE_MODEL)
model.edit_format = 'diff'

coder = Coder.create(fnames=files, main_model=model,use_git= False,task_id=task_id,api_key=OPENAI_API_KEY,base_url=BASE_URL,edit_format='diff')
coder.run(task)
