# When running this 'llm embed -c 'My email is 23f2001697@ds.study.iitm.ac.in' -m 3-small' this shows insufficient_quota but I have prompt the model just 2-3 times
_Slug: _

---
**Post ID:** 625798  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/when-running-this-llm-embed-c-my-email-is-23f2001697-ds-study-iitm-ac-in-m-3-small-this-shows-insufficient-quota-but-i-have-prompt-the-model-just-2-3-times/174414/1  

Traceback (most recent call last):


File “/home/jai_tyagi/.local/bin/llm”, line 8, in 


sys.exit(cli())


^^^^^


File “/home/jai_tyagi/.local/share/pipx/venvs/llm/lib/python3.12/site-packages/click/core.py”, line 1442, in call


return self.main(*args, **kwargs)


^^^^^^^^^^^^^^^^^^^^^^^^^^


File “/home/jai_tyagi/.local/share/pipx/venvs/llm/lib/python3.12/site-packages/click/core.py”, line 1363, in main


rv = self.invoke(ctx)


^^^^^^^^^^^^^^^^


File “/home/jai_tyagi/.local/share/pipx/venvs/llm/lib/python3.12/site-packages/click/core.py”, line 1830, in invoke


return _process_result(sub_ctx.command.invoke(sub_ctx))


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


File “/home/jai_tyagi/.local/share/pipx/venvs/llm/lib/python3.12/site-packages/click/core.py”, line 1226, in invoke


return ctx.invoke(self.callback, **ctx.params)


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


File “/home/jai_tyagi/.local/share/pipx/venvs/llm/lib/python3.12/site-packages/click/core.py”, line 794, in invoke


return callback(*args, **kwargs)


^^^^^^^^^^^^^^^^^^^^^^^^^


File “/home/jai_tyagi/.local/share/pipx/venvs/llm/lib/python3.12/site-packages/llm/cli.py”, line 2513, in embed


embedding = model_obj.embed(content)


^^^^^^^^^^^^^^^^^^^^^^^^


File “/home/jai_tyagi/.local/share/pipx/venvs/llm/lib/python3.12/site-packages/llm/models.py”, line 961, in embed


return next(iter(self.embed_batch([item])))


^^^^^^^^^^^^^^^^^^^^^^^^


File “/home/jai_tyagi/.local/share/pipx/venvs/llm/lib/python3.12/site-packages/llm/default_plugins/openai_models.py”, line 240, in embed_batch


results = client.embeddings.create(**kwargs).data


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


File “/home/jai_tyagi/.local/share/pipx/venvs/llm/lib/python3.12/site-packages/openai/resources/embeddings.py”, line 128, in create


return self._post(


^^^^^^^^^^^


File “/home/jai_tyagi/.local/share/pipx/venvs/llm/lib/python3.12/site-packages/openai/_base_client.py”, line 1239, in post


return cast(ResponseT, self.request(cast_to, opts, stream=stream, stream_cls=stream_cls))


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


File “/home/jai_tyagi/.local/share/pipx/venvs/llm/lib/python3.12/site-packages/openai/_base_client.py”, line 1034, in request


raise self._make_status_error_from_response(err.response) from None


openai.RateLimitError: Error code: 429 - {‘error’: {‘message’: ‘You exceeded your current quota, please check your plan and billing details. For more information on this error, read the docs: [https://platform.openai.com/docs/guides/error-codes/api-errors.](https://platform.openai.com/docs/guides/error-codes/api-errors.)’, ‘type’: ‘insufficient_quota’, ‘param’: None, ‘code’: ‘insufficient_quota’}}

---
**Post ID:** 625810  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/when-running-this-llm-embed-c-my-email-is-23f2001697-ds-study-iitm-ac-in-m-3-small-this-shows-insufficient-quota-but-i-have-prompt-the-model-just-2-3-times/174414/2  

Did you follow aipipe documentation?


Here is link: [GitHub - sanand0/aipipe: Gives anyone access to an OpenAI/OpenRouter API key free at 10 cents/week. Self-hostable. Useful as a backend if you're building pure front-end LLM apps](https://github.com/sanand0/aipipe)

---
**Post ID:** 627900  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/when-running-this-llm-embed-c-my-email-is-23f2001697-ds-study-iitm-ac-in-m-3-small-this-shows-insufficient-quota-but-i-have-prompt-the-model-just-2-3-times/174414/3  

a.  First go to ubantu/home,  delete  .venv,  llm-env folder if exists in file explorer.


b.   Restart ubantu terminal


Commands step by step



sudo apt install python3-venv python-full
python3 -m venv ~/llm-env
source ~/llm-env/bin/activate
pip install --upgrade pip
pip install llm openai
llm keys set openai
Enter Key:  ( you have to go on  [AI Pipe | Login](http://aipipe.org/login) and copy and paste Ai pipe Token here)
export OPENAI _API_KEY=(your Token from [platform.openai.com/api-keys](http://platform.openai.com/api-keys))
export OPENAI_BASE_URL=[https://aipipe.org/openai/V1](https://aipipe.org/openai/V1)

Follow above steps  strictly and then test


llm “what is 2 + 2?”


It will be definitely helpful.

