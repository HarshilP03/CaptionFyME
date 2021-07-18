import os
from flask import Flask, render_template, redirect, request, url_for
import Caption_it, camera
app = Flask(__name__)


username = None
result = []
res = False

@app.route('/')
def hello():
	return render_template("index.html",res = res)


@app.route('/',methods = ['POST'])
def genscene():
	global res
	global username
	if request.method == "POST" and request.form['btn'] == 'clicked':
		username = request.form['username']
		res = True
		return render_template("index.html",username = username)

	if request.method == "POST" and request.form['btn'] == 'generate':
		if request.files.getlist('photos') is not None:
			for f in request.files.getlist('photos'):
				path = "./static/{}".format(f.filename)
				f.save(path)
				caption = Caption_it.caption_this_image(path)
				print(str(path) + " " + caption)
				result.append({
					'image':path,
					'caption':caption
				})
			
			if res == True:
				clickPath = camera.gen_frame()
				clickCaption = Caption_it.caption_this_image(clickPath)
				result.append({
				'image':clickPath,
				'caption':clickCaption
				})

		return render_template("index.html",username = username,result = result)
		



# @app.route('/video_feed')
# def video_feed():
#     return Response(gen_frame(), mimetype='multipart/x-mixed-replace; boundary=frame')



if __name__ == '__main__':
	app.run(debug = True)

