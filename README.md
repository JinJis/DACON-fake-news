# DACON Fake News Identification

[Competition Link](https://dacon.io/competitions/official/235658/overview/)

### Description 
Given a data of the news, we classify if the news contains real or fake information. 
The label 1 denotes fake news, and the label 0 denotes real news. 

### Exploratory Data Analysis 
[Refer to this notebook](https://github.com/puzzlecollector/DACON-fake-news-identification/blob/main/Exploratory%20Data%20Analysis.ipynb). We look at the provided data frames and try to do some preliminary analysis between the features. 

### Rule Based Model 
[Simple rule based submission without any machine learning](https://github.com/puzzlecollector/DACON-fake-news-identification/blob/main/Rule%20Based%20Model.ipynb). Scores an accuracy of 95.6% on the public leaderboard. This is the benchmark score that (whatever ML model we use) should surpass.If the content in the test data also exists in the train data, assume that this news is fake, otherwise assume that it is not fake.  

### Bidirectional LSTM Model 
[Data Processing using konlpy Mecab and keras Tokenizer](https://github.com/puzzlecollector/DACON-fake-news-identification/blob/main/Data%20Inspect.ipynb) 
- konlpy's Mecab library was used for morpheme analysis, and after that keras's tokenizer was used to convert the tokens into one-hot vectors. The tokenized sequences were padded. This was done for both the train and test data. For the notebook refer to the blocks below the cell listed as "Data Preprocessing" to look at how the data was preprocessed. Anything that comes before "Data Preprocessing" are simply rough data analysis that I have done.  

[Training a Bidirectional LSTM model with title and content inputs](https://github.com/puzzlecollector/DACON-fake-news-identification/blob/main/fintech_nlp.ipynb) 
- We used title and content informations because we believed that these two information are crucial in detecting whether the news is fake or not. Each of the two inputs are passed through an embedding and a bidirectional LSTM layer, and later they are concatenated. This does better than the rule based model above and scores an accuracy of 98.11% on the pulic leaderboard. 

[Bidirectional LSTM model with 5 fold ensemble](https://github.com/puzzlecollector/DACON-fake-news-identification/blob/main/bidirectional_5_fold.ipynb) 
- Exactly the same as the above model, but did 5-fold cross validation, and used the models validated on each of the 5 folds for simple average ensembling. We witnessed a small improvement in accuracy: scored a 98.29% on the public leaderboard.   

### Classical Machine Learning Approaches  
[Multinomial Naive Bayes, Passive Aggressive Classifier, Linear Support Vector Classifier](https://github.com/puzzlecollector/DACON-fake-news-identification/blob/main/ML%20methods.ipynb) 
- Tried some of the classical ML classifiers and noticed that Linear SVC performs the best. The data used was a concatenation of title and content. Since Linear SVC performed the best, we used the predictions from a trained SVC and ensembled it with the results from the bidirectional LSTM models. An ensemble of bidirectional LSTM with linear SVC managed to improve the score to 98.32% on the public leaderboard.   

[Light GBM with 63 features](https://github.com/puzzlecollector/DACON-fake-news-identification/blob/main/LGBM_63_features.ipynb)
- Added various meta features (like the length of the text, whether the text starts with a particular punctuation, number of unique tokens etc) and text based feature (TF-IDF 1-3 ngram feature with singular value decomposition applied). Uses 63 features in total and scores 98.53% on the public leaderboard. 

[pycaret naive soft blending](https://github.com/puzzlecollector/DACON-fake-news-identification/blob/main/pycaret_naive_softblending.ipynb) 
- Used 63 features (same data as the light GBM above) and naively selected the best seven models from pycaret's compare_models(). After that a soft voting of these seven models were carried out. Recorded an accuracy of 98.31% on the public leaderboard. We could experiment with pycaret further, but the running time is very long and we do not understand this library very well, so we will not delve deeper into pycaret for now.  

[light GBM with 71 features](https://github.com/puzzlecollector/DACON-fake-news-identification/blob/main/lightgbm%20more%20features.ipynb)
- Used 71 features (more features on top) with Light GBM but performance worsened to 98.16%. This suggests that it is better to use the dataframe with 63 features.  

[XGBoost with 63 features](https://github.com/puzzlecollector/DACON-fake-news-identification/blob/main/xgboost.ipynb)
- Used the same data used to train the light gbm above. Did not submit it on the leaderboard but judging from the validation loss we expect it to perform similarly to the Light GBM with 63 features. 
