# writingtools

A set of tools that are useful when writing.
##Install

`pip install -e git+https://wafle@github.com/wafle/writingtools.git#egg=writingtools`

## gcompare

Compare the popularity of 2 phrases based on the number of result returned for their queries by a Google search:
```
$ gcompare "compare the popularity" "get the popularity"
"compare the popularity" 0.887: ############################################
"get the popularity" 0.113: #####
```

## synonyms

```
$ synonym popularity
1 : acclaim, acceptance, reputation, demand, following, fame
2 : adoration, fashion, favor, regard, prevalence, currency, renown, esteem, approval, repute, idolization, heyday, vogue, universality
3 : fashionableness, lionization
```

