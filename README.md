# Moka

Moka is a suite of generative AI tools, utilities and notebooks. The notebooks
folder contains some sample code on prompt engineering, langchain and stable diffusion
from deeplearning.ai course. 

Other utilities are:

1. Slack-copywriter --> A basic flask app to write social media contents based on 
standardized instructions.
2. TODO
3. TODO

To run the utilities you will need to install the package manager Poetry: https://python-poetry.org/


## 2. Run the slack-copywriter app

1. Navigate to the Moka directory and add your [API key](https://beta.openai.com/account/api-keys) to a newly created `.env` file.


2. Install libraries and dependencies:
```bash
   $ poetry install
```

3. Activate the virtual environment using Poetry:
```bash
   $ poetry shell
```

4. Navigate into the project directory:

   ```bash
   $ cd slack-copywriter
   ```

5. Run the flask app in debug mode

   ```bash
   $ flask --app app run --debug
   ```
The app will be available to access at [http://localhost:5000](http://localhost:5000)! 
