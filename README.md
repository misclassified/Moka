# Moka

Moka is a suite of tools to simplify some boring task and stimulate creativity. Powers
Generative AI to let the machine do some heavy lifting on your behalf.


# Run the slack-copywriter app

1. Navigate into the project directory:

   ```bash
   $ cd moka/slack-copywriter
   ```

2. Create a new virtual environment:

   ```bash
   $ python -m venv venv
   $ . venv/bin/activate
   ```

3. Install the requirements:

   ```bash
   $ pip install -r requirements.txt
   ```

4. In the slack-copywriter folder create a .env folder

5. Add your [API key](https://beta.openai.com/account/api-keys) to the newly created `.env` file.

6. Run the app:

   ```bash
   $ flask --app app run --debug
   ```

You should now be able to access the app at [http://localhost:5000](http://localhost:5000)! 