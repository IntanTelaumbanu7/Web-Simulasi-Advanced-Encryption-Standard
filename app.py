from flask import Flask, render_template, request
from aes import aes_process, SAMPLES

app = Flask(__name__)

DEFAULT_FORM = {
    'mode': 'encrypt',
    'input_type': 'hex',
    'input_value': '',
    'key': '',
    'sample': 'std',
}

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    error = None
    form = DEFAULT_FORM.copy()

    if request.method == 'GET':
        sample = SAMPLES['std']
        form.update({'input_value': sample['plain_hex'], 'key': sample['key'], 'sample': 'std'})

    if request.method == 'POST':
        submit_action = request.form.get('submit_action', '')
        selected_mode = request.form.get('mode', 'encrypt')
        if submit_action in ('encrypt', 'decrypt'):
            selected_mode = submit_action

        form.update({
            'mode': selected_mode,
            'input_type': request.form.get('input_type', 'hex'),
            'input_value': request.form.get('input_value', '').strip(),
            'key': request.form.get('key', '').strip(),
            'sample': request.form.get('sample', 'manual'),
        })
        if form['mode'] == 'decrypt':
            form['input_type'] = 'hex'
        try:
            result = aes_process(form['mode'], form['input_value'], form['input_type'], form['key'])
        except Exception as exc:
            error = str(exc)

    return render_template('index.html', result=result, error=error, form=form, samples=SAMPLES)

if __name__ == '__main__':
    app.run(debug=True)
