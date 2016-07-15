from requests_futures.sessions import FuturesSession
import json

def gcompare(*queries):
    session = FuturesSession()
    results = []
    for query in queries:
        results.append(session.get('http://ajax.googleapis.com/ajax/services/search/web?v=1.0&q="{}"'.format(query)))
    results = [json.loads(r.result().text) for r in results]
    for result in results:
        if result["responseStatus"] == 403:
            print("API limits reached")
            exit(1)
    arity_sum = 0
    arities = []
    for res in results:
        if "estimatedResultCount" in res["responseData"]["cursor"]:
            arity = int(res["responseData"]["cursor"]["estimatedResultCount"])
            arities.append(arity)
            arity_sum += arity
        else:
            arities.append(0)

    ratios = [ar / float(arity_sum) for ar in arities]
    for (query, ratio, arity) in zip(queries, ratios, arities):
        print("{} {:4.3f}: {}".format(query, ratio, int(ratio * 50) * "#"))

def main():
    import sys
    arguments = sys.argv[1:]
    if len(arguments) >= 2:
        gcompare(*arguments)
    else:
        print("usage: gcompare <phrase1> <phrase2>")

if __name__ == '__main__':
    main()
