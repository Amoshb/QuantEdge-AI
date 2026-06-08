import src.quantedge.data.mt5_connector as mt5_connector
import src.quantedge.data.fetch_symbol_data as fetch_symbol_data


def main():
    print("Hello from quantedge-ai!")
    mt5_connector.main()

    test_data = fetch_symbol_data.main()
    print(test_data)


if __name__ == "__main__":
    main()
