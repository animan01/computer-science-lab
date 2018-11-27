import requests
from bs4 import BeautifulSoup


def tokenize(book):
    if book is not None:
        words = book.lower().split()
        return words
    else:
        return None


def count_word(tokens, token):
    count = 0

    for element in tokens:
        # Remove Punctuation
        word = element.replace(",", "")
        word = word.replace(".", "")

        # Found Word?
        if word == token:
            count += 1
    return count


def news():
    # the target we want to open
    url = 'https://tsn.ua/'

    # open with GET method
    resp = requests.get(url)

    # http_respone 200 means OK status
    if resp.status_code == 200:
        print('Successfully opened the web page')
        print('The news are as follow :-\n')

        # we need a parser,Python built-in HTML parser is enough .
        soup = BeautifulSoup(resp.text, 'html.parser')

        # l is the list which contains all the text i.e news
        body = soup.findAll('h4')

        # links = body.findAll('a')

        # print(body)

        content = ''

        # now we want to print only the text part of the anchor.
        # find all the elements of a, i.e anchor
        for i in body:
            # print(i.text)
            content += i.text

        # print(content)

        book = content

        # Tokenize the Book
        words = tokenize(book)

        # print(words)

        for word in words:
            frequency = count_word(words, word)
            if (frequency >= 10 & len(word) < 2):
                print('Word: [' + word + '] Frequency: ' + str(frequency))


    else:
        print("Error")


news()

# print(page.content)

# html_doc = '<html><body class="ss">Test</body>'


# html_page = urllib2.urlopen("https://www.nytimes.com/")

# soup = BeautifulSoup(html_doc, 'html.parser')

# print(soup.contents)



