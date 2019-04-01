import requests
import json
# pip install requests

BASE_URL = 'https://jsonplaceholder.typicode.com'
ENDPOINT = 'posts'


def get_recent_todos(number_to_retrieve):
    url = '{}/{}/{}'
    return json.dumps([requests.get(url.format(BASE_URL, ENDPOINT, i)).json() for i in range(number_to_retrieve)])


def create_todo(title, body, user_id):
    url = '{}/{}'
    r = requests.post(url.format(BASE_URL, ENDPOINT, body=dict(title=title, body=body,
                                                               userId=user_id), headers={"Content-type": "application/json; charset=UTF-8"}))
    return r


def delete_todo(post_id):
    url = '{}/{}/{}'
    return requests.delete(url.format(BASE_URL, ENDPOINT, post_id)).json()


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("-n", "--number", help="Number of posts to retrieve from {}".format(BASE_URL),
                        type=int)

    parser.add_argument(
        "-t", "--title", help="Title of a post to insert", type=str)
    parser.add_argument(
        "-b", "--body", help="Title of a post to insert", type=str)
    parser.add_argument(
        "-i", "--id", help="Title of a post to insert", type=int)

    parser.add_argument(
        "-d", "--delete", help="Delete a post by passing an id", type=int)

    args = parser.parse_args()

    if args.number:
        print('task 1:\n')
        print([doc for doc in json.loads(get_recent_todos(args.number)) if doc], '\n')

    if all([args.title, args.body, args.id]):
        print('task 2:\n')
        print(create_todo(args.title, args.body, args.id), '\n')
    else:
        if any([args.title, args.body, args.id]):
            print('forgot something required to create a new post.\n Things required are --title, --body, --id. \nPlease Try Again.')

    if args.delete:
        print('task 3:\n')
        r = delete_todo(args.delete)
        print(r)
