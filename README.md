# TextThema - Content Classifier and Recommender System

A Text Content Themes Classifier and smart Recommender System. 
Here is documentation of the project process from data collection, model training, and deployment. <br/>
The model can classify 103 different types of themes despite from input. Despite the input content is Creative, poetry, Literary, Descriptive, synopsis, quotes, songs or Dialogues:<br/>The keys of `deployment_hf\tag_types_encoded.json` shows the theme types. 

The goal of this project was multimodal. To cover diverse range of objectives.
* detect nuances like humor and simile/metaphor, 
* detect Author Intents and content themes, 
* possibly detect plus recomment related books, famous people/authors, fictional character, franchise from input content.
* automate/recommend hashtags.



 ## Data Collection

dynamic website time based login prompt were handled.

Data was collected from a Goodreads Quotes Listing: https://https://www.goodreads.com/quotes <br/>The data collection process was as follows: 

The massive NLP data were scraped with `scraper/nlp_dataset_scraper.py` and the urls are stored along with book title in `scraper/quote-nlp-dataset-scraped.csv`. Employed a effecient tracking mangement system for scrap of massive NLP data.

In total, I scraped ~43,000 different content style data e.g. quote, poems, synopsis, dialogue, story and corresponding data's themes, tags. Finally, ~38,500 dataset reamined after cleaning.



## Data Preprocessing
Initially there were lots of themes and tags in the dataset. After some analysis, I found out many of them are rare themes and tags (probably custom tags by users). So, I removed those tags and then I kept *103* themes and tags for intial test. After that, I removed any noisy data due to scraping and dropped any duplicate occurence resulting in *~38500* samples.


## Model Training 
Finetuned a `roberta-base` (RoBERTa) model which is a transformers model from HuggingFace Transformers using Fastai and Blurr. The model training notebook can be viewed [here](https://github.com/tanvir-ishraq/TextThema-Multi-Classifier/blob/main/notebooks/quote-multi-classifier.ipynb)

## Benchmark

## Model Compression and ONNX Inference
The trained model has a memory of 900+MB. I compressed this model using ONNX quantization and brought it to 125MB. 

## Model Deployment

The compressed model is deployed to HuggingFace Spaces Gradio App. The implementation can be found in `deployment` folder or [here](https://huggingface.co/spaces/tanvir-ishraq/quote-text-style-classifierr) 

<!-- <img src = "deployment/gradio_app.PNG" width="800" height="400"> -->
 <img src = "github_img/hf_gradio_app_TextThema.png" width="830" >

## Web Deployment
Deployed a Flask App built to take descprition and show the genres as output. Check `flask ` branch. The website is live [here](https://textthema-multi-classifier.onrender.com/) 

 <img src = "github_img/flask_app_home_input.png" width="830" >
<img src = "github_img/flask_app_results_output.png" width="830" >
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
