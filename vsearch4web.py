from flask import Flask, render_template, request, redirect, escape

app = Flask(__name__)


def search4phrase(phrase: str, letters: str = 'aeiou') -> set:
    """Return a set of the 'letters' found in a supplied 'phrase'."""
    return set(letters).intersection(set(phrase))


def log_requst(req: 'flask_request', res: str) -> None:
    with open('vsearch.log', 'a') as log:
        print(
            req.form, request.environ['REMOTE_ADDR'],
            req.user_agent, res, file=log, sep='|')


@app.route('/')
@app.route('/entry')
def entry_page() -> 'html':
    return render_template(
        'entry.html',
        the_title='Welcome to search4letters on the web!')


@app.route('/search4', methods=['POST'])
def do_search() -> 'html':
    phrase = request.form['phrase']
    letters = request.form['letters']
    results = str((search4phrase(phrase, letters)))
    title = 'Here are your results!'
    log_requst(request, results)  # logging the request and results
    return render_template(
        'results.html',
        the_title=title,
        the_results=results,
        the_letters=letters,
        the_phrase=phrase,)


@app.route('/viewlog')
def view_the_log() -> 'html':
    contents = []
    with open('vsearch.log') as log:
        for line in log:
            contents.append([])
            for item in line.split('|'):
                contents[-1].append(escape(item))
    titles = ('Form data', 'Remote_addr', 'User_agent', 'Results')
    return render_template(
        'viewlog.html',
        the_title='View Log',
        the_row_titles=titles,
        the_data=contents,)

if __name__ == '__main__':
    app.run(debug=True)
