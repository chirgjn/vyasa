import subprocess
from pathlib import Path


def run(target: str | Path) -> tuple[int, str, str]:
    script = Path(__file__).parent.parent / "framework/tools/find-docs-dir.sh"
    result = subprocess.run(
        ["bash", str(script), str(target)],
        capture_output=True,
        text=True,
    )
    return result.returncode, result.stdout.strip(), result.stderr.strip()


def make_layout(tmp_path: Path, docs_rel: str) -> Path:
    layout = tmp_path / "layout.md"
    _ = layout.write_text(f"---\ndocs: {docs_rel}\n---\n# Layout\n")
    return layout


def test_finds_docs_dir_from_file_in_same_dir(tmp_path: Path) -> None:
    _ = make_layout(tmp_path, "docs")
    (tmp_path / "docs").mkdir()
    target = tmp_path / "AGENTS.md"
    _ = target.write_text("# Agents")
    code, out, _ = run(target)
    assert code == 0
    assert out == str(tmp_path / "docs")


def test_finds_docs_dir_walking_up(tmp_path: Path) -> None:
    _ = make_layout(tmp_path, "docs")
    (tmp_path / "docs").mkdir()
    subdir = tmp_path / "services" / "payments"
    subdir.mkdir(parents=True)
    target = subdir / "some-file.md"
    _ = target.write_text("content")
    code, out, _ = run(target)
    assert code == 0
    assert out == str(tmp_path / "docs")


def test_no_layout_md_returns_error(tmp_path: Path) -> None:
    target = tmp_path / "AGENTS.md"
    _ = target.write_text("content")
    code, _, err = run(target)
    assert code == 1
    assert "no layout.md found" in err


def test_layout_md_missing_docs_field_returns_error(tmp_path: Path) -> None:
    _ = (tmp_path / "layout.md").write_text("---\ntitle: foo\n---\n")
    target = tmp_path / "AGENTS.md"
    _ = target.write_text("content")
    code, _, err = run(target)
    assert code == 1
    assert "no 'docs:' field" in err


def test_nonexistent_target_resolves_nearest_parent(tmp_path: Path) -> None:
    _ = make_layout(tmp_path, "docs")
    (tmp_path / "docs").mkdir()
    # Target file does not exist yet — simulates a new file being written
    target = tmp_path / "new-subdir" / "new-file.md"
    code, out, _ = run(target)
    assert code == 0
    assert out == str(tmp_path / "docs")


def test_directory_target(tmp_path: Path) -> None:
    _ = make_layout(tmp_path, "docs")
    (tmp_path / "docs").mkdir()
    subdir = tmp_path / "subdir"
    subdir.mkdir()
    code, out, _ = run(subdir)
    assert code == 0
    assert out == str(tmp_path / "docs")
