This repo contains a simple python script to convert Spraakbanken swedish
corpus xml data to the OpenNLP training data format. 

It looks for all POS tags which are Proper Nouns and puts <START> xxx <END> 
around it if matching. 
