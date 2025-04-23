import subprocess
import pytest

programa = "./programa1"

def run_validator(validator: str, credit_card: str) -> str:
    return subprocess.check_output([validator, credit_card]).decode('utf-8').strip()

def correct_output(company):
    return f"Valid {company} card"

@pytest.fixture
def executable():
    return programa
    
def test_visa_prefix(executable):
    expected_output = "Valid Visa card"
    obtained_output = run_validator(executable,"4000000000000000")
    assert expected_output == obtained_output, f"Expected '{expected_output}' but got '{obtained_output}'"

def test_visa_length(executable):
    expected_outputs = ["Valid Visa card","Invalid card number","Invalid card number","Valid Visa card"]
    inputs = [f"4{'0'*i}" for i in range(12,16)]
    obtained_outputs = [run_validator(executable,i) for i in inputs]
    for input, obtained_output, expected_output in zip(inputs,obtained_outputs,expected_outputs):
        assert expected_output == obtained_output, f"Card {input} should get {expected_output} but instead got '{obtained_output}'"

def test_mastercard_prefix(executable):
    expected_outputs = ["Invalid card number","Valid Mastercard card","Valid Mastercard card","Valid Mastercard card","Valid Mastercard card","Valid Mastercard card","Invalid card number"]
    inputs = [f"5{i}00000000000000" for i in range(0,7)]
    obtained_outputs = [run_validator(executable,i) for i in inputs]
    for input, obtained_output, expected_output in zip(inputs,obtained_outputs,expected_outputs):
        assert expected_output == obtained_output, f"Card {input} should get {expected_output} but instead got '{obtained_output}'"

def test_mastercard_length(executable):
    expected_outputs = ["Invalid card number","Valid Mastercard card","Invalid card number"]
    inputs = [f"53{'0'*i}" for i in range(13,16)]
    obtained_outputs = [run_validator(executable,i) for i in inputs]
    for input, obtained_output, expected_output in zip(inputs,obtained_outputs,expected_outputs):
        assert expected_output == obtained_output, f"Card {input} should get {expected_output} but instead got '{obtained_output}'"

def test_american_express_prefix(executable):
    expected_outputs = ["Invalid card number","Valid American Express card","Invalid card number","Invalid card number","Valid American Express card","Invalid card number"]
    inputs = [f"3{i}0000000000000" for i in range(3,9)]
    obtained_outputs = [run_validator(executable,i) for i in inputs]
    for input, obtained_output, expected_output in zip(inputs,obtained_outputs,expected_outputs):
        assert expected_output == obtained_output, f"Card {input} should get {expected_output} but instead got '{obtained_output}'"

def test_american_express_length(executable):
    expected_outputs = ["Invalid card number","Valid American Express card","Invalid card number",]
    inputs = [f"34{'0'*i}" for i in range(12,15)]
    obtained_outputs = [run_validator(executable,i) for i in inputs]
    for input, obtained_output, expected_output in zip(inputs,obtained_outputs,expected_outputs):
        assert expected_output == obtained_output, f"Card {input} should get {expected_output} but instead got '{obtained_output}'"
