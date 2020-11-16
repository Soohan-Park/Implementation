# Permutation 구현 [Python3]  

### Prob.

Permutation (순열) 구현.

<br/>

### Sol.

* 지난 번 구현해보았던 `Combination`에 이어 `Permutation`을 한 번 구현해 보고자 함.
* `class`를 활용해서 구현해보았으며, 이를 바탕으로 `Combination`을 다시 한 번 구현해봐야 할 것 같음.
* **중복된 문자가 들어있는 경우**로 인해 약 1주를 고생고생하다.. [이 블로그](https://shoark7.github.io/programming/algorithm/Permutations-and-Combinations)를 참고하여 해결하였다!

<br/>

<br/>

`Combination`을 구현해 보았다면, 당연하게(?) `Permutation`도 구현해봐야 하지 않겠는가.

**재귀**를 활용해 비교적 금방 구현해낸 `Combination`에 반해, `Permutation`을 구현하는 데에는 오랜 시간이 소요되었다.

그 이유는, **순열을 생성하고자 하는 집합에 동일한 문자열이 있는 경우**를 처리하는 것이 생각보다 복잡하였다.

결국, 온전하게 스스로 해결하지는 못하였지만, 위의 링크해 둔 블로그를 참고하여 해당 이슈에 대한 해결방안을 찾을 수 있었다!

*(심지어 itertools에서 발생하는 중복되는 경우도 해결된다..!!)*

<br/>

##### Permutation

```python
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
```

>  **Parameters**
>
> - before: 생성중(?)인 순열을 담고 있는 변수
> - target: 순열을 만들기 위해 주어진 대상
> - visited: 각각의 target 값이 현재 순열에서 사용중인지를 나타내는 리스트
> - answer: 만들어진 순열을 저장하고 있는 리스트
> - length: 만들고자 하는 순열의 길이





그 고생을 했는데... 생각보다 코드 길이는 매우 짧아서 허탈했다.

위 코드에서 가장 핵심이 되는 부분은,



> ##### 1.
>
> ```python
> if not visited[i] and (i == 0 or target[i - 1] != target[i] or visited[i - 1]):
> ```

> ##### 2.
>
> ```python
> visited[i] = True  # 사용 LOCK
> answer = self.permutation(before, target, visited, answer, length)
> visited[i] = False  # 사용 UNLOCK
> ```



이렇게 두 부분이 아닐까 한다. 

**1.**을 통해, 한 번 사용했던 값들이 중복되어 사용되는 것을 방지해주고, 뿐만 아니라 중복되는 문자열로 만들어지는 순열의 중복 생성을 방지해준다.

**2.**을 통해, 리스트 visited의 상태를 변경시킴으로써, 해당 값에 대한 Lock과 같은 역할을 하게 된다. (이를 통해, **1.**에서의 동일한 값 중복 사용 방지)

<br/>

평소 `itertools` 로 편하게 사용하던 메서드인 `Permutation`을 직접 구현해보면서, 간단하고 쉬워보이는 것도 다시 들여다보면 생각보다 복잡할 수 있다는 것을 배울 수 있었다.~~*세상에 쉬운 거 하나 없다*~~



테스트 코드를 포함한 전체 소스 코드는 아래와 같다.

<br/>

##### Source Code

```python
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

```

