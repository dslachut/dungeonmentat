from openai import OpenAI

__client = OpenAI(base_url="http://localhost:1234/v1", api_key="lm-studio")

__chat_model = "deepseek-r1-distill-qwen-7b-uncensored-reasoner-i1"

__embedding_model = "text-embedding-nomic-embed-text-v1.5"


def get_embedding(text: str, model:str=__embedding_model) -> list[float]:
    """Get embedding vector for text

    Args:
        text (str): text to vectorize
        model (str): name of model to use. Defaults to __embedding_model.

    Returns:
        list[float]: the embedding vector
    """
    text = text.replace("\n", " ")
    return __client.embeddings.create(input=[text], model=model).data[0].embedding


def do_completion(system_prompt: str, user_prompt: str, temperature: float = 0.7, model: str = __chat_model, ) -> str:
    """Do a chat completion with the LLM

    Args:
        system_prompt (str): Instructions for the LLM about how to answer the user prompt.
        user_prompt (str): Prompt for the LLM to answer.
        temperature (float, optional): chat model temperature. Defaults to 0.7.
        model (str, optional): chat model to call. Defaults to __model.

    Returns:
        str: _description_
    """
    completion = __client.chat.completions.create(
        model=model,
        messages=[{"role": "system", "content": system_prompt}, {"role": "user", "content": user_prompt}],
        temperature=temperature,
    )
    return completion.choices[0].message.content.split("</think>\n\n")[-1]
