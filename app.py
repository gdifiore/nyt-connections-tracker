from flask import Flask, render_template, request
from connections_parser import parse_connections_puzzle

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        puzzle_text = request.form['puzzle_text']
        puzzle_number, results = parse_connections_puzzle(puzzle_text)

        print(f"[DEBUG] Puzzle #{puzzle_number} Results:")
        for category, is_correct in results.items():
            print(f"{category}: {'Correct' if is_correct else 'Incorrect'}")

        return render_template('index.html', puzzle_number=puzzle_number, results=results)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
