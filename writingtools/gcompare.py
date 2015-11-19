from requests_futures.sessions import FuturesSession
import json

def gcompare(query1, query2):
    session = FuturesSession()
    query1 = '"' + query1 + '"'
    query2 = '"' + query2 + '"'
    term1 = session.get("http://ajax.googleapis.com/ajax/services/search/web?v=1.0&q={}".format(query1))
    term2 = session.get("http://ajax.googleapis.com/ajax/services/search/web?v=1.0&q={}".format(query2))

    term1_json = json.loads(term1.result().text)
    term2_json = json.loads(term2.result().text)

    if term1_json["responseStatus"] == 403 or term2_json["responseStatus"] == 403:
        print("API limits reached")
        exit(1)

    term1_arity = int(term1_json["responseData"]["cursor"]["estimatedResultCount"])
    term2_arity = int(term2_json["responseData"]["cursor"]["estimatedResultCount"])

    sum = term1_arity + term2_arity
    term1_percent = term1_arity / float(sum)
    term2_percent = term2_arity / float(sum)

    print("{} {:4.3f}: {}".format(query1, term1_percent, int(term1_percent * 50) * "#"))
    print("{} {:4.3f}: {}".format(query2, term2_percent, int(term2_percent * 50) * "#"))

def main():
    import sys
    arguments = sys.argv[1:]
    if len(arguments) == 2:
        gcompare(arguments[0], arguments[1])
    else:
        print("usage: gcompare <phrase1> <phrase2>")

if __name__ == '__main__':
    main()