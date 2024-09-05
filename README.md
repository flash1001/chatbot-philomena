# chatbot-philomena

A Telegram bot using OpenAI API and Fine-Tuning 

## Requirements?

This code requires an already built Fine-Tuning model using OpenAI. Thankfully, OpenAI gives us documentation on the matter
by just following the next link [https://platform.openai.com/docs/guides/fine-tuning](https://platform.openai.com/docs/guides/fine-tuning).

To link the model with the Telegram chatbot I highly recommend [BotFather](https://docs.radist.online/docs/our-products/radist-web/connections/telegram-bot/instructions-for-creating-and-configuring-a-bot-in-botfather), as it is an easy Bot Creator for telegram. Just follow the instructions of the previous link
and you'll be ready to go :).

## How to use?

The current code has three important files that you'll use during your fine tuning process and bot interaction:

1. data_preparation.ipynb is a very intuitive guide through both the training and validation .jsonl files that you have created. After this file has access to
those files, it will validate the format looking for possible mistakes for you to correct. It will also provide a token count, distribution of tokens per role
and an approximate value of the tokens you will be charged with. For prices by model you can check out the next link [https://openai.com/api/pricing/](https://openai.com/api/pricing/).

2. fine_tuned_model_analysis.ipynb will help you evaluate how well your Fine-Tuned model was trained, remember to train it and to validate it with much valuable data as possible.
This file will give you a train_loss and train_accuracy as primary data, and are pretty self explanatory on what they do. In addition, you can play with some parameters of
the model you created as if it was the OpenAI playground. You'll see an example message on this section to help you use it, although i recommend to use the real thing
[OpenAI Playground](https://platform.openai.com/playground/chat?models=gpt-4o). If you are not satisfied with how your model responds don't blame yourself, as collecting valuable data
is a hard task, and it happened to me quite a few times ;).

3. philo_bot.py is the file which connects your Model to the Telegram Bot in order to give you a response in chat. While it is running, you can chat with your Model, just make
sure to use the necessary state variables, and also to change the context of the model to your specific context (the one left in the code was mine 😊​).

## Additional notes

This project was created under the last API documentation available to the current date (September 5, 2024), be sure to make any changes if necessary for your project.

I think you are good to go now, good luck 🦉​🦉​🦉​