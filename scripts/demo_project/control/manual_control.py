from flask import Flask, render_template, request

app = Flask(__name__)
device_status = {'generator': 'off'}

@app.route('/')
def index():
    return render_template('index.html', status=device_status['generator'])

@app.route('/toggle', methods=['POST'])
def toggle():
    device_status['generator'] = 'on' if device_status['generator'] == 'off' else 'off'
    return render_template('index.html', status=device_status['generator'])

if __name__ == '__main__':
    app.run(debug=True)
