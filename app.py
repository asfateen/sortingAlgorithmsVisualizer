from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

def bubble_sort(numbers):
    steps = []
    n = len(numbers)
    final = []

    for i in range(n):
        for j in range(0, n-i-1):
            steps.append({
                'array': numbers.copy(),
                'compare': (j, j+1),
                'final': final[:]
            })
            if numbers[j] > numbers[j+1]:
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
            steps.append({
                'array': numbers.copy(),
                'compare': [],
                'final': final[:]
            })
        final.append(n - i - 1)
        steps.append({
            'array': numbers.copy(),
            'compare': [],
            'final': final[:]
        })
    return steps


def optimized_bubble_sort(numbers):
    steps = []
    n = len(numbers)
    final = []

    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            steps.append({
                'array': numbers.copy(),
                'compare': (j, j+1),
                'final': final[:]
            })
            if numbers[j] > numbers[j+1]:
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
                swapped = True
            steps.append({
                'array': numbers.copy(),
                'compare': [],
                'final': final[:]
            })

        if not swapped:
            final = list(range(n))
            steps.append({
                'array': numbers.copy(),
            'compare': [],
            'final': final[:]
            })
            return steps

        final.append(n - i - 1)
        steps.append({
            'array': numbers.copy(),
            'compare': [],
            'final': final[:]
        })
        


    return steps

def selection_sort(numbers):
    steps = []
    n = len(numbers)
    final = []

    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            steps.append({
                'array': numbers.copy(),
                'compare': (min_idx, j),
                'final': final[:]
            })
            if numbers[min_idx] > numbers[j]:
                min_idx = j
            steps.append({
                'array': numbers.copy(),
                'compare': [],
                'final': final[:]
            })

        numbers[i], numbers[min_idx] = numbers[min_idx], numbers[i]
        final.append(i)
        steps.append({
            'array': numbers.copy(),
            'compare': [],
            'final': final[:]
        })
    return steps

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/sort', methods=['POST'])
def sort():
    numbers = list(map(int, request.form['numbers'].split(',')))
    sort_type = request.form['sort_type']

    if sort_type == 'bubble':
        sort_steps = bubble_sort(numbers.copy())
    elif sort_type == 'optimizedBubble':
        sort_steps= optimized_bubble_sort(numbers.copy())
    elif sort_type == 'selection':
        sort_steps = selection_sort(numbers.copy())

    return jsonify(sort_steps)

if __name__ == '__main__':
    app.run(debug=True)
