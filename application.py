from flask import Flask
from flask import request, jsonify
import sys
import shopee
import lazada
import youtube

application = Flask(__name__)

@application.route('/post', methods=['POST'])
def post():
    json = request.get_json()
    print(json, file=sys.stdout)
    #print('Error', file=sys.stderr)
    return jsonify({'success': True})

@application.route('/', methods=['GET'])
@application.route('/index', methods=['GET'])
def index():
    #print('Error', file=sys.stderr)
    # return jsonify({'success': True})
    return '<p>Hello %s!</p>\n'

@application.route('/nlp', methods=['GET'])
def nlp():
    review_num = request.args.get('review_num')
    # Default 10
    if type(review_num) != str:
        review_num = 10
    else:
        review_num = int(review_num)
    reviews = shopee.get_reviews(1529516322, 66397495, review_num=review_num)
    only_review_text = []
    for review in reviews:
        only_review_text.append(review['review'])
    return {0: only_review_text}

@application.route('/youtube_search',methods=['GET'])
def youtube_search():
    video_title = request.args.get('video_title')
    max_result = request.args.get('max_result')
    
    if type(review_num) != str:
        review_num = "meme_video"
    if type(max_result) != str:
        max_result = 5
    else:
        max_result = int(max_result)
    
    return youtube.search_result(video_title, max_result)

if __name__ == "__main__":
    # Setting debug to True enables debug output. This line should be
    # removed before deploying a production app.
    application.debug = True
    application.run()