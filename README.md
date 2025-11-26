![Title](https://github.com/Mecha-Coder/42-ft-linear-regression/blob/main/demo/Title.png)

## **Overview**

Train a Linear Regression Model with Gradient Descent using the provided dataset. Then, use that model to preduct the car price based on the mileage. 

## **Key Learnings**
- Trained a linear regression model on a given dataset.
- Applied gradient descent to optimize the model and achieve the best fit.
- Normalized and denormalized data.
- Evaluated model performance using Mean Squared Error (MSE) and the coefficient of determination (R²).


## **Read More**

👉 [**Project requirement**](https://github.com/Mecha-Coder/42-ft-linear-regression/blob/main/demo/Linear_Regression.pdf)

👉 [**See my article on how to complete this project**](https://hackmd.io/@Mecha-Coder/42-ft-linear-regression#3-Complete-Assignment)


## Demo

<div align="center">
    <img 
        src="https://raw.githubusercontent.com/Mecha-Coder/42-ft-linear-regression/main/demo/Training.png"
        width="250">
    <p>Training Program</p>
</div>

<div align="center">
    <img 
        src="https://raw.githubusercontent.com/Mecha-Coder/42-ft-linear-regression/main/demo/Predict.png"
        width="250">
    <p>Predict Program</p>
</div>

<div align="center">
    <img 
        src="https://raw.githubusercontent.com/Mecha-Coder/42-ft-linear-regression/main/demo/Bonus.png"
        width="250">
    <p>Bonus Program</p>
</div>

<div align="center">
  <img src="https://github.com/Mecha-Coder/42-ft-linear-regression/blob/main/demo/Result.gif">
  <p>Training Results</p>
</div>


## **How to run**

1. Pre-requisite:
```bash 
✅ System: Linux distro / WSL
✅ Python3 installed
```

2. Clone repo:
```bash
git clone https://github.com/Mecha-Coder/42-ft-linear-regression/
cd 42-ft-linear-regression
```

3. Run with make:
```bash
1. `make install` - Create virtual env and install depandencies (Will take some time ⏳)
2. `make train` - Train model using Gradient Descent with below hyperparameters
3. `make bonus` - Plot graph and perform precision evaluation
4. `make clean` - Reset to retrain with different hyperparameters
```

4. Hyperparameters used for traing
```bash
# Go to /src/header.py to change the hyperparameters
# Ensure to run `make clean` to reset the training
INIT_M = 0
INIT_C = 0
LEARN_RATE = 1
CONVERGE_LIMIT = 0.00001
ITERATION_LIMIT = 10000
```

## **Resource**
- https://www.aamoha.me/Linear-Regression
- https://bhatnagar91.medium.com/how-neural-networks-learn-using-gradient-descent-f48c2e4079a6
- https://hackmd.io/@laian/H1YEGw0qa
- https://towardsdatascience.com/linear-regression-and-gradient-descent-for-absolute-beginners-eef9574eadb0/
- https://github.com/leogaudin/ft_linear_regression
- https://www.youtube.com/watch?v=sDv4f4s2SB8
- https://www.youtube.com/watch?v=PaFPbb66DxQ
- https://www.youtube.com/watch?v=w2FKXOa0HGA
