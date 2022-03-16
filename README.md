# NLP Project Generate Content

The first step is to scrape all the blog posts of Efinancial careers (https://www.efinancialcareers.com/news) and then create an NLP generator that with a title as input can generate an entire blog post.

I used gpt2 huggingface (pretrained) as a model to generate the text. The idea is to use the already trained model, fine-tune it to the data scraped from Efinancial careers website, and then, based on what the model observes, generate what should follow in any given blog post.
