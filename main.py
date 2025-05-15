import pytest
import sys

def run_crm_tests():
    pytest.main(["tests/crm", "-v", "--tb=short"])

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "crm":
        run_crm_tests()
    else:
        print("Usage: python main.py crm")
