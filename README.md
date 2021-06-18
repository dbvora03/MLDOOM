# ML DOOM

ML DOOM is a a project that uses GPT-2 to generate lyrics that mimic your favourite rapper's favourite rapper: MF DOOM. The purpose of this project is to take the concept of "DOOM bots" even further. As a rapper who revolves around the " mastermind supervillain" theme, DOOM bots are people hired by MF DOOM who perform at concerts and go into public as MF DOOM himself. What if we took DOOM bots one step further by creating a bot that generates MF DOOM lyrics.... without MF DOOM. 

---

### How does it work?
ML DOOM uses GPT-2, a transformer-based language model that was trained on 8 million web pages. The model was fine-tuned using using over 1800 MF DOOM lyrics scraped using Beautiful soup. I don't have a GPU on my machine, so I trained my model on Colab and imported a `checkpoint/` folder to my local directory. The model was then put on a Flask application to communicate to the React front end. 

---

### How can I run this on my machine?
1. Add `mfdoom.txt` to your google drive
2. Follow the instructions on [this Colab notebook](https://colab.research.google.com/drive/11WefYtgmUY58m6mngRqXEoR9C_SEJ0TU?usp=sharing) (this will take forever)
3. Download the `checkpoint/` to your local directory
4. Add a `config.py` file to the main directory and add a `GENIUS_API_TOKEN` variable
5. Run the following commands for the backend:
```bash
$ pip install -r requirements.txt

$ python server.py
```
6. Run the following commands for the front-end
```
$ cd frontend

$ npm i 

$ npm start
```
7. Do whatever you want with it. If it's cool, make a pull request 😼

