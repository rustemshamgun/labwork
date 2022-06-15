def search_substr(subst, st):

if subst.lower() in st.lower():

return 'Контакт бар!'

else:

return 'Кері!'
# Тесты

print(search_substr('Кол', 'коЛокОл'))

print(search_substr('Колобок', 'колобоК'))

print(search_substr('Кол', 'Плов'))