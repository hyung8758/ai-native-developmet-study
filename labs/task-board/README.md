# Task Board 실습

작은 Task Board에 완료 상태 변경과 삭제 기능을 추가하며, Agent에게 주는 맥락과 작업 환경이 결과에 미치는 영향을 비교합니다.

## 준비

- Python 3.10+
- `pip install -r requirements.txt`
- Codex 또는 `AGENTS.md`와 Skill 폴더를 지원하는 코딩 Agent

각 라운드를 별도의 작업 디렉터리나 Git worktree에서 열어 주세요. 시작 전에는 해당 라운드의 코드가 수정되지 않은 상태인지 확인합니다.

## 실행 방법

```bash
cd round-1
python -m pip install -r requirements.txt
uvicorn app.main:app --reload
```

브라우저에서 `http://127.0.0.1:8000`을 엽니다. Round 2에서도 디렉터리 이름만 `round-2`로 바꾸어 같은 방법으로 실행합니다.

## 실험 방법

### Round 1: 짧은 요청

`round-1/prompts/task.md`에 적힌 요청만 Agent에게 전달합니다. Agent가 결정하거나 추측하는 부분, 수정한 파일, 테스트 여부를 기록합니다.

### Round 2: 명세와 Harness

`round-2/`를 작업 공간으로 열어 `AGENTS.md`와 Skill이 적용되게 합니다. `round-2/prompts/task.md`의 명세를 전달하고 결과를 같은 기준으로 확인합니다. reviewer Agent 사용은 선택 활동입니다.

두 라운드의 목표 기능은 완료/미완료 토글과 삭제입니다. 추가 필터나 스타일 개선은 확장 과제로 남겨 핵심 비교 범위를 일정하게 유지합니다.

## 참고 자료와 자체 제작 자료

`references/README.md`에 실제 GitHub 자료의 원문 링크와 용도를 기록했습니다. Anthropic의 `webapp-testing` Skill 예제는 Apache-2.0 라이선스에 따라 원문 사본을 함께 두고, 실습에서 사용하는 간단한 Skill은 그 구조를 참고해 별도로 작성했습니다. Anthropic Claude Code의 reviewer Agent 예시는 Claude Code 전용 형식이므로 그대로 실행하지 않고, 아이디어를 Codex TOML reviewer 예제로 가볍게 옮겼습니다.
