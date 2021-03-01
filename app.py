from qtrade import Questrade

qtrade = Questrade (access_code='comjxj3dhaAICLUBhLIHV5mubYf2vvev0')
id = qtrade.get_account_id()
positions = qtrade.get_account_positions(id)
print(positions)