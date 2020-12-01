class Combination:
    NULL = '@'

    def combination(self, before, arr, answer):
        target = before + arr[0]
        arr[0] = self.NULL

        for i in range(len(arr)):
            if arr[i] == self.NULL:  # 끝을 나타내는 문자를 만난 경우
                if target not in answer:
                    answer.append(target)
            else:
                spam = target + arr[i]
                if spam not in answer:
                    answer.append(spam)

                self.combination(target, arr[i:], answer)  # Recursive

        return answer


def test():
    target = ['A', 'A', 'B', 'C']
    answer = []
    combi = Combination()

    for _ in range(len(target)):
        answer = combi.combination('', target, answer)  # answer에 계속 이어서 추가
        target = target[1:]  # 순열이 아닌 조합이므로, C-A 같은 경우를 제외하기 위해

    answer.sort(key=lambda x: len(x))  # 길이 순으로 정렬

    for ans in answer:
        print( [x for x in ans] )


if __name__ == '__main__':
    test()
