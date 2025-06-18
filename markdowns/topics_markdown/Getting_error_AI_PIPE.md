# Getting error AI PIPE
_Slug: _

---
**Post ID:** 625318  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/getting-error-ai-pipe/174255/1  

sir, i am not able to do this


llm “What is 2 + 2”


Error: Error code: 401 - {‘message’: ‘Bearer…


bMA is invalid: JWSInvalid: Invalid Compact JWS’}


i am getting this error [@carlton](/u/carlton)

---
**Post ID:** 625399  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/getting-error-ai-pipe/174255/2  

![That's a blurry, low-resolution image of a person wearing a dark-colored hoodie.  Their face is mostly obscured by the hood and their hand.  The background appears to be a wall with horizontal lines.
](https://dub1.discourse-cdn.com/flex013/user_avatar/discourse.onlinedegree.iitm.ac.in/22f3000982/48/78201_2.png) 22f3000982:

llm “What is 2 + 2”


Error: Error code: 401 - {‘message’: ‘Bearer…


bMA is invalid: JWSInvalid: Invalid Compact JWS’}




Did you set your API key correctly? This would show up if your API key is invalid or messed up somehow.


Also, this should probably be in the GA 1 thread

---
**Post ID:** 625452  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/getting-error-ai-pipe/174255/3  

![That's a blurry, low-resolution image of a person wearing a dark-colored hoodie.  Their face is mostly obscured by the hood and their hand.  The background appears to be a wall with horizontal lines.
](https://dub1.discourse-cdn.com/flex013/user_avatar/discourse.onlinedegree.iitm.ac.in/22f3000982/48/78201_2.png) 22f3000982:

sir, i am not able to do this


llm “What is 2 + 2”


Error: Error code: 401 - {‘message’: ‘Bearer…


bMA is invalid: JWSInvalid: Invalid Compact JWS’}




means your API request to the LLM (Large Language Model) is being rejected due to an invalid or expired token. The `401` status code stands for Unauthorized. Check if you have set your API Key correctly

---
**Post ID:** 625503  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/getting-error-ai-pipe/174255/4  

export OPENAI_BASE_URL=https://aipipe.org/openai/v1  kumar@sahili MINGW64 ~  llm embed -c ‘What is 2 + 2’ -m 3-small Traceback (most recent call last):   File “”, line 198, in _run_module_as_main   File “”, line 88, in run_code   File "C:\Users\kumar\AppData\Local\Programs\Python\Python313\Scripts\llm.exe_main.py", line 7, in      sys.exit(cli())              ~~~^^   File “C:\Users\kumar\AppData\Local\Programs\Python\Python313\Lib\site-packages\click\core.py”, line 1161, in call     return self.main(*args, **kwargs)            ~~~~~~~~~^^^^^^^^^^^^^^^^^   File “C:\Users\kumar\AppData\Local\Programs\Python\Python313\Lib\site-packages\click\core.py”, line 1082, in main     rv = self.invoke(ctx)   File “C:\Users\kumar\AppData\Local\Programs\Python\Python313\Lib\site-packages\click\core.py”, line 1697, in invoke     return _process_result(sub_ctx.command.invoke(sub_ctx))                            ~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^   File “C:\Users\kumar\AppData\Local\Programs\Python\Python313\Lib\site-packages\click\core.py”, line 1443, in invoke     return ctx.invoke(self.callback, **ctx.params)            ~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^   File “C:\Users\kumar\AppData\Local\Programs\Python\Python313\Lib\site-packages\click\core.py”, line 788, in invoke     return __callback(*args, **kwargs)   File “C:\Users\kumar\AppData\Local\Programs\Python\Python313\Lib\site-packages\llm\cli.py”, line 2513, in embed     embedding = model_obj.embed(content)   File “C:\Users\kumar\AppData\Local\Programs\Python\Python313\Lib\site-packages\llm\models.py”, line 961, in embed     return next(iter(self.embed_batch([item])))                      ~~~~~~~~~~~~~~~~^^^^^^^^   File “C:\Users\kumar\AppData\Local\Programs\Python\Python313\Lib\site-packages\llm\default_plugins\openai_models.py”, line 240, in embed_batch     results = client.embeddings.create(**kwargs).data               ~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^   File “C:\Users\kumar\AppData\Local\Programs\Python\Python313\Lib\site-packages\openai\resources\embeddings.py”, line 128, in create     return self._post(            ~~~~~~~~~~^         “/embeddings”,         ^^^^^^^^^^^^^^     …<8 lines>…         cast_to=CreateEmbeddingResponse,         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^     )     ^   File “C:\Users\kumar\AppData\Local\Programs\Python\Python313\Lib\site-packages\openai_base_client.py”, line 1242, in post     return cast(ResponseT, self.request(cast_to, opts, stream=stream, stream_cls=stream_cls))                            ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^   File “C:\Users\kumar\AppData\Local\Programs\Python\Python313\Lib\site-packages\openai_base_client.py”, line 919, in request     return self._request(            ~~~~~~~~~~~~~^         cast_to=cast_to,         ^^^^^^^^^^^^^^^^     …<3 lines>…         retries_taken=retries_taken,         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^     )     ^   File “C:\Users\kumar\AppData\Local\Programs\Python\Python313\Lib\site-packages\openai_base_client.py”, line 1023, in _request     raise self._make_status_error_from_response(err.response) from None openai.AuthenticationError: Error code: 401 - {‘message’: ‘Bearer .eyJlbWFpbCI6IjI0ZjIwMDAxNjRAZHMuc3R1ZHkuaWl0bS5hYy5pbiJ9.ctFb6WLOXZQksR-pdWDAaE8Bfah5LCIJ-c7pY-8t41c is invalid: JWSInvalid: JWS “alg” (Algorithm) Header Parameter missing or invalid’}  kumar@sahili MINGW64 ~ $ i get this error when export  i also get this error again and again how i resolve it

---
**Post ID:** 625563  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/getting-error-ai-pipe/174255/5  

It’s problem with the way you are using llm, request needs to go via proxy (aipipe).


Find documentation below [sanand0/aipipe: Gives anyone access to an OpenAI/OpenRouter API key free at 10 cents/week. Self-hostable. Useful as a backend if you’re building pure front-end LLM apps](https://github.com/sanand0/aipipe)


[@22f3000982](/u/22f3000982) [@Sahil_singh](/u/sahil_singh)


If you follow steps in above documentation carefully then you will get not face invalid token issues.

---
**Post ID:** 625577  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/getting-error-ai-pipe/174255/6  

done , thankyu everyone

---
**Post ID:** 627485  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/getting-error-ai-pipe/174255/7  

I am not able to do this . Please help me

