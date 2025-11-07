 # ML Linear Regression — Simple Gradient Descent Demo

 This small project demonstrates a hand-implemented simple linear regression trained with gradient descent on a car dataset. It is educational code intended to show the mechanics of mean squared error (MSE), gradients, and iterative parameter updates.

 ## Contents

- `car data.csv`, `CAR DETAILS FROM CAR DEKHO.csv`, `Car details v3.csv`, `car details v4.csv`, `data.csv` — CSV datasets (the notebook uses `car data.csv`).
- `relations.py` — core functions:
  - `MSE(x, y, a, b)` — compute mean squared error
  - `derv_mse_a` / `derv_mse_b` — gradients w.r.t. `a` and `b`
  - `gradient_descent(x, y, learning_rate=0.01, iterations=1000)` — trains `a` and `b`
  - `predictions(x, y, a, b)` — prints predicted vs actual values
- `LRML.ipynb` — the Jupyter notebook that loads the data, trains the model, and plots results.

 ## Quick setup

Recommended: use a virtual environment.

CMD example (run in project root):

```powershell
python -m venv venv; .\venv\Scripts\activate.bat
python -m pip install --upgrade pip
pip install -r requirements.txt
```

If you prefer, you can install packages individually:

```powershell
pip install pandas matplotlib seaborn
```

## How to run

 Start Jupyter in the project folder:

```powershell
jupyter notebook
```

Or Open and run the notebook in VS Code:

- Open the project folder in VS Code.
- Make sure the Python and Jupyter extensions are installed.
- Select the project's virtual environment as the Python interpreter (bottom-right).
- Open LRML.ipynb — use the Run Cell icons or choose "Run All" from the notebook toolbar.
- If prompted to start a Jupyter server or select a kernel, choose the venv kernel.
- If kernels fail, reopen the notebook and explicitly select the venv interpreter from the kernel picker.


What to expect:
- The notebook imports `relations` (the `relations.py` file), reads `car data.csv`, splits train/test, trains via `gradient_descent` and prints progress every 100 iterations.
- After training, the notebook prints the trained parameters `a` and `b` and shows predicted vs actual values and a regression line plot.

## Implementation notes

- The notebook currently uses `x = Selling_Price` and `y = Present_Price` when training.
- `relations.gradient_descent` expects array-like inputs (pandas Series or numpy arrays). It initializes `a` and `b` to 0 and updates them using the analytic gradients implemented in `relations.py`.
- The default notebook hyperparameters are `Lr = 0.0001` and `epochs = 1000`. If the loss does not decrease, try reducing the learning rate or increasing epochs.


## Next improvements (suggested)

- Add a small script to export trained model parameters.

## License

This project is provided as-is for learning purposes. Use and modify freely.
