"""
Solved.
https://shoark7.github.io/programming/algorithm/Permutations-and-Combinations
위의 블로그에서 `중복된 문자가 들어있는 순열`에 대한 해결 방안을 참고하였다.
"""


class Permutation:
    def permutation(self, before, target, visited, answer, length):
        if len(before) == length:
            answer.append(before)
            return answer

        for i in range(len(target)):
            # 블로그 참고
            #    1) DFS처럼 사용한 값, 중복 사용 방지
            #    2) (정렬된 target에서) 이전값과 동일한 값 사용 방지
            #    3) 바로 이전 값이 사용중인지 확인 (사용중이여야만 함 - DFS처럼)
            if not visited[i] and (i == 0 or target[i - 1] != target[i] or visited[i - 1]):
                before += target[i]
                visited[i] = True  # 사용 LOCK
                answer = self.permutation(before, target, visited, answer, length)
                visited[i] = False  # 사용 UNLOCK
                before = before[:-1]

        return answer


def test():
    target = ['A', 'A', 'B', 'C']
    # target = ['1', '2', '3', '4']

    target.sort()

    res = []
    visited = [False for _ in range(len(target))]
    per = Permutation()

    # 해당 `length`까지 출력
    for i in range(3):
        res = per.permutation('', target, visited, res, i+1)
    print('All permutation of {} / length: 1~3\n{}'.format(target, res))

    # 해당 `length`만 모두 출력
    res = []
    res = per.permutation('', target, visited, res, 3)
    print('Permutation of {} / length: 3\n{}'.format(target, res))


if __name__ == '__main__':
    test()
