import camelcase as camelcase
from tenseflow import change_tense

text = "md golam kibria"
largeFirstLatter = camelcase.CamelCase().hump(text)  # for large first latter
print(largeFirstLatter)
