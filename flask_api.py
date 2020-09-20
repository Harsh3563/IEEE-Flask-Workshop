from flask import Flask, render_template, url_for

app = Flask(__name__)
app.config["ALLOWED_IMAGE_EXTENSIONS"] = ["JPEG", "JPG", "PNG"]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')

@app.route('/image')
def image():
	return render_template('image.html')

@app.route('/predict', methods = ['POST'] )
def upload():
    return 0

	# UPLOADING FILE


	# POST REQUEST
    # if request.method == 'POST':
	   
	#     f = request.files['file']
	#     fname=secure_filename(f.filename)

	#     if allowed_image(fname):
	#     	basepath = os.path.dirname(__file__)
	#     	file_path = os.path.join(basepath, 'uploads', fname)
	#     	f.save(file_path)
	#     	photo = extract_features(file_path, xception_model)
	#     	description = generate_desc(model, tokenizer, photo, max_length)
	#     	result= description[6:-3]
	#     	if os.path.exists(file_path):
	#     		os.remove(file_path)
	#     	return result
	#     else:
	#     	return 'Error occured, Please ensure you\'re using jpeg or jpg file format.' 
	# return None

if __name__== '__main__': 
    app.run(debug=True)         # run in debug mode