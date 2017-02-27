from flask import Flask, render_template,request,redirect

app=Flask(__name__)

def search4phrase(phrase:str, letters:str='aeiou') -> set:
    """Return a set of the 'letters' found in a supplied 'phrase'."""
    return set(letters).intersection(set(phrase))

@app.route('/')
@app.route('/entry')
def entry_page() -> 'html':
	return render_template('entry.html',
		the_title='Welcome to search4letters on the web!')


@app.route('/search4',methods=['POST'])
def do_search() -> 'html':
	phrase=request.form['phrase']
	letters=request.form['letters']
	results=str((search4phrase(phrase,letters)))
	title='Here are your results!'
	return render_template('results.html',
		the_title=title,
		the_results=results,
		the_letters=letters,
		the_phrase=phrase,)

if __name__=='__main__':
	app.run(debug=True)