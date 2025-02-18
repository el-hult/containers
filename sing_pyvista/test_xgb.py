print(f"Running test file {__file__}")
import xgboost as xgb
X = [[1],[0]]
y = [1,0]

model = xgb.XGBRegressor(tree_method="hist", device="cpu")
model.fit(X,y)
model.predict(X)

try:
    Xy = xgb.QuantileDMatrix(X, y)
    model = xgb.train(dtrain=Xy,params=dict(device='cuda',tree_method='hist'))
    model.predict(xgb.DMatrix(X))
except Exception as e:
    print('Not in cuda environment?')
    raise e