import json
import subprocess
from pathlib import Path


def run(command: str) -> tuple[int, str]:
    script = Path(__file__).parent.parent / "scripts/tools/block-no-verify.sh"
    payload = json.dumps({"tool_input": {"command": command}})
    result = subprocess.run(
        ["bash", str(script)],
        input=payload,
        capture_output=True,
        text=True,
    )
    return result.returncode, result.stderr.strip()


def test_blocks_no_verify() -> None:
    code, err = run("git commit --no-verify -m 'msg'")
    assert code == 2
    assert "deny" in err


def test_allows_normal_commit() -> None:
    code, _ = run("git commit -m 'normal commit'")
    assert code == 0


def test_allows_no_verify_in_commit_message() -> None:
    # --no-verify inside a quoted message must not trigger the block
    code, _ = run("git commit -m 'use --no-verify carefully'")
    assert code == 0


def test_allows_no_verify_in_heredoc() -> None:
    code, _ = run("git commit -m \"$(cat <<'EOF'\n--no-verify\nEOF\n)\"")
    assert code == 0


def test_blocks_no_verify_after_message_flag() -> None:
    code, err = run("git commit -m 'msg' --no-verify")
    assert code == 2
    assert "deny" in err


def test_allows_unrelated_commands() -> None:
    code, _ = run("git push origin main")
    assert code == 0


def test_deny_response_is_valid_json() -> None:
    from typing import cast

    _, err = run("git commit --no-verify -m 'msg'")
    parsed = cast(dict[str, str], json.loads(err))
    assert parsed["decision"] == "deny"
    assert "reason" in parsed
