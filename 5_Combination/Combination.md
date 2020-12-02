# Combination 구현 [Python3]

### Prob.

예를 들어, `[A, A, B, C]` 이란 리스트가 있을 때, 해당 리스트의 모든 부분 집합을 구하시오.

<br/>

### Sol.

* 처음 문제를 보았을 때, 이 문제는 Combination을 사용해서 모든 조합을 찾아내는 문제라고 생각함.
* Combination의 경우 `itertools` 패키지의 `combinations` 을 사용하면 되지만, 이를 직접 구현해보고자 함.
* 다른 블로그의 Combination 구현을 공부하던 중, 영감?을 얻어 직접 재귀로 구현함.

<br/>
<br/>

#### Version 2 (2020. 12. 01)

지난 번 `Combination` 구현 이후, `Permutation`을 구현해보면서 Class를 사용하는 구조로 구현을 해보았었고, 기존에 구현했던 `Combination`을 동일하게 Class화 하여 재구현 해보았다.

이번 **Ver. 2**에서는 크게 알고리즘적으로 변화된 부분은 없고, Class로는 이렇게도 구현할 수 있겠구나에 초점을 맞춰 코드를 작성해보았다.

<br/>

```python
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

```

<br/>

<br/>

#### Version 1

모 기업 면접에서 위와 같은 문제가 나왔었다. 당시 긴장해서 백지 상태인 데다가, 평소 패키지를 import해서 사용하기만 했던 `Combination`을 직접 구현하라고 하니... 아무것도 못하고 그냥 어버버 하다가 나왔다.

면접이 끝난 이후, `Combination`을 한 번 구현해보기 위해 여러 블로그들을 찾아봤지만, 대부분 내 머리로는 이해하기 어려웠다.

그 중 [이 블로그](https://shoark7.github.io/programming/algorithm/Permutations-and-Combinations)의 게시글이 그나마 가장 이해하기 쉬워, 해당 게시글로 `Combination` 구현을 공부하던 중 아래와 같은 아이디어가 떠올라서 직접 구현해보았다.

*(위 게시글에서 **순차적으로 / 재귀 / 정렬** 에서 아이디어를 얻어서 직접 구현해보았다.)*

<br/>

먼저, 문제와 같이 `[A, A, B, C]` 가 주어졌을 때, 각 원소에 대해 **순차적으로** 원소들을 가져와 **각 원소 별로 다음에 올 수 있는 경우의 수** 트리를 만들어 보았다.

<br/>

```txt
A ┬ @
  ├ A ┬ @
  │   ├ B ┬ @
  │   │   └ C ─ @
  │   └ C ─ @
  ├ B ┬ @
  │   └ C ─ @
  └ C ─ @

** '@'는 끝을 의미함 **
```

<br/>

각 원소에 대해 위와 같이 트리가 그려지고, DFS 처럼 **재귀**를 통해 부분 집합을 얻을 수 있을 것이라 생각했다.

따라서 아래와 같이 구현해보았다. (효율성은 개선이 필요해보인다.)

<br/>

```python
def combi(before, arr, answer):
    target = before + arr[0]
    arr[0] = '@'

    for i in range(len(arr)):
        if arr[i] == '@':  # 끝을 나타내는 문자를 만난 경우
            if target not in answer:
                answer.append(target)
        else:
            spam = target + arr[i]
            if spam not in answer:
                answer.append(spam)
            combi(target, arr[i:], answer)  # Recursive

    return answer


if __name__ == '__main__':
    target = ['A', 'A', 'B', 'C']
    answer = []
    for _ in range(len(target)):
        answer = combi('', target, answer)  # answer에 계속 이어서 추가
        target = target[1:]  # 순열이 아닌 조합이므로, C-A 같은 경우를 제외하기 위해

    answer.sort(key=lambda x : len(x))  # 길이 순으로 정렬

    for ans in answer:
        print([x for x in ans])
```
