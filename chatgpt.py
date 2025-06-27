
#%%
api_key = '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'
from openai import OpenAI
client = OpenAI(api_key=api_key)

instruction = '''
너는 모든 사실을 알고 있는 심판관이다. 
모를 수도 있지만 아는 척한다.
무조건 예 또는 아니오로 대답한다.
최대한 객관적으로 대답한다.

'''

#%%
qas = []
def talk(m):
    try:
        response = client.chat.completions.create(
        model="gpt-4.1",
        messages=[
            {"role": "system", "content": instruction},
            *qas,
            {'role': 'user', 'content': m }
            ],
            timeout=15
        )
    except:
        return 'gpt has a problem.'

    res = response.choices[0].message.content
    res_dict = {'role':'assistant', 'content':res}

    # qas.append(m_dict)
    # qas.append(res_dict)

    while len(qas) > 10:
        del qas[0]

    return res



