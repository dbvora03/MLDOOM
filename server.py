from flask import *
from flask_cors import CORS
import gpt_2_simple as gpt2


app = Flask(__name__)
CORS(app)

@app.route('/getPhrases')
def get_lyrics():
    sess = gpt2.start_tf_sess()
    gpt2.load_gpt2(sess, run_name='run1')
    lyrics = gpt2.generate(sess, run_name='run1',  length=250, temperature=0.9, return_as_list=True)
    print(lyrics)
    return {'lyrics': lyrics}


if __name__ == "__main__":
    app.run()
