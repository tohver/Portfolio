<h1>
	Neural Machine Translation Model (without Attention)
</h1>

The purpose of this simple neural network is to demonstrate the potential of tensorflow to customize your model, by using Functional API, building your own layers, subclassing etc.
It's not the intention to beat the competitors like DeepL or Google Translator.
Wherefore, to make the training quicker, the following restriction have been made:
* The number of pairs has been reduced to 30.000
* the networks (encoder and decoder) have a minimum number of hidden layers
* the model has been trained for 10 epochs.



The language dataset is from http://www.manythings.org/anki/.   
The original dataset consists of over 200,000 pairs of sentences in English and German. 

The following schematic ilustrated the custom translation model architecture built in this project.

![Alt Text](https://docs.google.com/uc?export=download&id=1XsS1VlXoaEo-RbYNilJ9jcscNZvsSPmd)

The custom model consists of an encoder RNN and a decoder RNN. 
The encoder takes words of an English sentence as input, and uses a pre-trained word embedding to embed the words into a 128-dimensional space. To indicate the end of the input sentence, a special end token (in the same 128-dimensional space) is passed in as an input. This token is a TensorFlow Variable that is learned in the training phase (unlike the pre-trained word embedding, which is frozen).

The decoder RNN takes the internal state of the encoder network as its initial state. A start token is passed in as the first input, which is embedded using a learned German word embedding. The decoder RNN then makes a prediction for the next German word, which during inference is then passed in as the following input, and this process is repeated until the special <end> token is emitted from the decoder.

The project is based on the Capstone Project in the course [Customising your models with TensorFlow 2](https://www.coursera.org/learn/customising-models-tensorflow2/home/welcome) offered by Imperial College London on Coursera.



