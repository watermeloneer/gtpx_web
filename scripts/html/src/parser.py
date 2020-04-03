import string
import json
import base64

import pathlib

from bs4 import BeautifulSoup


class QuestionsPaser:

    def paser(self, fpath):
        save_path = fpath.split('.')[0] + '.json'
        with open(fpath) as html_doc:
            soup = BeautifulSoup(html_doc)
            questions = self._get_questions(soup)
            self._save(questions, save_path)


    def _get_questions(self, soup):
        questions = []
        questions_div = soup.find_all("div", class_="questions")
        for question_div in questions_div:
            qtype = self._get_qtype(question_div)
            content = self._get_qcontent(question_div)
            answers = self._get_answers(question_div)
            answer = self._get_correct_answer(question_div)
            question = {
                'qtype': qtype,
                'content': content,
                'answers': answers,
                'answer': answer
            }
            print(question)

            questions.append(question)
        return questions
    

    def _get_qtype(self, div):
        # 判断题 单选题
        qtype = div.find_all("div", class_='questions-title')[0].text.split(' ')[-1]
        return qtype

    def _get_qcontent(self, div):
        qcontent = div.find_all("div", class_='exam-question')[0].text.replace('\n', '').replace(' ', '')
        return qcontent

    def _get_answers(self, div):
        """单选题
        <div class="answers">
        <div class="select single-select a.">
        <input class="radioOrCheck hidden" data-name="a" data-type="1" id="3407271" name="keyChk_questions_340727" type="radio"/>
        <label for="3407271">
        <span class="select-icon"><i class="icon icon-m_exam_correct"></i></span>
        <span class="words">串联或并联 </span>
        </label>
        </div>
        <div class="select single-select b.">
        <input class="radioOrCheck hidden" data-name="b" data-type="1" id="3407272" name="keyChk_questions_340727" type="radio"/>
        <label for="3407272">
        <span class="select-icon"><i class="icon icon-m_exam_correct"></i></span>
        <span class="words">串联 </span>
        </label>
        </div>
        <div class="select single-select c.">
        <input class="radioOrCheck hidden" data-name="c" data-type="1" id="3407273" name="keyChk_questions_340727" type="radio"/>
        <label for="3407273">
        <span class="select-icon"><i class="icon icon-m_exam_correct"></i></span>
        <span class="words">并联 </span>
        </label>
        </div>
        </div>
        """

        """判断题
        <div class="answers">
        <div class="select judge rt">
        <input class="radioOrCheck hidden" data-name="true" data-type="3" id="3406591" name="keyJudge_questions_340659" type="radio" value="true"/>
        <label for="3406591">
        <span class="select-icon"><i class="icon icon-m_exam_correct"></i></span>
        <span class="words">正确</span>
        </label>
        </div>
        <div class="select judge wg">
        <input class="radioOrCheck hidden" data-name="false" data-type="3" id="3406592" name="keyJudge_questions_340659" type="radio" value="false"/>
        <label for="3406592">
        <span class="select-icon"><i class="icon icon-m_exam_error"></i></span>
        <span class="words">错误</span>
        </label>
        </div>
        </div>
        """
        answers = div.find_all("div", class_='answers')[0]
        choices = answers.find_all("span", class_='words')
        answer_text = ''
        for index, words in enumerate(choices):
            choice_text = words.text
            choice_en = string.ascii_uppercase[index]
            answer_text = answer_text + "**" + choice_en + "、" + choice_text

        print(answer_text)
        return answer_text

    def _get_correct_answer(self, div):
        # base64 解密

        encoded_answer = div.find_all("div", class_='question-content')[0]['date-answer']
        answer_str = base64.b64decode(encoded_answer).decode("utf-8", "ignore")
        print(answer_str)
        answer_json = json.loads(answer_str)
        answer = answer_json['answer']
        if answer == 'true':
            answer = 'A'
        elif answer == 'false':
            answer = 'B'
        elif isinstance(answer, (list, tuple)):
            answer = answer[0]
        else:
            pass

        return answer.capitalize()

    def _save(self, questions, save_path):
        with open(save_path, 'w') as f:
            data = json.dumps(questions, ensure_ascii=False)
            f.write(data)


if __name__ == "__main__":
    fpath = '/Users/turkey/Projects/gtpx_web/scripts/html/src/基础训练-低压电工作业.htm'
    QuestionsPaser().paser(fpath)
    fpath = '/Users/turkey/Projects/gtpx_web/scripts/html/src/基础训练-高处安装、维护、拆除作业-在线100分.htm'
    QuestionsPaser().paser(fpath)
    fpath = '/Users/turkey/Projects/gtpx_web/scripts/html/src/基础训练-高压电工作业-在线100分.htm'
    QuestionsPaser().paser(fpath)
    fpath = '/Users/turkey/Projects/gtpx_web/scripts/html/src/基础训练-熔化焊接与热切割作业-在线100分.htm'
    QuestionsPaser().paser(fpath)