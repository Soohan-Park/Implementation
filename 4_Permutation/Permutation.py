class Permutation:
    # 중복 가능
    def permutation(self, count, target, length, answer, permutation_all = False):
        if count == length: return answer

        count += 1

        # `length`까지 전부 출력 | `length`만 출력
        if permutation_all: pool = answer  # 이 때, pool은 answer객체의 위치를 가리키기만 한다.
        else: pool = []

        for i in range(len(answer)):
            for t in target:
                pool.append(answer[i] + t)

        return self.permutation(count, target, length, pool, permutation_all=permutation_all)

    # 중복 불가능
    def permutation_no_duplicated(self):
        pass


def test():
    target = ['1','2','3','4']
    per = Permutation()

    # 해당 `length`만 출력 (중복O)
    res = per.permutation(1, target, 3, target.copy(), permutation_all=True)  # copy()가 없다면, 동일한 객체를 참조하게 된다.
    print('Permutation of [1,2,3,4] / length: 1~3\n'
          '{}'.format(res))

    # 해당 `length`까지 모두 출력 (중복O)
    res = per.permutation(1, target, 3, target.copy())
    print('Permutation of [1,2,3,4] / length: 3\n'
          '{}'.format(res))


if __name__ == '__main__':
    test()
