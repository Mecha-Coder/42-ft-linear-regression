![Title](/blob/main/demo/Title.png)

### **Overview**

Train a Linear Regression Model with Gradient Descent using the provided dataset. Then, use that model to preduct the car price based on the mileage. 

---

### **Key Learnings**
- Trained a linear regression model on a given dataset.
- Applied gradient descent to optimize the model and achieve the best fit.
- Normalized and denormalized data.
- Evaluated model performance using Mean Squared Error (MSE) and the coefficient of determination (R²).

---

### **Read More**

👉 [**Project requirement**](/blob/main/demo/Linear_Regression.pdf)

👉 [**Steps to complete the project**](https://hackmd.io/@Mecha-Coder/BJ8itE4Wbx#3-Complete-Assignment)

--- 

### Demo

![demo](/blob/main/demo/Result.gif)

---

### **How to run**

Pre-requisite: 
- System: Linux distro / WSL
- Python3 installed

Clone repo:
```bash
git clone https://github.com/Mecha-Coder/42-ft-linear-regression/
cd 42-ft-linear-regression
```

Run with make:
1. `make install` - Create virtual environment and install depandencies (Will take time ⏳)
2. `make train` - Train the model using Gradient Descent with below hyperparameters
```bash
INIT_M = 0
INIT_C = 0
LEARN_RATE = 1
CONVERGE_LIMIT = 0.00001
ITERATION_LIMIT = 10000
```
3. `make bonus` - Plot graph and perform precision evaluation
4. `make clean` - To reset and train with different hyperparameters
---

### **Resource**
- https://www.aamoha.me/Linear-Regression
- https://bhatnagar91.medium.com/how-neural-networks-learn-using-gradient-descent-f48c2e4079a6
- https://hackmd.io/@laian/H1YEGw0qa
- https://towardsdatascience.com/linear-regression-and-gradient-descent-for-absolute-beginners-eef9574eadb0/
- https://github.com/leogaudin/ft_linear_regression
- https://www.youtube.com/watch?v=sDv4f4s2SB8
- https://www.youtube.com/watch?v=PaFPbb66DxQ
- https://www.youtube.com/watch?v=w2FKXOa0HGA
