import os
import argparse

def strBool(v):
    if isinstance(v, bool):
       return v
    if v.lower() in ('yes', 'true', 't', 'y', '1'):
        return True
    elif v.lower() in ('no', 'false', 'f', 'n', '0'):
        return False
    else:
        raise argparse.ArgumentTypeError('Expected a Boolean Value.')

def parse():
    parser = argparse.ArgumentParser(description = 'Command Line Interface for COVID-19 Prediction in India')
    parser.add_argument('-tr','--train', type = str, help = 'Argument taken for training model(s).', default = "none")
    parser.add_argument('-req','--install_requirements', type = strBool, help = 'Argument taken for installing requirements', default = False)
    parser.add_argument('-v','--visualize', type = strBool, help = 'Argument taken for visualizing metrics', default = False)
    parser.add_argument('-t','--test', type = strBool, help = 'Argument for testing with custom input',required = True)
    args = parser.parse_args()
    return args


if __name__ == "__main__":

    args = parse()

    if (args.train == 'cases'):
        os.system('python3 train_cases.py')

    if (args.train == 'deaths'):
        os.system('python3 train_deaths.py')

    if (args.train == 'all'):
        os.system('python3 train_cases.py')
        os.system('python3 train_deaths.py')

    if (args.install_requirements):
        os.system('sudo apt install python3-pip')
        os.system('pip3 install -r requirements.txt')

    if (args.visualize):
        os.system('python3 visualize.py')
    
    if (args.test):
        os.system('python3 test.py')
    



        