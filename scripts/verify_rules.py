import os

def test_rule_file_exists():
    rule_path = os.path.abspath(".agent/rules/windows-powershell-encoding.md")
    assert os.path.exists(rule_path), f"Rule file {rule_path} does not exist"

def test_rule_content():
    rule_path = os.path.abspath(".agent/rules/windows-powershell-encoding.md")
    with open(rule_path, "r", encoding="utf-8") as f:
        content = f.read()
    assert "# Windows PowerShell 编码规范" in content
    assert "$OutputEncoding = [Console]::OutputEncoding = [System.Text.Encoding]::UTF8;" in content

if __name__ == "__main__":
    try:
        test_rule_file_exists()
        test_rule_content()
        print("TDD Verification: PASS")
    except Exception as e:
        print(f"TDD Verification: FAIL - {e}")
        exit(1)
