# 실습

`lessons/`에서 배운 개념을 실제 작업으로 비교하고 관찰하는 실험 공간입니다. 실습 앱은 처음부터 기능이 완성되어 있지 않으며, Agent에게 같은 목표를 서로 다른 조건으로 맡겨 결과를 비교합니다.

## 실습 순서

1. `task-board/round-1/`에서 `prompts/task.md`의 짧은 요청으로 기능을 요청합니다.
2. 변경 파일, 테스트, 제약 준수와 사람의 개입을 `task-board/scorecard.md`에 기록합니다.
3. `task-board/round-2/`에서 `prompts/task.md`의 명세와 프로젝트 규칙, Skill을 사용해 요청합니다.
4. 결과를 같은 기준으로 비교하고, `task-board/references/`에 있는 실제 공개 저장소 사례와 실습 설정을 살펴봅니다.

두 라운드는 동일한 초기 앱에서 시작합니다. Round 1에는 작업 지침 파일과 Skill이 없고, Round 2에는 실습용 `AGENTS.md`, Skill, 선택적으로 사용할 reviewer Agent 설정이 있습니다.

## 폴더 안내

- `task-board/round-1/`: 최소 FastAPI 앱, 사전 설정 없음
- `task-board/round-2/`: 동일한 앱과 실습용 Agent 설정
- 각 라운드의 `prompts/task.md`: 해당 라운드의 요청문 또는 작업 명세
- `task-board/references/`: 공개 GitHub 사례, 출처 및 라이선스 정보
- `task-board/scorecard.md`: 비교 관찰 기록지
