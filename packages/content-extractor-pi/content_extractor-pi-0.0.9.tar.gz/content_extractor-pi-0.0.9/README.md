**content-extractor-pi** is a Python module which aims
to extract a certain piece of content defined by the user in a set of documents. 
This piece of content can be a paragraph that deals with a certain topic, 
headers, page numbers et cetera. **content-extractor-pi** does need some examples of the desired 
content, supplied by a domain expert, but our focus on few shot learning means ~10 
examples is usually enough out a corpus that may contain 1000s of documents. 

Installation
------------

The easiest way to install content-extractor-pi is using pip:

    pip install content-extractor-pi

Documentation
------------
The main object of content-extractor-pi is ContentExtractor and its only attribute that it expects 
is a pre-trained word embedding model. In the example I'm using the pre-trained
google news word-2-vec model available [here](https://drive.google.com/file/d/0B7XkCwpI5KDYNlNUTTlSS21pQmM/edit?usp=sharing).

### ContentExtractor.train_model method  

The **train_model** method extracts and scales features for the provided text examples contained
in train_df, creates synthetic samples of the target class, and trains
the model at the core of content_extractor.

#### Parameters

- **train_df**: pandas DataFrame containing the text examples in one column and the corresponding 
  labels in the other one
- **train_additional_features, default=None**: pandas DataFrame containing additional features 
  describing the text examples contained in train_df
- **y_name, default="label"**: column name of train_df where the labels are stored
- **text_name, default="text"**: column name of train_df where the text examples are stored
- **use_pca, default=False**: apply Principal component analysis to the scaled extracted features,
  more info can be find [here](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.PCA.html).
- **gamma, default=1**: Kernel coefficient for [sklearn.svm.SVC](https://scikit-learn.org/stable/modules/generated/sklearn.svm.SVC.html)
- **C, default=0.1**: Regularization parameter for [sklearn.svm.SVC](https://scikit-learn.org/stable/modules/generated/sklearn.svm.SVC.html)

### ContentExtractor.extract_content method  

The **extract_content** method extracts and scales features for the provided text examples
contained in target_df and returns the ones labeled as 1 by the model. 

#### Parameters
- **target_df**: pandas DataFrame containing all the text examples that we have at disposal
- **target_additional_features, default=None**: pandas DataFrame containing additional features 
  describing the text examples contained in target_df
- **text_name, default="text"**: column name of target_df where the text examples are stored

Example
------------
In the following example we have a full implementation that leads to extracting the desired 
content from a set of more than 62000 paragraphs originated from the World Bank Loan Agreements
Corpus, using just 11 examples manually labeled as 1. We aim to extract the *objective paragraph*
that is a short segment describing how the the loan it's going to be spent, below you can find an 
example.

<p align="center"><img src="https://github.com/paoloitaliani/content-extractor-pi/raw/master/images/image1.png" width=600></p>

The desired paragraphs are stored in the **target_examples** list.
```python
from content_extractor import contextractor as cte
from gensim.models import KeyedVectors
import pandas as pd

W2V_MODEL = KeyedVectors.load_word2vec_format('/your/path/to/GoogleNews-vectors-negative300.bin.gz',
                                              binary=True)
train_df = pd.read_csv("data/train_df.csv")
target_df = pd.read_csv("data/target_df.csv")

cont_ext = cte.ContentExtractor(W2V_MODEL)
cont_ext.train_model(train_df)
target_examples = cont_ext.extract_content(target_df)
```