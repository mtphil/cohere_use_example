import argparse
import cohere
import os


def main():
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument("-p", "--prompt", help="your prompt")
    arg_parser.add_argument("-t", "--max_tokens", help="max tokens")
    arg_parser.add_argument("-t", "--temperature", help="temperature")
    arg_parser.add_argument("-f", "--frequency_penalty", help="frequency penalty")
    arg_parser.add_argument("-m", "--model", help="model")

    args = arg_parser.parse_args()

    co = cohere.Client(os.getenv('COHERE_API_TOKEN'))

    response = co.generate(
        model=args.model,
        prompt=args.prompt,
        max_tokens=args.max_tokens,
        temperature=args.temperature,
        frequency_penalty=args.freqeuncy_penalty)

    startup_idea = response.generations[0].text

    print(startup_idea)


if __name__ == '__main__':
    main()
