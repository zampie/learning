import logging

logging.basicConfig(level=logging.DEBUG)


class BullsCowsAI:
    def __init__(self, target_size=4):
        self.candidates = list(range(0, 10))
        self.bulls = set()
        self.cows = set()
        self.not_in_target_nums = set()
        self.target_size = target_size
        self.answer = [1, 4, 5, 6]
        self.answer_template = [-1] * self.target_size
        self.round = 0
        self.wrong_answers = set()

    def update_info(self, bulls, cows):
        logging.debug('------------------------')
        logging.debug(f'round: {self.round}')

        self.wrong_answers.add(tuple(self.answer))

        self.bulls |= set(bulls)
        self.cows |= set(cows)
        self.cows -= self.bulls

        self.not_in_target_nums |= set(self.answer) - set(bulls) - set(cows)

        self.candidates = list((set(self.candidates) - set(self.answer)) | set(self.cows))

        if len(self.cows) + len(self.bulls) == self.target_size:
            # 公牛与奶牛数量足够填充答案时， 可忽略其他candidates
            print('sufficient cows')
            self.candidates = list(self.cows)

        for correct_num in bulls:
            self.answer_template[self.answer.index(correct_num)] = correct_num

        logging.debug(f'last answer: {self.answer}')
        logging.debug(f'input bulls: {bulls}')
        logging.debug(f'input cows: {cows}')
        logging.debug(f'curr bulls: {self.bulls}')
        logging.debug(f'curr cows: {self.cows}')
        logging.debug(f'not in target_nums: {self.not_in_target_nums}')
        logging.debug(f'candidates: {self.candidates}')
        logging.debug(f'answer template: {self.answer_template}')

    def generate_possible_answer(self):
        possible_answers = []

        def dfs(candidates, curr, idx):
            while idx < self.target_size and self.answer_template[idx] != -1:
                curr.append(self.answer_template[idx])
                idx = idx + 1

            if len(curr) == self.target_size:
                possible_answers.append(tuple(curr))
                return

            for i in range(len(candidates)):
                dfs(candidates[:i] + candidates[i + 1:], curr + [candidates[i]], idx + 1)

        dfs(self.candidates, [], 0)
        possible_answers = list(set(possible_answers) - self.wrong_answers)
        logging.debug(f'possible answers num: {len(possible_answers)}')
        return possible_answers

    def plan1(self):
        self.answer = self.generate_possible_answer()[0]
        return list(self.generate_possible_answer()[0])

    def plan2(self):
        # 不一定要选备选答案里的，尽快更新candidates
        if len(self.cows) + len(self.bulls) != self.target_size:
            # 试探没有选过的答案, 直到奶牛数量足够
            cunning_answer = list(set(self.candidates) - self.cows)
            logging.debug(f'cunning answer: {cunning_answer}')

            if len(cunning_answer) < self.target_size:
                # 如果长度不够，用上一次的答案(一定不在candidates中)填充
                cunning_answer = self.answer[:self.target_size - len(cunning_answer)] + cunning_answer
            else:
                cunning_answer = cunning_answer[:self.target_size]

            self.answer = cunning_answer

        else:
            self.answer = list(self.generate_possible_answer()[0])

    def answer_question(self, bulls, cows):
        self.update_info(bulls, cows)
        self.plan2()
        self.round += 1
        logging.debug(f'answer: {self.answer}')
        return self.answer

# def test_1():
#
#     target = [1, 2, 3, 4]
#
#     player = BullsCowsAI()
#
#     bulls = [1]
#     cows = [4]
#     answer = player.answer_question(bulls, cows)  # 1023
#     if answer == target:
#         print('win')
#
#     bulls = [2, 3]
#     cows = []
#     answer = player.answer_question(bulls, cows)  # 1234
#     if answer == target:
#         print('win')
#     assert answer == target
#
#
# def test_2():
#     target = [5, 0, 7, 8]
#
#     player = BullsCowsAI()
#
#     bulls = []
#     cows = [5]
#     answer = player.answer_question(bulls, cows)  # 0237
#     if answer == target:
#         print('win')
#
#     bulls = []
#     cows = [0, 7]
#     answer = player.answer_question(bulls, cows)  # 0289
#     if answer == target:
#         print('win')
#
#     bulls = []
#     cows = [8]
#     answer = player.answer_question(bulls, cows)  # 8570
#     if answer == target:
#         print('win')
#
#     bulls = [7]
#     cows = [8, 5, 0]
#     answer = player.answer_question(bulls, cows)  # 5078
#     if answer == target:
#         print('win')
#     assert answer == target


if __name__ == '__main__':
    target = [5, 0, 7, 8]

    player = BullsCowsAI()

    bulls = []
    cows = [5]
    answer = player.answer_question(bulls, cows)  # 0237
    if answer == target:
        print('win')

    bulls = []
    cows = [0, 7]
    answer = player.answer_question(bulls, cows)  # 0289
    if answer == target:
        print('win')

    bulls = []
    cows = [8]
    answer = player.answer_question(bulls, cows)  # 8570
    if answer == target:
        print('win')

    bulls = [7]
    cows = [8, 5, 0]
    answer = player.answer_question(bulls, cows)  # 5078
    if answer == target:
        print('win')
    assert answer == target
