def answerConfirm(quest):
    valid_abswers_pt = ('S', 'N')
    while True:
        try:
            answer = input(quest).upper()
            assert answer in valid_abswers_pt
            if answer == 'S' or answer == 'Y':
                return True
            else:
                return False
        except:
              print(f"'{answer}' não é uma resposta válida")
