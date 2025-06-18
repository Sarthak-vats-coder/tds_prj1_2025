# LLM CLI Tool Error– Model Authentication Issue with Models other OpenAI models
_Slug: _

---
**Post ID:** 632835  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/llm-cli-tool-error-model-authentication-issue-with-models-other-openai-models/176603/1  

I Kindly need Help with LLM CLI Tool –  Model Authentication Issue with Models other OpenAI models.


I’ve been trying to go a bit deeper into Module 1 after completing GA1, and I’ve encountered some issues while experimenting with the `llm` CLI tool and different models.


Specifically, I tried running the following command to test the Gemini model, as shown on the Module 3 introduction page:


`llm 'What is 2 + 2?' -m openrouter/google/gemini-2.0-flash-lite-001`
But I received the following error:


`Error: Error code: 401 - {'error': {'message': 'No auth credentials found', 'code': 401}}`
Initially, I had set my OpenAI key from AIPipe , but I got a “model not found” error. So I checked the available models using:


`llm model list`
At that point, the Gemini model wasn’t listed.


I then installed the `llm-openrouter` plugin, and after that, the Gemini model appeared in the list. However, I’m now facing the above authentication error.


To test if the issue was only with Gemini and other models other than OpenAI models , I created a personal API key from OpenRouter and tried running a free model:(i tried free models on both keys from AIpipe and my personal account since it doesn’t need any credits to be purchased)


`llm 'What is 2 + 2?' -m openrouter/qwen/qwen3-8b:free`
This worked correctly with my OpenRouter API key, which confirms that the plugin is working fine.


I’m confused about how to properly authenticate for other via AIPipe for OpenRouter using the `llm` CLI. I’ve been trying different approaches for the last two days but haven’t been able to resolve this.


Certainly! Here’s a grammatically correct and polished version of the message you want to add at the end:



I also tried setting the API keys individually for OpenAI, OpenRouter(this is basically configured while installing the plugin `llm-openrouter`), and even my personal keys, using the key management options mentioned in the `llm` documentation. Additionally, I saw that our course page suggest changing the base URL like this:


`export OPENAI_BASE_URL=https://aipipe.org/openrouter/v1
llm 'What is 2 + 2?' -m openrouter/google/gemini-2.0-flash-lite-001`
However, even this approach didn’t work for me.


Could you kindly guide me on how to resolve this issue?


Thank you for your time and help.


Sincerely,


Meikanda Sivam

