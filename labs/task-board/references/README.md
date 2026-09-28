# 공개 GitHub 참고 사례

실습 자료는 공개 저장소의 실제 구조와 workflow를 참고합니다. 아래에서 원문 예시를 보되, 저장소별 Agent 제품과 실행 환경의 차이를 구분하세요.

## Skill: Anthropic webapp-testing

- [원본 SKILL.md](https://github.com/anthropics/skills/blob/main/skills/webapp-testing/SKILL.md)
- [이 폴더의 원문 사본](anthropic-webapp-testing/SKILL.md)
- [라이선스](anthropic-webapp-testing/LICENSE.txt): Apache License 2.0
- 참고할 점: 목적이 분명한 Skill 메타데이터, 브라우저 동작을 관찰한 뒤 자동화하는 절차, 체크리스트와 보조 리소스의 분리
- 출처 고지: 아래 사본은 원문을 보존한 참고용 사본입니다. 이 실습 저장소의 `round-2/.agents/skills/task-board-verification/SKILL.md`는 이 아이디어를 바탕으로 새로 작성한 경량 실습 예제입니다.

Anthropic 저장소는 Skills가 지침, 스크립트, 참고 자료를 한 폴더에 묶을 수 있다고 설명합니다. 실제 `webapp-testing` 예시는 Playwright 스크립트를 사용하므로, 현재 실습용 경량 Skill과 실행 의존성이 같지는 않습니다.

## Skill과 프로젝트 규칙: OpenAI Agents Python

- [실제 AGENTS.md](https://github.com/openai/openai-agents-python/blob/main/AGENTS.md)
- [code-change-verification Skill](https://github.com/openai/openai-agents-python/blob/main/.agents/skills/code-change-verification/SKILL.md)
- 참고할 점: `AGENTS.md`에서 저장소의 공통 규칙과 Skill 사용 조건을 안내하고, 반복 검증의 구체 절차는 Skill로 분리
- 이 레포의 `AGENTS.md`와 Skill은 학생용으로 단순화해 직접 작성했습니다.

원본 Skill은 해당 SDK 저장소의 Make/uv workflow에 의존합니다. 실습 앱에 그대로 복사하지 않고, 우리 앱에 맞는 pytest와 브라우저 확인 절차를 작성합니다.

## Agent: Anthropic Claude Code reviewer 예시

- [Code Review Agent 예제가 포함된 GitHub 문서](https://github.com/anthropics/claude-code/blob/main/plugins/plugin-dev/skills/agent-development/examples/complete-agent-examples.md)
- 참고할 점: 읽기 중심 도구, 변경 사항 기반 검토, 심각도별 구체적인 피드백
- 제품 차이: 원본 frontmatter와 도구 이름은 Claude Code 형식입니다. `round-2/.codex/agents/code-reviewer.toml`은 역할과 출력 형식만 참고해 직접 쓴 Codex용 실습 예시입니다.

Codex용 TOML 사용자 Agent 형식은 [Codex Subagents 문서](https://developers.openai.com/codex/subagents)를 따릅니다. Agent 설정은 프로젝트 범위 `.codex/agents/`에 두며, 실습에서 직접 호출하거나 Agent 지원 환경에서 확인합니다.

## 실습 안에서 직접 작성한 파일

- `round-2/AGENTS.md`: 공통 프로젝트 규칙
- `round-2/.agents/skills/task-board-verification/SKILL.md`: UI/API 검증 절차
- `round-2/.codex/agents/code-reviewer.toml`: 변경 내용을 읽기 전용으로 점검하는 선택 reviewer
