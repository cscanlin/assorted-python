from flask import Flask, stream_with_context, Response
import time

app = Flask(__name__)

@app.route('/')
def streamed_response():
    return Response(stream_with_context(my_function()))

def my_function():
    for _ in range(5):
        time.sleep(.5)
        yield 'Hello</br>'

if __name__ == "__main__":
    app.run()
