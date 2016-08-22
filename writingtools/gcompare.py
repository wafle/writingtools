from requests_futures.sessions import FuturesSession
import json

def gcompare(*queries):
    session = FuturesSession()
    results = []
    for query in queries:
        results.append(session.get('https://www.googleapis.com/customsearch/v1?key=AIzaSyA81rdeOh9QiSbvOG4xEcTvK-jZBXl_HMc&cx=008639277777108339676:gt1rhznvzgm&q="{}"'.format(query)))
    results = [json.loads(r.result().text) for r in results]
    arity_sum = 0
    arities = []
    for res in results:
        if "error" in res:
            print(res["error"]["errors"][0]["reason"])
            exit(1)
        arity = int(res["queries"]["request"][0]["totalResults"])
        arities.append(arity)
        arity_sum += arity

    ratios = [ar / float(arity_sum) for ar in arities]
    for (query, ratio, arity) in zip(queries, ratios, arities):
        print("{} {:4.3f}% ({}): {}".format(query, ratio * 100, arity, int(ratio * 50) * "#"))

def main():
    import sys
    arguments = sys.argv[1:]
    if len(arguments) >= 2:
        gcompare(*arguments)
    else:
        print("usage: gcompare <phrase1> <phrase2>")

if __name__ == '__main__':
    main()
