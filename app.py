from flask import Flask, render_template, request, session
from connections_parser import parse_connections_puzzle
import os

app = Flask(__name__)
app.secret_key = os.environ.get('FLASK_SESSION_SECRET')

@app.route('/', methods=['GET', 'POST'])
def index():
    session.setdefault('puzzle_number', 0)

    if request.method == 'POST':
        puzzle_text = request.form['puzzle_text']
        puzzle_number, results = parse_connections_puzzle(puzzle_text)

        if puzzle_number is None:
            return render_template('index.html', error_message="Invalid input. Please copy from the NYT Connections results page.")
        elif session['puzzle_number'] <= puzzle_number:
            return render_template('index.html', error_message="You've already entered this puzzle in the past.")
        else:
            session['puzzle_number'] = puzzle_number

        print(f"[DEBUG] Puzzle #{puzzle_number} Results:")
        for category, is_correct in results.items():
            print(f"{category}: {'Correct' if is_correct else 'Incorrect'}")

        return render_template('index.html', puzzle_number=puzzle_number, results=results)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5000)))
