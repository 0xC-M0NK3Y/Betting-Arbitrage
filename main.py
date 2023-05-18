from analyzer.analyze import analyze_sport
import sys

def main():
    if len(sys.argv) != 2:
        print(f'Usage {sys.argv[0]} <sport>')
        exit()
    result = analyze_sport(sys.argv[1])

    for i in range(len(result)):
        print(result[i])

if __name__ == '__main__':
    main()