import os
from flask import Flask, render_template, redirect, url_for, request, session
from connections_parser import parse_connections_puzzle
from calculations import calculate_average_guesses

app = Flask(__name__)
app.secret_key = os.environ.get('FLASK_SESSION_SECRET')

def initialize_session():
    session.setdefault('puzzle_number', 0)
    session.setdefault('total_puzzles', 0)
    session.setdefault('avg_guesses', 0)

def process_puzzle_submission(puzzle_text):
    puzzle_number, results = parse_connections_puzzle(puzzle_text)

    if puzzle_number is None:
        return render_template('index.html',
                               error_message="Invalid input. Please copy from the NYT Connections results page.")

    if puzzle_number <= session['puzzle_number']:
        return render_template('index.html',
                               error_message="You've already entered this puzzle in the past.")

    session['puzzle_number'] = puzzle_number

    print(f"[DEBUG] Puzzle #{puzzle_number} Results:")
    for category, is_correct in results.items():
        print(f"{category}: {'Correct' if is_correct else 'Incorrect'}")

    session['avg_guesses'] = calculate_average_guesses(session['avg_guesses'], session['total_puzzles'], len(results))

    return render_template('index.html', puzzle_number=puzzle_number, results=results, avg_guesses=session['avg_guesses'])

@app.route('/', methods=['GET', 'POST'])
def index():
    initialize_session()

    if request.method == 'POST':
        puzzle_text = request.form['puzzle_text']
        return process_puzzle_submission(puzzle_text)

    return render_template('index.html')

@app.route('/reset', methods=['GET'])
def reset_session():
    session.clear()
    return render_template('reset.html')

if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5000)))
