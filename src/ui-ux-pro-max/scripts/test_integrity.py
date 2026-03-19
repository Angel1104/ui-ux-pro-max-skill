#!/usr/bin/env python3
"""
Data integrity tests for UI/UX Pro Max CSV databases.
Run: python3 src/ui-ux-pro-max/scripts/test_integrity.py
"""
import csv
import sys
from pathlib import Path

DATA_DIR = Path(__file__).parent.parent / "data"
PASS = "\033[92m✓\033[0m"
FAIL = "\033[91m✗\033[0m"

errors = []
total = 0


def check(condition, message):
    global total
    total += 1
    if condition:
        print(f"  {PASS} {message}")
    else:
        print(f"  {FAIL} {message}")
        errors.append(message)


def load(filename):
    path = DATA_DIR / filename
    if not path.exists():
        return None, f"{filename} not found"
    with open(path, encoding="utf-8") as f:
        return list(csv.DictReader(f)), None


# ── Required columns per file ──────────────────────────────────────────────────
REQUIRED_COLS = {
    "products.csv":     ["Product Type", "Keywords", "Primary Style Recommendation"],
    "styles.csv":       ["Style Category", "Keywords", "Best For"],
    "colors.csv":       ["Product Type", "Primary", "Background", "Foreground"],
    "typography.csv":   ["Font Pairing Name", "Heading Font", "Body Font", "Google Fonts URL"],
    "ux-guidelines.csv":["Category", "Issue", "Description", "Do", "Don't"],
    "charts.csv":       ["Data Type", "Best Chart Type", "When to Use"],
    "landing.csv":      ["Pattern Name", "Section Order"],
    "ui-reasoning.csv": ["UI_Category", "Recommended_Pattern", "Style_Priority", "Anti_Patterns"],
    "components.csv":   ["Component", "Category"],
}

STACK_REQUIRED = ["Category", "Guideline", "Description", "Do", "Don't", "Severity"]
STACKS = ["react.csv", "nextjs.csv", "vue.csv", "svelte.csv", "flutter.csv", "swiftui.csv", "react-native.csv"]


def test_required_columns():
    print("\n── Required columns ──────────────────────────────────────────")
    for filename, required in REQUIRED_COLS.items():
        rows, err = load(filename)
        if err:
            check(False, f"{filename}: {err}")
            continue
        check(len(rows) > 0, f"{filename}: has rows ({len(rows)})")
        if rows:
            for col in required:
                check(col in rows[0], f"{filename}: has column '{col}'")


def test_no_empty_critical_fields():
    print("\n── No empty critical fields ──────────────────────────────────")
    critical = {
        "products.csv": "Product Type",
        "styles.csv": "Style Category",
        "colors.csv": "Product Type",
        "typography.csv": "Font Pairing Name",
        "ui-reasoning.csv": "UI_Category",
    }
    for filename, col in critical.items():
        rows, err = load(filename)
        if err:
            check(False, f"{filename}: {err}")
            continue
        empty = [i + 2 for i, r in enumerate(rows) if not r.get(col, "").strip()]
        check(len(empty) == 0, f"{filename}: no empty '{col}' (empty rows: {empty[:5] or 'none'})")


def test_stack_files():
    print("\n── Stack CSV files ───────────────────────────────────────────")
    for stack_file in STACKS:
        path = DATA_DIR / "stacks" / stack_file
        check(path.exists(), f"stacks/{stack_file}: exists")
        if not path.exists():
            continue
        with open(path, encoding="utf-8") as f:
            rows = list(csv.DictReader(f))
        check(len(rows) >= 10, f"stacks/{stack_file}: has ≥10 rows ({len(rows)} found)")
        if rows:
            for col in STACK_REQUIRED:
                check(col in rows[0], f"stacks/{stack_file}: has column '{col}'")
            severity_values = {"Critical", "High", "Medium", "Low"}
            bad_severity = [r["Severity"] for r in rows if r.get("Severity", "") not in severity_values]
            check(len(bad_severity) == 0, f"stacks/{stack_file}: valid Severity values (invalid: {bad_severity[:3] or 'none'})")


def test_no_draft_files():
    print("\n── No zombie/draft files ─────────────────────────────────────")
    check(not (DATA_DIR / "draft.csv").exists(), "draft.csv is deleted")


def test_color_tokens():
    print("\n── Color token completeness ──────────────────────────────────")
    rows, err = load("colors.csv")
    if err:
        check(False, f"colors.csv: {err}")
        return
    token_cols = ["Primary", "Background", "Foreground", "Card", "Border"]
    for col in token_cols:
        empty = [i + 2 for i, r in enumerate(rows) if not r.get(col, "").strip()]
        check(len(empty) == 0, f"colors.csv: no empty '{col}' (empty rows: {empty[:5] or 'none'})")


def test_typography_urls():
    print("\n── Typography Google Fonts URLs ──────────────────────────────")
    rows, err = load("typography.csv")
    if err:
        check(False, f"typography.csv: {err}")
        return
    missing_url = [r.get("Font Pairing Name", f"row {i+2}") for i, r in enumerate(rows)
                   if not r.get("Google Fonts URL", "").strip()]
    check(len(missing_url) == 0, f"typography.csv: all pairings have Google Fonts URL (missing: {missing_url[:3] or 'none'})")


# ── Run ────────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    print("UI/UX Pro Max — Data Integrity Tests")
    print("=" * 60)

    test_required_columns()
    test_no_empty_critical_fields()
    test_stack_files()
    test_no_draft_files()
    test_color_tokens()
    test_typography_urls()

    print("\n" + "=" * 60)
    passed = total - len(errors)
    print(f"Results: {passed}/{total} passed")

    if errors:
        print(f"\nFailed ({len(errors)}):")
        for e in errors:
            print(f"  {FAIL} {e}")
        sys.exit(1)
    else:
        print(f"{PASS} All checks passed")
        sys.exit(0)
