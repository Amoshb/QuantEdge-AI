from dotenv import dotenv_values
import MetaTrader5 as mt5


class MT5Connector:
    def __init__(self):
        config = dotenv_values(".env")
        self.account = config['ACCOUNT']
        self.password = config['PASSWORD']
        self.server = config['SERVER']
    
    def connect(self):
        if not mt5.initialize(login=int(self.account), 
                              password=self.password, 
                              server=self.server):
            print("initialize() failed, error code =", mt5.last_error())
            return False
        print("MT5 initialized successfully")
        return True
    
    def disconnect(self):
        mt5.shutdown()


def main():
    connector = MT5Connector()
    connector.connect()
