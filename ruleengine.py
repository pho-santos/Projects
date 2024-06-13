#you can use to filter objects by a rule
#commands filter(iterable objects, return which the rule matches and filter returns a single object if true or false)
import rule_engine

beto_verse = [
    {
        'name' : 'betomen',
        'betoverso' : 'heroes',
        'likes dadinho?' : 'yes'
    },
    {   
        'name' : 'beto carteiro',
        'betoverso' : 'trabalhador',
        'likes dadinho?' : 'yes'
    },
    {   
        'name' : 'beto original',
        'betoverso' : 'terra 1',
        'likes dadinho?' : 'yes'
    },
]

rule = rule_engine.Rule('name =~~ beto')
rule.filter(beto_verse)
print(rule.filter)