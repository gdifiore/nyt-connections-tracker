import os
from flask import Flask, render_template, request, session
from connections_parser import parse_connections_puzzle
from calculations import calculate_average_guesses

app = Flask(__name__)
app.secret_key = os.environ.get('FLASK_SESSION_SECRET')

def initialize_session():
    session.setdefault('puzzle_number', 0)
    session.setdefault('total_puzzles', 0)
    session.setdefault('avg_guesses', 0)

def process_puzzle_submission(puzzle_text):
    puzzle_number, results, guesses = parse_connections_puzzle(puzzle_text)

    if puzzle_number is None:
        return render_template('index.html',
                               error_message="Invalid input. Please copy from the NYT Connections results page.", avg_guesses=session['avg_guesses'])

    if puzzle_number <= session['puzzle_number']:
        return render_template('index.html',
                               error_message="You've already entered this puzzle in the past.", avg_guesses=session['avg_guesses'])

    session['puzzle_number'] = puzzle_number
    session['total_puzzles'] += 1
    print(session['total_puzzles'])

    print(f"[DEBUG] Puzzle #{puzzle_number} Results:")
    for category, is_correct in results.items():
        print(f"{category}: {'Correct' if is_correct else 'Incorrect'}")

    # only recalculate average if all categories are correct
    if results == {'Yellow': True, 'Green': True, 'Blue': True, 'Purple': True}:
        session['avg_guesses'] = calculate_average_guesses(session['avg_guesses'], session['total_puzzles'], guesses)

    return render_template('index.html', puzzle_number=puzzle_number, results=results, avg_guesses=session['avg_guesses'])

@app.before_request
def make_session_permanent():
    session.permanent = True

@app.route('/', methods=['GET', 'POST'])
def index():
    initialize_session()

    if request.method == 'POST':
        puzzle_text = request.form['puzzle_text']
        return process_puzzle_submission(puzzle_text)

    return render_template('index.html', avg_guesses=session['avg_guesses'])

@app.route('/reset', methods=['GET'])
def reset_session():
    session.clear()
    return render_template('reset.html')

if __name__ == '__main__':
    app.run(debug=False, port=int(os.environ.get('PORT', 5000)))
