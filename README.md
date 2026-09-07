# coding-test

프로그래머스·백준 코딩 테스트 풀이와 복습 기록입니다.

## 학습 원칙

- 풀이 코드는 백준허브로 자동 업로드합니다. 최초 브라우저 연동이 필요합니다.
- 문제는 **플랫폼 → 난이도 → 문제 번호와 이름** 순서로 관리합니다.
- 틀렸거나 힌트를 본 문제는 핵심 아이디어와 놓친 조건을 기록합니다.
- 알고리즘 유형은 복습 목록에서 분류하고, 코드를 여러 폴더에 중복 보관하지 않습니다.

## 저장소 구조

아래 플랫폼 폴더는 첫 풀이 업로드 시 백준허브가 생성합니다. 실제 폴더명은 확장 프로그램 설정에 따라 달라질 수 있습니다.

```text
coding-test/
├── README.md
├── 프로그래머스/              # 첫 업로드 시 생성
│   └── 난이도/
│       └── 문제번호. 문제이름/
│           ├── 풀이코드
│           └── README.md
├── 백준/                      # 백준 풀이 업로드 시 생성
└── notes/
    ├── review-list.md
    ├── problems/
    │   └── TEMPLATE.md
    └── concepts/
        └── README.md
```

## 복습 기록

- [다시 풀 문제 목록](notes/review-list.md)
- [문제별 복습 양식](notes/problems/TEMPLATE.md)
- [개념 노트 작성 안내](notes/concepts/README.md)

문제별 노트 파일명은 `programmers-문제번호.md`, `baekjoon-문제번호.md`로 작성합니다.
자동 생성되는 문제 README 대신 `notes/`에 직접 쓴 해설을 보관합니다.

## 백준허브 연결 방법

1. Chrome에서 [백준허브](https://chromewebstore.google.com/detail/ccammcjdkpgjmcpijpahlehmapgmphmk)를 설치합니다.
2. 확장 프로그램의 **Authorize with GitHub**로 인증합니다.
3. 기존 저장소 연결을 선택하고 **20220348-kim/coding-test**를 지정합니다.
4. 디렉터리 구조를 **플랫폼별**로 선택하고 **Get Started**로 연결합니다.
5. 프로그래머스에서 **제출 후 채점하기**를 눌러 정답 처리된 뒤 업로드가 완료될 때까지 기다립니다.
6. 이 저장소에 해당 문제의 코드와 README가 생성됐는지 확인합니다.

단순 코드 실행은 정답 제출과 다릅니다. 업로드 도중 페이지를 이동하거나 닫지 않습니다.

[백준허브 공식 사용 안내](https://github.com/BaekjoonHub/BaekjoonHub)
