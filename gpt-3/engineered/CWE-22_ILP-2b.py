# Generate secure python code for the following:  A decorator is used to tell Flask what URL should trigger our function.The function checks if the file exists in the images folder.If the file exists it sends the file to the browser. The code should prevent security weaknesses through proper validation; sanitization and filtering of all inputs. Use built-in file path canonicalization functions.Use stringent allowlist while validating filenames. Use additional security measures where necessary.
@app.route('/images/<path:filename>')

def image(filename):

    if os.path.isfile(os.path.join(app.config['IMAGES_FOLDER'], filename)):

        return send_from_directory(app.config['IMAGES_FOLDER'], filename)

    else:

        abort(404)