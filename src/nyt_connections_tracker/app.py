import os
import secrets
from flask import Flask, render_template, request, session
from nyt_connections_tracker.connections_parser import parse_connections_puzzle
from nyt_connections_tracker.calculations import calculate_average_guesses

app = Flask(__name__)
app.secret_key = os.environ.get('FLASK_SESSION_SECRET', secrets.token_hex(32))

def initialize_session():
    """Initialize session defaults."""
    session.setdefault('puzzle_number', 0)
    session.setdefault('total_puzzles', 0)
    session.setdefault('avg_guesses', 0)
    session.setdefault('category_counts', {'Yellow': 0, 'Green': 0, 'Blue': 0, 'Purple': 0})

def process_puzzle_submission(puzzle_text):
    """Process submitted puzzle and update session."""
    puzzle_number, results, guesses = parse_connections_puzzle(puzzle_text)

    if puzzle_number is None:
        return render_template('index.html',
                               error_message="Invalid input. Please copy from the NYT Connections results page.", avg_guesses=session['avg_guesses'])

    if puzzle_number <= session['puzzle_number']:
        return render_template('index.html',
                               error_message="You've already entered this puzzle in the past.", avg_guesses=session['avg_guesses'])

    session['puzzle_number'] = puzzle_number
    session['total_puzzles'] += 1

    for category, is_correct in results.items():
        if is_correct:
            session['category_counts'][category] += 1

    if results == {'Yellow': True, 'Green': True, 'Blue': True, 'Purple': True}:
        session['avg_guesses'] = calculate_average_guesses(session['avg_guesses'], session['total_puzzles'], guesses)

    return render_template('index.html',
                         puzzle_number=puzzle_number,
                         results=results,
                         avg_guesses=session['avg_guesses'],
                         category_counts=session['category_counts'],
                         total_puzzles=session['total_puzzles'])

@app.before_request
def make_session_permanent():
    session.permanent = True

@app.route('/', methods=['GET', 'POST'])
def index():
    initialize_session()

    if request.method == 'POST':
        puzzle_text = request.form['puzzle_text']
        return process_puzzle_submission(puzzle_text)

    return render_template('index.html',
                         avg_guesses=session['avg_guesses'],
                         category_counts=session['category_counts'],
                         total_puzzles=session['total_puzzles'])

@app.route('/reset', methods=['GET'])
def reset_session():
    session.clear()
    return render_template('reset.html')

if __name__ == '__main__':
    app.run(debug=False, port=int(os.environ.get('PORT', 5000)))
