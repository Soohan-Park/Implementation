# Permutation 구현 [Python3]  

### Prob.

Permutation (순열) 구현.

1. 중복이 **가능**한 순열
2. 중복이 **불가능**한 순열

<br/>

### Sol.

* 지난 번 구현해보았던 `Combination`에 이어 `Permutation`을 한 번 구현해 보고자 함.
* 위 **Prob.**에도 나와 있듯이, 중복이 가능한 순열과 중복이 불가능한 순열에 대해 구현해보고자 함.
* `class`를 활용해서 구현해보았으며, 이를 바탕으로 `Combination`을 다시 한 번 구현해봐야 할 것 같음.

<br/>

<br/>

`Combination`을 구현했다면, 당연(?)하게 `Permutation`도 구현해봐야 한다고 생각해서 한 번 구현해 보았다.



##### 중복이 가능한 순열

```python
# 중복 가능
    def permutation(self, count, target, length, answer, permutation_all=False):
        if count == length: return answer

        count += 1

        # `length`까지 전부 출력 | `length`만 출력
        if permutation_all: pool = answer  # 이 때, pool은 answer객체의 위치를 가리키기만 한다.
        else: pool = []

        for i in range(len(answer)):
            for t in target:
                pool.append(answer[i] + t)

        return self.permutation(count, target, length, pool, permutation_all=permutation_all)
```

>  **Parameters**
>
> - count: 현재 만들고 있는 순열의 길이를 의미
> - target: 순열을 만들기 위해 주어진 대상
> - length: 만들고자 하는 순열의 길이
> - answer: 만들어진 순열을 저장하고 있는 리스트
> - permutation_all: 주어진 `length`에 해당하는 길이의 순열만 만들 것인지, 혹은 1~length까지 순열들을 모두 만들것인지 선택



위의 코드에서 보는 것과 같이 **중복을 허용하는** 순열을 구현하는 것은 간단하다.

**이중 반복문**을 통해 간단하게 구현 가능하다.

구현하다보니, 해당 `length`에 해당하는 길이의 순열만 만들 것인지, 혹은 `length`까지 길이의 순열들을 모두 만들 것인지 **`pool` 변수에 어떠한 값을 매칭시키는지**에 따라 이를 조절할 수 있다는 것을 알게 되었고 이를 구현해 보았다. *(주석 부분 참고)*



##### ~~중복이 불가능한 순열~~ (Not yet.)

```python
# 중복 불가능
    def permutation_no_duplicated(self):
        pass
```

> **Parameters**
>
> - 







전체 코드는 아래와 같다.



##### Source Code

```python
class Permutation:
    # 중복 가능
    def permutation(self, count, target, length, answer, permutation_all=False):
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

```

