from database_share_transactions import computeHistorical

try:
    name_client, equity_name, date_rand, type_trans, cost, numbers, total = computeHistorical()
except:
    print('locha')
