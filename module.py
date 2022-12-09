# module for TCR wop/wp ANN model

# import load_model and pkgs

from tensorflow.keras.models import load_model
import joblib
import pandas as pd

# Class and function for TCR wop/wp ANN model

class tcr_prediction:
    def __init__(self,input_data):
        self.data = pd.DataFrame([input_data])
        self.model_wop = load_model('tcr-wop.h5')
        self.scaler = joblib.load('scaler.pkl')
        self.input_data_scaled = self.scaler.transform(self.data)
        self.line='-'*70
    def help(self): 
        help = ''' This is ANN model trained to predict a 'Interfacial Temperature Difference - d(Ti) [C]' and a 'Total Temperature Difference - d(T) [C]' due to the Thermal Contact Resistence (TCR) accros different metalic composite pairs.
        
        # for prediction
        >>> prediction = tcr_prediction(data)
        
        # for help
        >>> prediction.help()
        
        # for prediction at without pressurised condition (wop)
        >>> prediction.wop()
        
        # for prediction at pressurised condition (wp)
        >>> prediction.wp()
        '''
        print(self.line)
        print(help)
        print(self.line)
        
    def wop(self):    
        prediction_wop = self.model_wop.predict(self. input_data_scaled)
        prediction_df = pd.DataFrame(prediction_wop)
        result = pd.concat([self.data, prediction_df], axis=1, ignore_index=True)
        result.columns = ['TCR-Pairs', 'Pressure', 'T1[C]', 'T1i[C]','Prediction-d(Ti)', 'Prediction-d(T)']
        
        print('Prediction Results:')
        print(self.line)
        print(result)
        print(self.line)