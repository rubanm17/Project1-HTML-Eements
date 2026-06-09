import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error, r2_score

bl_tth_x, bl_tth_y = datasets.load_diabetes(return_X_y=True)

bl_tth_x = bl_tth_x[:,np.newaxis,2]

bl_tth_x_train = bl_tth_x[:-20]
bl_tth_x_test = bl_tth_x[-20:]

bl_tth_y_train = bl_tth_y[:-20]
bl_tth_y_test = bl_tth_y[-20:]

regr = linear_model.LinearRegression()

regr.fit(bl_tth_x_train, bl_tth_y_train)

bl_tth_y_pred = regr.predict(bl_tth_x_test)

print('Coefficients: \n', regr.coef_)
print('Mean squared error: %.2f' % mean_squared_error(bl_tth_y_test, bl_tth_y_pred))
print('Coefficient of determination: %.2f' % r2_score(bl_tth_y_test, bl_tth_y_pred))

plt.scatter(bl_tth_x_test, bl_tth_y_test, color='black')
plt.plot(bl_tth_x_test, bl_tth_y_pred, color='blue', linewidth=3)

plt.xticks(())
plt.yticks(())

plt.show()