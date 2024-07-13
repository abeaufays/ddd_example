import pytest

from bank_transfer_layers.interface.text_input import instruction_parser


class TestInstructionParser:
    def test_create_account_not_implemented(self):
        with pytest.raises(NotImplementedError):
            instruction_parser.parse("+ A 100")

    def test_transfer_fund(self, mocker):
        patched_transfer_fund = mocker.patch("bank_transfer_layers.application.use_case.transfer_fund")
        instruction_parser.parse("A B 100")
        patched_transfer_fund.assert_called_once_with("A", "B", 100)
    
    def test_invalid_instruction(self):
        with pytest.raises(ValueError):
            instruction_parser.parse("A B C")
        
        with pytest.raises(ValueError):
            instruction_parser.parse("- B")
        
        with pytest.raises(ValueError):
            instruction_parser.parse("azerty")