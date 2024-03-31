# Emoji prediction using LSTM
- This is a simple project for predicting emojis based on input phrases. Currently 10 types of emojis can be predicted based on the input : 🤔, ❤️, 😃, 😂, 😭, 🔥, 🙏, 👍, 😍, 😠,

- The dataset was generated using various methods such as manual input, phrases from the internet and some with using ChatGpt

- The aim of the project was to gain a deeper understanding of Recurrent Neural Networks(RNNs) and in particular Long short-term memory (LSTM) - which is the method used for this project. This includes determining which architecture of the neural network performs the best at prediction - mainly the number of layers used, units used per layer, and epochs used to train the model.
  
- Details of how well the model performs with different parameters can be found in:
  1. In a textual form: models/training set v.3.0/metrics
  2. In the form of confusion matrices: models/training set v.3.0/confusion_matrices
  3. As charts showing precision/accuracy: models/training set v.3.0/class_accuracy
 
- The models trained make use of pretrained word embeddings to capture context from input data and in particular the : crawl-300d-2M-subword.zip: 2 million word vectors trained with subword information on Common Crawl (600B tokens). This can be found here: https://fasttext.cc/docs/en/english-vectors.html. 

## How to use a model to get predictions:
1. Clone this repositiory.
2. Make sure your device has python 3.10 or above installed. You can download miniconda and create a python environment to do so as well.
3. Open the model_stats.ipynb notebook and make sure all the libraries/packages mentioned above are installed on your device.
4. Then copy a name of a model from here **(do not add the extension like .md or .png or .json and so on or the root folder)**. This a image for reference to see which models you can get predictions from:
   </br>
   </br>
   ![image](https://github.com/curryfizz/Emoji-Prediction/assets/52543544/3da62071-d9ef-43e1-aeea-af34fb59ee3f)
5. Paste the copied name into this cell (the second cell) of the model_stats.ipynb notebook.
   </br>
   </br>
   ![image](https://github.com/curryfizz/Emoji-Prediction/assets/52543544/4752482b-a01a-4866-83ac-72cafe6bd03d)
6. To add phrases/text of your own to get predictions add your that in this cell of the mode_stats.ipynb notebook - that is to "test" array.
   </br>
   </br>
   ![image](https://github.com/curryfizz/Emoji-Prediction/assets/52543544/9a621fe1-9fd6-4b9f-b13d-beb56629f0c0)
7. Then use the "Run all" option for jupyter notebook and see the results at the end of the model_stats.ipynb notebook. This version has some present already so if you cloned the repo and open the model_stats.ipynb file you will be able to see the results of one of the models used here.
   
</br>

## For the next section, please note that training a model on a local device using it's own resources has limitations depending on the specifications of the device. So proceed at your own discretion.

</br>

## How to run the notebook and train a model
1. Clone this repository.
2. Make sure your device has python 3.10 or above installed. You can download miniconda and create a python environment to do so as well.
3. Install the packages listed in the first cell of the lstm_predictor.ipynb notebook. 
4. Download the crawl-300d-2M-subword.zip: 2 million word vectors trained with subword information on Common Crawl (600B tokens) zip from: https://fasttext.cc/docs/en/english-vectors.html.
5. Create a subfolder in the data folder called "fast_text" and then another subfolder in the newly created "fast_text" folder called "crawl_dataset".
6. Extract the contents of the downloaded zipped folder into the "crawl_dataset" folder. Since this part seems a little messy, look at the project/folder structure below for reference (this is using Visual Studio Code):
   </br>
   </br>
 ![image](https://github.com/curryfizz/Emoji-Prediction/assets/52543544/36e97842-7559-4f7f-9443-8e03b28c6a87)

7. You can then modify the parameters you are using to train a model by making changes to this cell in the lsmt_predictor.ipynb notebook:
   </br>
   </br>
 ![image](https://github.com/curryfizz/Emoji-Prediction/assets/52543544/334a794b-1d92-45cd-9b94-cccef47325af)

8. Just use the "Run all" option in jupyter notebook and that's it!



