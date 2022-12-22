from app import create_app

app = create_app()


@app.before_request
def start_up():
    print("start")


@app.after_request
def stopping(res):
    print("stopping")
    return res


if __name__ == '__main__':
    app.run(debug=True, host="127.0.0.1", port=5000)
