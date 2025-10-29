from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def form_page():
    return """
    <html>
        <head>
            <title>Calculator</title>
            <style>
                body {
                    font-family: Arial;
                    background: #f2f2f2;
                    display: flex;
                    flex-direction: column;
                    align-items: center;
                    justify-content: center;
                    height: 100vh;
                }
                form {
                    background: white;
                    padding: 20px 40px;
                    border-radius: 12px;
                    box-shadow: 0 4px 10px rgba(0,0,0,0.2);
                    text-align: center;
                }
                input, select, button {
                    font-size: 18px;
                    padding: 5px 10px;
                    margin: 10px;
                    border-radius: 6px;
                    border: 1px solid #ccc;
                }
                button {
                    background-color: #4CAF50;
                    color: white;
                    cursor: pointer;
                }
                button:hover {
                    background-color: #45a049;
                }
            </style>
        </head>
        <body>
            <form action="/calc" method="get">
                <h2>🧮 Simple Web Calculator</h2>
                <input type="number" name="a" step="any" placeholder="First number" required>
                <select name="op">
                    <option value="+">+</option>
                    <option value="-">-</option>
                    <option value="*">*</option>
                    <option value="/">/</option>
                </select>
                <input type="number" name="b" step="any" placeholder="Second number" required>
                <br>
                <button type="submit">Calculate</button>
            </form>
        </body>
    </html>
    """

@app.get("/calc", response_class=HTMLResponse)
def calc(a: float, b: float, op: str):
    try:
        if op == "+": result = a + b
        elif op == "-": result = a - b
        elif op == "*": result = a * b
        elif op == "/": result = a / b
        else: return f"<h3>❌ Invalid operation: {op}</h3>"
        return f"""
        <html><body style='font-family:Arial;text-align:center;margin-top:50px'>
            <h2>✅ Result: {a} {op} {b} = {result}</h2>
            <a href='/'>← Back</a>
        </body></html>
        """
    except Exception as e:
        return f"<h3>Error: {e}</h3><a href='/'>← Back</a>"
