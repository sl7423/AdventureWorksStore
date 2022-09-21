import random
import pickle

filename = 'accounts/MLModels/finalized_model.sav'
algo = pickle.load(open(filename, 'rb'))

class GenerateRecommendations:
    def __init__(self, metadata, model=algo):
        self.metadata = metadata.copy()
        self.model = model
        
        self.columns = [f'{product},' for product in self.metadata.columns]
                  
        
    def get_product_id(self):
        
        print(self.columns)
        while True:
            product_name = input('Please enter the Category of Product')
            if product_name not in self.columns:
                print("Not a Product")
                continue
            else:
                return self.metadata[self.metadata['product_name'] == product_name]['productid']
                 
    def get_product_info(self, product_id):
        columns = [f'{column}' for column in self.metadata.columns if column not in ['productid']]
        product_info = self.metadata.loc[self.metadata['productid'] == product_id][columns]
        return product_info.to_dict(orient='records')
    
    def predict_purchase(self, user_id, product_title):
        review_prediction = self.model.predict(uid=user_id, iid=self.metadata.loc[self.metadata['product_name'] == product_title]['productid'].values[0])
        return review_prediction.est
    
    def generate_recommendation(self, user_id, thresh=3, recommend=6):
        
        product_titles = list(self.metadata['product_name'])
        random.shuffle(product_titles)
        
        recommendation = []
        recommendation_id = []
        
        while thresh > 0 or len(recommendation) < recommend:
            for product_title in product_titles:
                rating = self.predict_purchase(user_id, product_title)
                if rating > thresh:
                    product_id = self.metadata.loc[self.metadata['product_name'] == product_title]['productid'].values[0]
                    recommendation.append(self.get_product_info(product_id))
                    recommendation_id.append(product_id)
                if len(recommendation) == recommend:
                    break
            if len(recommendation) == recommend:
                break
            thresh -= 1
        
        return recommendation_id
    