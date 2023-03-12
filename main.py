import argparse
import cohere
import os


def main():
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument("-p", "--prompt", help="your prompt")

    args = arg_parser.parse_args()

    co = cohere.Client(os.getenv('COHERE_API_TOKEN'))

    response = co.generate(
        model='xlarge',
        prompt=args.prompt,
        max_tokens=1000,
        temperature=1.5,
        frequency_penalty=0.25)

    startup_idea = response.generations[0].text

    print(startup_idea)


if __name__ == '__main__':
    main()
