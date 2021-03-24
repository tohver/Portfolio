with image ![Alt Text](https://docs.google.com/uc?export=download&id=1DTeaXD8tA8RjkpVrB2mr9csSBOY4LQiW)

It's very easy to make some words **bold** and other words *italic* with Markdown. You can even [link to Google!](http://google.com)

A simple neural network that translates from English to German.
Bulding flexible model architectures, freezing layers, data processing pipeline and sequence modelling.

- Using the functional API
- Building of custom layers (o specjalnym przeznaczeniu)
Learn embedding for the <end> token added at the end of the sentnece (before padding zeros)


The dataset for the project comes from 
a language dataset from http://www.manythings.org/anki/ to build a neural translation model. This dataset consists of over 200,000 pairs of sentences in English and German. 
Celem projektu nie jest stworzenie modelu lepszego niż deepl.com lub google.translator, lecz zademonstrowanie możliwości customizing of the ....?.
Dlatego to make the training quicker użyto tylko części dataset (30 000?) i bardzo prostą architekturę. Również ilość epoch jest bardzo niewielka (15?).
 In order to make the training quicker, we will restrict to our dataset to 20,000 pairs. 

Making use of a pre-trained English word embedding module

The dataset used in this project:
https://drive.google.com/open?id=1KczOciG7sYY7SB9UlBeRP1T9659b121Q


Poniżej przedstawiam schemat of the custom encoder decoder model architecture.
(obrazek 1)


The custom model consists of an encoder RNN and a decoder RNN. The encoder takes words of an English sentence as input, and uses a pre-trained word embedding to embed the words into a 128-dimensional space. To indicate the end of the input sentence, a special end token (in the same 128-dimensional space) is passed in as an input. This token is a TensorFlow Variable that is learned in the training phase (unlike the pre-trained word embedding, which is frozen).

The decoder RNN takes the internal state of the encoder network as its initial state. A start token is passed in as the first input, which is embedded using a learned German word embedding. The decoder RNN then makes a prediction for the next German word, which during inference is then passed in as the following input, and this process is repeated until the special <end> token is emitted from the decoder.

The workflow:
1. Text preprocessing and data preparation
The preprocessing includes m.innymi tokenizing of the target language and using of the pre-trained english word embedding module from TensorFlow Hub for the source language.

2. Creating the custom layer (i.e. to add the <end> token embedding to encoder model)

3. Building the encoder network (using functional API)
4. Building the decoder network (using Subclassing)
5. Custom training loop




The project is based on the Capstone Project in Customizing ...... offered by Imperial College London.



