#Model Knowledge
question_answer_id = """
질문: 
주주총회에 대해서 설명해주세요

답변: 
주주총회는 주식회사의 주인인 주주들이 모여 회사의 중요한 의사결정을 내리는 회의입니다.
주식회사의 주주들은 자신이 보유한 주식 수만큼 의결권을 행사할 수 있으며, 이를 통해 회사의 경영에 참여합니다. 
주주총회는 매년 정기적으로 실시하는 정기주주총회와 필요에 따라 비정기적으로 개최하는 임시주주총회가 있습니다.

주주총회는 기업의 주인인 주주들이 모여 회사의 중요한 의사결정을 내리는 자리이기 때문에, 모든 주주가 참석할 수 있도록 일정을 정하고, 안건을 미리 공지하는 것이 중요합니다. 
또한, 주주들의 의견을 적극적으로 수렴하고, 공정한 절차를 통해 의사결정을 내리는 것이 중요합니다.
"""


def question_prompt(user_question, qa_sample):
    prompt = ""
    prompt += "<s>[INST] <<SYS>>\n"\
            "항상 도움이 되는 답변을 제공하되, 악의적이거나 비윤리적이거나 인종 차별적이거나 성차별적인 답변을 해서는 안 됩니다.\n"\
            "편견 없이 긍정적인 답변을 제공하세요\n"\
            "한국어 맞춤법 가이드라인에 따라 한국어로 질문에 간결하게 답변하세요.\n"\
            "외래어는 한국어로 번역하지 말고 영어로 남겨주세요.\n"\
            "길게 설명하지 말고 짧고 명확하게 답변하세요.\n"\
            "항상 사실을 바탕으로 환각에 빠지지 말고 질문에 답변하세요.\n"\
            "다음은 답변에 참조할 수 있는 몇가지 예시 입니다.:\n"\
            f"{qa_sample}\n"\
            "질문과 답변 사이에 연관성이 없다고 생각하는 경우, '답변을 위해서는 추가정보가 필요합니다' 라고 응답하세요.\n"\
            "<</SYS>>\n"\
            "아래 질문에 답변하세요. 답변할때에는 반드시 한국어만 사용해야 합니다.:\n"\
            "[/INST]\n"\
            f"질문: {user_question}\답변: "
    return [prompt]


def answer_retrieval(model, prompt):
    answer_retrieval =  model.generate(prompt)
    print(answer_retrieval)
    result = answer_retrieval.generations[0][0].text
    return result

