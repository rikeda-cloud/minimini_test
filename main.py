import sys
from presentation_layer.minimini_test import Option
sys.path.append("../business_logic_layer")
sys.path.append("../persistence_layer")


def main():
    option = Option()
    option.test_loop()


if __name__ == '__main__':
    main()
