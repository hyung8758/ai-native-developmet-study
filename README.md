# AI-Native Development Study

AI-Native 개발자로 성장하기 위한 신입 교육 자료와 실습 코드를 관리하는 저장소입니다. 개념을 먼저 학습한 뒤, Agent에게 주는 작업 조건을 바꾸어 같은 개발 과제의 결과를 비교하는 것을 목표로 합니다.

## 저장소 구성

```text
.
├── README.md
├── lessons/                 # 읽고 학습할 이론 자료
└── labs/                    # 개념을 실험하는 실습
    └── task-board/
        ├── round-1/          # 짧은 요청으로 시작하는 기본 환경
        ├── round-2/          # 작업 명세와 Agent 설정이 포함된 환경
        ├── references/       # GitHub 참고 사례 및 출처·라이선스
        └── scorecard.md      # 라운드 결과 비교 기록지
```

## 학습 순서

먼저 [lessons/README.md](lessons/README.md)의 순서에 따라 이론 자료를 읽습니다.

1. AI 보조 코딩에서 AI-Native 개발로
2. Prompt를 작업 명세로 발전시키기
3. Context Engineering
4. AGENTS.md와 Skills
5. Harness와 검증 루프
6. 사람의 역할과 Agent 협업

## 실습: Task Board

FastAPI 기반 Task Board에 완료 상태 변경과 삭제 기능을 추가하는 과제입니다. 두 라운드의 앱은 동일한 초기 상태에서 시작하고, Agent에게 제공하는 작업 조건이 다릅니다.

- **Round 1:** [요청문](labs/task-board/round-1/prompts/task.md)을 사용합니다. 별도의 프로젝트 지침이나 Skill은 제공하지 않습니다.
- **Round 2:** [작업 명세](labs/task-board/round-2/prompts/task.md)를 사용합니다. [AGENTS.md](labs/task-board/round-2/AGENTS.md), 검증 Skill, 선택형 Code Reviewer 설정이 포함됩니다.

실습 전 각 라운드의 앱을 별도 작업 폴더나 Git worktree에서 열어 초기 상태를 보존하세요. 각 앱 실행, 의존성 설치 및 실험 절차는 [labs/task-board/README.md](labs/task-board/README.md)를 참고합니다. 결과는 [scorecard](labs/task-board/scorecard.md)에 같은 기준으로 기록합니다.

## 참고 자료

실습의 Skill과 Agent 설정은 실제 공개 저장소의 구조와 사례를 참고합니다. 원문 링크, 로컬 사본 여부, 라이선스와 도구 간 차이는 [참고 자료 안내](labs/task-board/references/README.md)에 기록했습니다. 실습 자료와 참고 사례를 그대로 동일한 Agent 제품에서 실행할 수 있다고 가정하지 말고, 각 파일의 안내를 확인하세요.

## 교육 자료 기여

이론 자료는 `lessons/`, 실험 프롬프트와 코드 및 결과 기록은 `labs/`에 둡니다. 실습 조건을 변경할 때는 두 라운드의 초기 앱과 요구사항 범위가 계속 비교 가능하도록 함께 검토합니다.

