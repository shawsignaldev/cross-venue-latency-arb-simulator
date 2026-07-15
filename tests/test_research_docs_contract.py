from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def test_research_depth_docs_exist() -> None:
    for relative in [
        "docs/math-model.md",
        "docs/validation-protocol.md",
        "docs/limitations-and-regimes.md",
    ]:
        path = ROOT / relative
        assert path.exists(), f"missing {relative}"
        text = path.read_text(encoding="utf-8")
        assert len(text.split()) >= 130
        assert "##" in text

def test_readme_links_research_depth_docs() -> None:
    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    for relative in [
        "docs/math-model.md",
        "docs/validation-protocol.md",
        "docs/limitations-and-regimes.md",
    ]:
        assert relative in readme
