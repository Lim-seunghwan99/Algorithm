def boj18869():
    M, N = list(map(int, input().split()))
    # 행성의 크기를 알고 있을 때, 균등한 우주의 쌍이 몇 개인가?, 구성이 같은데 순서만 다른 우주의 쌍은 한 번만 센다.
    # Ai < Aj -> Bi < Bj
    # Ai = Aj -> Bi = Bj
    # Ai > Aj -> Bi > Bj 이면 균등
    S = {}
    for _ in range(M):
        planet = list(map(int, input().split()))
        # 중복된 값을 제거하고, 중복이 제거된 행성들을 오름차순으로 정렬한다.
        sortedPlanet = sorted(list(set(planet)))  # 일대일 대응 함수 공역 만들기
        # 정렬된 고유 크기 리스트를 이용해 각 크기 값이 몇 번째 순위인지를 매핑하는 딕셔너리
        ranked = {sortedPlanet[i]: i for i in range(len(sortedPlanet))}
        vector = tuple([ranked[i] for i in planet])
        S[vector] = S.get(vector, 0) + 1

    ans = 0
    # print(S)
    for i in S.values():
        ans += (i*(i-1)) // 2
    print(ans)



if __name__ == "__main__":
    # boj15665()
    # boj16987()
    # boj5427()
    # boj13549()
    boj18869()