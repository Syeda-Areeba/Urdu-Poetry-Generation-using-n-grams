# Urdu Poetry Generation Using N-grams

## Overview

This project involves scraping Urdu poems from the Rekhta website and generating new poetry using N-grams. The process includes web scraping with Scrapy, data preprocessing, and poetry generation with N-gram models.

## 1. Web Scraping

### Tools
- **Scrapy**: A Python framework for web scraping.

### Process
- **Spider**: `I210307urdupoemsspider` crawls the Rekhta website to collect Urdu poems.
- **Data Extraction**: Extracts poet names, poem titles, and lines from each poem.
- **Output**: Data is saved in JSON format and later converted to CSV.

### Command
```bash
scrapy crawl I210307urdupoemsspider -o poems_data.json
```

## 2. Corpus Statistics

- **Number of Poems**: 484
- **Number of Poets**: 25
- **Total Unique Words**: 6116

## 3. Poetry Generation

### Models
- **Forward Bigrams**: Predict the next word based on the preceding word.
- **Backward Bigrams**: Predict the previous word based on the succeeding word.
- **Trigrams**: Predict the next word using the context of two preceding words.
- **Bidirectional Bigrams**: Combine forward and backward contexts.

### Evaluation
- **Perplexity**: Measures model performance. Lower values indicate better predictive accuracy.

### Results
- **Trigrams** generally perform best, followed by Bidirectional Bigrams and Bigrams.

## 4. Challenges and Solutions

### Challenges
- **Rhyme Scheme**: Difficulty in maintaining consistent rhyme due to the lack of Urdu rhyming word libraries.
- **Poetry Consistency**: Ensuring coherent word selection and rhyme scheme.

### Solutions
- **Rhyme Detection**: Implemented a function to find rhyming words by matching last characters.
- **Probabilistic Selection**: Used probabilistic methods with controlled randomness for word selection.

## Conclusion

The project successfully demonstrates Urdu poetry generation using N-grams, addressing key challenges in rhyme consistency and model evaluation. Further improvements could enhance the quality and coherence of generated poetry.
