#!/usr/bin/env python3
"""Validate that every skill packages and extracts without sibling dependencies."""
from __future__ import annotations

import argparse
import re
import shutil
import subprocess
import sys
import tempfile
import zipfile
from pathlib import Path, PurePosixPath

SKILLS = [
    "choka", "dodoitsu", "gogyohka", "haibun", "haiku",
    "katauta", "lunes", "monoku", "renga",
    "sedoka", "senryu", "sijo", "tanka",
]
FORBIDDEN_PARTS = {"shared", "evals-infra", "dist", ".github"}
FORBIDDEN_TEXT = (
    re.compile(r"(?im)\bshared/"),
    re.compile(r"(?im)\bevals-infra/"),
    re.compile(r"(?im)(?:^|[\s`])[^\s`/]+-workspace(?:[/\s`]|$)"),
    re.compile(r"(?im)\bload\s+(?:the\s+)?[\w-]+\s+skill\b"),
    re.compile(r"(?im)\buse\s+(?:the\s+)?[\w-]+\s+skill\b"),
    re.compile(r"(?im)\bselect\s+another\s+skill\b"),
)
TEXT_SUFFIXES = {".md", ".txt", ".json", ".py", ".js", ".ts", ".sh", ".go", ".rs", ".java", ".c", ".h", ".cpp"}


def safe_members(archive: zipfile.ZipFile, skill: str) -> list[str]:
    errors: list[str] = []
    for name in archive.namelist():
        member = PurePosixPath(name)
        if not name or member.is_absolute() or ".." in member.parts:
            errors.append(f"unsafe archive member {name!r}")
        if not name.startswith(f"{skill}/"):
            errors.append(f"member escapes skill root: {name!r}")
        if any(part in FORBIDDEN_PARTS or part.endswith("-workspace") for part in member.parts):
            errors.append(f"forbidden package member: {name!r}")
        if name.endswith("/"):
            errors.append(f"directory member is not allowed: {name!r}")
    return errors


def check_zip(path: Path, skill: str, extract_root: Path) -> list[str]:
    try:
        with zipfile.ZipFile(path) as archive:
            names = archive.namelist()
            errors = ["package is empty"] if not names else safe_members(archive, skill)
            if errors:
                return errors
            # Only extract after all member names have passed traversal checks.
            archive.extractall(extract_root)
            for name in names:
                if Path(name).suffix.lower() not in TEXT_SUFFIXES:
                    continue
                text = (extract_root / name).read_text(encoding="utf-8", errors="replace")
                for pattern in FORBIDDEN_TEXT:
                    if pattern.search(text):
                        errors.append(f"{name}: forbidden external-routing signal: {pattern.pattern}")
    except (OSError, zipfile.BadZipFile) as exc:
        return [f"cannot inspect package: {exc}"]

    top_level = sorted(path.name for path in extract_root.iterdir())
    if top_level != [skill]:
        errors.append(f"expected exactly one top-level directory {skill!r}, found {top_level}")
    if not (extract_root / skill / "SKILL.md").is_file():
        errors.append("package does not contain SKILL.md")
    return errors


def copy_skill_source(root: Path, skill: str, destination: Path) -> None:
    source = root / skill
    if not source.is_dir():
        raise FileNotFoundError(f"missing source skill directory: {source}")
    shutil.copytree(source, destination / skill)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--package-script", type=Path, default=None)
    args = parser.parse_args()
    root = args.root.resolve()
    package_script = (args.package_script or root / "package_skills.py").resolve()
    if not package_script.is_file():
        print(f"FAIL: package script not found: {package_script}")
        return 1

    failures = 0
    for skill in SKILLS:
        errors: list[str] = []
        with tempfile.TemporaryDirectory(prefix=f"standalone-source-{skill}-") as source_tmp, tempfile.TemporaryDirectory(prefix=f"standalone-extract-{skill}-") as extract_tmp:
            source_root = Path(source_tmp)
            extract_root = Path(extract_tmp)
            try:
                copy_skill_source(root, skill, source_root)
                shutil.copy2(package_script, source_root / "package_skills.py")
                destination = source_root / "dist"
                result = subprocess.run(
                    [sys.executable, "package_skills.py", "--target", str(destination)],
                    cwd=source_root,
                    text=True,
                    capture_output=True,
                )
                if result.returncode != 0:
                    errors.append(f"packager exited {result.returncode}: {result.stderr.strip()}")
                packages = sorted(destination.glob("*.skill")) if destination.is_dir() else []
                if len(packages) != 1 or packages[0].name != f"{skill}.skill":
                    errors.append(f"one-skill source produced {[p.name for p in packages]}, expected [{skill}.skill]")
                elif not errors:
                    errors.extend(check_zip(packages[0], skill, extract_root))
            except (OSError, shutil.Error) as exc:
                errors.append(str(exc))
        if errors:
            failures += 1
            print(f"FAIL {skill}: {'; '.join(errors)}")
        else:
            print(f"PASS {skill}")
    if failures:
        print(f"FAIL: {failures} of {len(SKILLS)} skills failed isolation")
        return 1
    print(f"PASS: {len(SKILLS)} skills packaged from one-skill sources and extracted safely")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
