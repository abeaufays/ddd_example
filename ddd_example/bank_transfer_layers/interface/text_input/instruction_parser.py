from bank_transfer_layers.application import use_case


def parse(instruction:str) -> None:
    match instruction.split(" "):
            case ["+", account_id, initial_balance] if initial_balance.isnumeric():
                raise NotImplementedError
            case [from_account_id, to_account_id, amount] if amount.isnumeric():
                use_case.transfer_fund(from_account_id, to_account_id, int(amount))
            case _:
                raise ValueError(f"Invalid instruction: {instruction}")