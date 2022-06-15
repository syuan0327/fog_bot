import numpy as np
import pandas as pd
from to_sequences_1 import to_sequences
from sklearn.preprocessing import MinMaxScaler
from keras.models import load_model
def modell():
    model = load_model('fog_model.h5')
    lookback = 72

    predictdata = pd.read_csv('./testdata.csv')
    predictdata.drop(predictdata.index[predictdata[(predictdata.values == 'X') | \
        (predictdata.values == 'V')].index], inplace=True)
    predictdata = predictdata.drop(['time','Label'],axis=1)
    predictdata = predictdata.astype("float64")
    predictdata.info()

    scalerPredict = MinMaxScaler(feature_range=(0, 1))  # Also try QuantileTransformer
    scaleredPredict = scalerPredict.fit_transform(predictdata)

    scalerYPredict = MinMaxScaler(feature_range=(0, 1))
    YPredict = scalerYPredict.fit_transform(predictdata['VIZ'].values.reshape(-1, 1))
    scaleredPredict.shape, YPredict.shape

    predictX, predictY = to_sequences(predictdata.values, lookback)
    
    predictX.shape, predictY.shape

    predictX = np.reshape(predictX, (predictX.shape[0], 1, -1))

    threeDayPredict = model.predict(predictX)
    threeDayPredict.shape
    threeDayPredictOutput = scalerYPredict.inverse_transform(threeDayPredict)
    print(threeDayPredictOutput)
    output = pd.DataFrame(threeDayPredictOutput)
    output.to_csv('ans.csv', index=False)

modell()