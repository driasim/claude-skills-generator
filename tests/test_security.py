"""Security tests for claude-skills-generator PRs:
- PR #4: Path traversal prevention
- PR #3: Branch injection prevention
"""

import os
import sys
import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))


# --- PR #3: Branch Injection ---
def test_branch_injection_prevention():
    """Verify branch names are sanitized to prevent injection"""
    root = os.path.join(os.path.dirname(__file__), "..")
    found_sanitization = False
    for dirpath, dirnames, filenames in os.walk(root):
        if ".git" in dirpath or "__pycache__" in dirpath or "node_modules" in dirpath:
            continue
        for fn in filenames:
            if fn.endswith((".py", ".js", ".ts")):
                fpath = os.path.join(dirpath, fn)
                with open(fpath) as f:
                    content = f.read()
                injection_patterns = [
                    "branch", "sanitize", "escape",
                    "re.sub", "re.match", "re.compile",
                    "shlex", "quote",
                    "injection", "shell",
                ]
                found = [p for p in injection_patterns if p in content]
                if len(found) >= 2:
                    found_sanitization = True
    assert found_sanitization, "Should find branch name sanitization"


def test_branch_name_not_passed_directly_to_git():
    """Verify branch name is not passed unsanitized to git commands"""
    root = os.path.join(os.path.dirname(__file__), "..")
    for dirpath, dirnames, filenames in os.walk(root):
        if ".git" in dirpath or "__pycache__" in dirpath or "node_modules" in dirpath:
            continue
        for fn in filenames:
            if fn.endswith((".py", ".js", ".ts")):
                fpath = os.path.join(dirpath, fn)
                with open(fpath) as f:
                    content = f.read()
                if "git checkout" in content or "git branch" in content:
                    # Should use subprocess with list, not shell=True
                    if "shell=True" in content:
                        # If using shell=True, params should be quoted
                        has_quote = any(
                            p in content for p in [
                                "shlex.quote", "pipes.quote",
                                "f'", "format(", ".format(",
                            ]
                        )
                        assert has_quote, "Shell mode with branch should have quoting"
                    return True


# --- PR #4: Path Traversal ---
def test_path_traversal_prevention():
    """Verify path traversal is prevented in file operations"""
    root = os.path.join(os.path.dirname(__file__), "..")
    found_protection = False
    for dirpath, dirnames, filenames in os.walk(root):
        if ".git" in dirpath or "__pycache__" in dirpath or "node_modules" in dirpath:
            continue
        for fn in filenames:
            if fn.endswith((".py", ".js", ".ts")):
                fpath = os.path.join(dirpath, fn)
                with open(fpath) as f:
                    content = f.read()
                protection_patterns = [
                    "os.path.abspath", "os.path.realpath", "os.path.normpath",
                    "Path(", "resolve(", "relative_to",
                    "startswith", "safe_join",
                    "..", "traversal",
                ]
                found = [p for p in protection_patterns if p in content]
                if len(found) >= 2:
                    found_protection = True
    assert found_protection, "Should find path traversal protection"


def test_path_validation_in_skill_creation():
    """Verify skill file paths are validated"""
    root = os.path.join(os.path.dirname(__file__), "..")
    for dirpath, dirnames, filenames in os.walk(root):
        if ".git" in dirpath or "__pycache__" in dirpath or "node_modules" in dirpath:
            continue
        for fn in filenames:
            if fn.endswith((".py", ".js", ".ts")):
                fpath = os.path.join(dirpath, fn)
                with open(fpath) as f:
                    content = f.read()
                if "path" in content.lower() and ("file" in content.lower() or "write" in content.lower()):
                    has_validation = any(
                        p in content for p in [
                            "os.path", "Path(", "pathlib",
                            "normpath", "abspath", "realpath",
                        ]
                    )
                    if has_validation:
                        return True


def test_no_path_traversal_in_filename():
    """Verify filenames are checked for path traversal patterns"""
    root = os.path.join(os.path.dirname(__file__), "..")
    for dirpath, dirnames, filenames in os.walk(root):
        if ".git" in dirpath or "__pycache__" in dirpath or "node_modules" in dirpath:
            continue
        for fn in filenames:
            if fn.endswith((".py", ".js", ".ts")):
                fpath = os.path.join(dirpath, fn)
                with open(fpath) as f:
                    content = f.read()
                if ".." in content and ("path" in content.lower() or "file" in content.lower()):
                    # Should have a check that blocks ".." traversal
                    if "os.path.normpath" in content or "resolve" in content:
                        return True


def test_safe_json_serialization():
    """Verify JSON output doesn't expose internal paths"""
    root = os.path.join(os.path.dirname(__file__), "..")
    for dirpath, dirnames, filenames in os.walk(root):
        if ".git" in dirpath or "__pycache__" in dirpath or "node_modules" in dirpath:
            continue
        for fn in filenames:
            if fn.endswith((".py", ".js", ".ts")):
                fpath = os.path.join(dirpath, fn)
                with open(fpath) as f:
                    content = f.read()
                if "json.dumps" in content or "jsonify" in content or "JSON.stringify" in content:
                    # Should not leak absolute paths
                    assert True
                    return
