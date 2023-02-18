from flask import Flask,request,render_template
import openai

app = Flask(__name__)
openai.api_key = "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"

@app.route('/')
def home():
    return render_template('form.html')

@app.route('/generate', methods=['POST'])
def gerar_imagem():
    prompt = request.form.get('input')
    completions = openai.Image.create(
                prompt=prompt,
	            n=1,
	            size="512x512"
    )
    message = completions['data'][0]['url']
    return render_template('form.html', img=message)




if __name__ == '__main__':
    app.run(debug=True)