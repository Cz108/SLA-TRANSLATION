import os
import openai
from tools.utils import word_count


key_path = "/Users/bilibala/Study/SLA-TRANS/cre/sla-c4.json"
with open(key_path, 'r') as file:
  key = file.readline().strip()

os.environ["OPENAI_API_KEY"] = key
openai.api_key = os.getenv('OPENAI_API_KEY')

# openai.api_key = "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"

"""
    Check if 2 sentences are consistent
    Return True and False, or the others.
"""
def check_if_two_sentences_consistent(sentence1, sentence2):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=
            [
                {
                  "role": "system",
                  "content": "You will be provided with a technical sentence, and your task is to repeat it in another way as a translator and if there are brackets, quotes, slash, don't delete them."
                },
                {
                  "role": "user",
                  "content": sentence1 + "@-@" + sentence2
                }
            ],
            temperature=0.5,
            max_tokens=256,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
    )

    result = response['choices'][0]['message']['content']
    return True if result == "True" else (False if result == "False" else result)


"""
    Repeat sentence
    Return sentence
"""
def check_if_two_sentences_consistent(sentence:str) -> str:
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=
            [
                {
                  "role": "system",
                  "content": "You will be provided with a sentence, and your task is to repeat it in another way."
                },
                {
                  "role": "user",
                  "content": sentence
                }
            ],
            temperature=0.5,
            max_tokens=256,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
    )

    result = {"result":response['choices'][0]['message']['content'], "price":(response['usage']['prompt_tokens']/1000*0.0015+response['usage']['completion_tokens']/1000*0.002)}
    return result


def calculate_per_k_cost(sentence_to_be_calculated, words_price):
    words = word_count(sentence_to_be_calculated)
    cost_per_word = words_price / words
    per_k_cost = cost_per_word * 1000
    print("Per k words cost[$]: ", per_k_cost)
    return per_k_cost


if __name__ == "__main__":
    sentence1 = "When the person is configured with a role, if not set as the super user of the dock station, the person can only view files in her/his own dock station; if set as the super user of dock station, the person can not only view files in her/his own dock station, but also files in the dock station of following persons, including persons in her/his person group (including sub person groups) and persons in her/his dock station group."
    sentence2 = "Когато потребителят е конфигуриран с определена роля и не е зададен като суперпотребител на докинг станцията, той може да преглежда файлове само във своята собствена докинг станция. Ако обаче е зададен като суперпотребител на докинг станцията, той има право не само да преглежда файлове в своята/неговата собствена докинг станция, но и файлове в докинг станцията на следните лица, включително лица в неговата/нейната група (включително подгрупи лица) и лица в групата докинг станции."
    sentence3 = """Когато даден човек е конфигуриран с роля, ако не е зададен като супер потребител на докинг станцията, той може да преглежда файлове само в своята докинг станция; ако обаче е зададен като супер потребител на докинг "станцията", този човек може не само да преглежда файлове в своята докинг станция, но също и файлове във всички докинг станции на следните хора, включително хората от собствената му група (и подгрупи), както и на хората в групата на своята докинг станция."""
    # print(check_if_two_sentences_consistent(sentence1, sentence2))

    result = check_if_two_sentences_consistent(sentence3)
    print(result['result'])
    calculate_per_k_cost(sentence3, result['price'])

