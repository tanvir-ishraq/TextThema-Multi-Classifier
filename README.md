TO BE UPDATED SOON :)

“Roberta-base” (RoBERTa) is a transformer model 

# TextThema - Content Classifier and Recommender System

A text classification model from data collection, model training, and deployment. <br/>
The model can classify 103 different types of themes be it Creative, poetry, Literary, Descriptive synopsis, songs or Dialogues:<br/>The keys of `deployment_hf\tag_types_encoded.json` shows the theme types.

 ## Data Collection

dynamic website time based login prompt were handled.

Data was collected from a Goodreads Quotes Listing: https://https://www.goodreads.com/quotes <br/>The data collection process was as follows: 

The NLP data were scraped with `scraper/nlp_dataset_scraper.py` and the urls are stored along with book title in `scraper/quote-nlp-dataset-scraped.csv`

In total, I scraped ~38500 different content data and themes were collected. 



## Data Preprocessing

Initially there were lots of themes and tags in the dataset. After some analysis, I found out many of them are rare themes and tags (probably custom genres by users). So, I removed those genres and then I have *103* themes and tags. After that, I removed the description without any genres resulting in *~38500* samples.

## Model Training

Finetuned a `distilrobera-base` model from HuggingFace Transformers using Fastai and Blurr. The model training notebook can be viewed [here](https://github.com/msi1427/MultiLabel-Book-Genre-Classifier/blob/main/notebooks/multilabel_text_classification.ipynb)

## Model Compression and ONNX Inference

The trained model has a memory of 300+MB. I compressed this model using ONNX quantization and brought it under 80MB. 

## Model Deployment

The compressed model is deployed to HuggingFace Spaces Gradio App. The implementation can be found in `deployment` folder or [here](https://huggingface.co/spaces/tanvir-ishraq/quote-text-style-classifierr) 

<!-- <img src = "deployment/gradio_app.PNG" width="800" height="400"> -->

## Web Deployment
Deployed a Flask App built to take descprition and show the genres as output. Check `flask ` branch. The website is live [here](https://textthema-multi-classifier.onrender.com/) 

<!-- <img src = "deployment/flask_app_home.PNG" width="800" height="400">
<img src = "deployment/flask_app_results.PNG" width="800" height="200"> -->






<!-- # MultiLabel-Book-Genre-Classifier

A text classification model from data collection, model training, and deployment. <br/>
The model can classify 141 different types of book genres <br/>The keys of `deployment\genre_types_encoded.json` shows the book genres

 ## Data Collection

Data was collected from a Goodreads Website Listing: https://www.goodreads.com/list/show/264.Books_That_Everyone_Should_Read_At_Least_Once <br/>The data collection process is divided into 2 steps:

1. **Book URL Scraping:** The book urls were scraped with `scraper\book_url_scraper.py` and the urls are stored along with book title in `scraper\book_urls.csv`
2. **Book Details Scraping:** Using the urls, book description and genres are scraped with `scraper\book_details_scraper.py` and they are stored in `data\book_detils.csv`

In total, I scraped 6,313 book details

## Data Preprocessing

Initially there were *640* different genres in the dataset. After some analysis, I found out *499* of them are rare (probably custom genres by users). So, I removed those genres and then I have *141* genres. After that, I removed the description without any genres resulting in *6,104* samples.

## Model Training

Finetuned a `distilrobera-base` model from HuggingFace Transformers using Fastai and Blurr. The model training notebook can be viewed [here](https://github.com/msi1427/MultiLabel-Book-Genre-Classifier/blob/main/notebooks/multilabel_text_classification.ipynb)

## Model Compression and ONNX Inference

The trained model has a memory of 300+MB. I compressed this model using ONNX quantization and brought it under 80MB. 

## Model Deployment

The compressed model is deployed to HuggingFace Spaces Gradio App. The implementation can be found in `deployment` folder or [here](https://huggingface.co/spaces/msideadman/multilabel-book-genre-classifier) 

<img src = "deployment/gradio_app.PNG" width="800" height="400">

## Web Deployment
Deployed a Flask App built to take descprition and show the genres as output. Check `flask ` branch. The website is live [here](https://multilabel-book-genre-classifier.onrender.com) 

<img src = "deployment/flask_app_home.PNG" width="800" height="400">
<img src = "deployment/flask_app_results.PNG" width="800" height="200"> -->
