from resources import question_data

class Questions:
    def __init__(self, quest, answer):
        self.quest= quest
        self.answer= answer
class Quiz:
    def __init__(self, list):
        self.quest_number= 0
        self.score= 0
        self.quest_list= list
    
    def still_has_quest(self):
        return self.quest_number< len(self.quest_list)
    
    def next_quest(self):
        current_quest= self.quest_list[self.quest_number]
        self.quest_number += 1
        input(f'Q.{self.quest_number}: {current_quest.quest} (True/False): ')


question_bank=[]
for question in question_data:
    question_text= question['question']
    quest_answer= question['correct_answer']
    next_quest= Questions(question_text, quest_answer)
    question_bank.append(next_quest)
    
quiz= Quiz(question_bank)
quiz.next_quest()



