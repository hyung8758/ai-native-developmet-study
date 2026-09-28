---
name: task-board-verification
description: Verify API and browser behavior after changing the Task Board. Use after changing task creation, completion, deletion, or frontend behavior.
---

# Task Board 검증

## 절차

1. 저장소 루트에서 `pytest -q`를 실행하고 실패가 있으면 결과를 요약한다.
2. 앱을 `uvicorn app.main:app --reload`로 실행한다.
3. 브라우저에서 `http://127.0.0.1:8000`을 열고 다음 동작을 확인한다.
   - 새 Task 추가
   - Task 완료와 미완료 전환
   - Task 삭제
4. 브라우저 콘솔에 오류가 있는지 확인한다.
5. 실패한 확인은 숨기지 말고 재현 단계와 함께 보고한다.

## 보고 형식

- 테스트: 통과/실패와 실행 명령
- 브라우저: 확인한 동작과 결과
- 콘솔: 오류 유무
- 남은 문제: 확인하지 못한 항목 또는 알려진 실패

