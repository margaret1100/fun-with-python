
import itertools
import numpy as np

#listing of the boy and girl cast members

boys = ['Malcolm', 'Keith', 'Joe', 'Michael', 'Ethan', 'Clint', 'Shad', 
'Tyler', 'Dimitri', 'Kareem', 'Anthony',]

girls = ['Nurys', 'Alexis', 'Zoe', 'Keyana', 'Jada', 'Uche', 'Audrey',
'Nicole', 'Diandre', 'Alivia', 'Geles']

#How the boys and girls were matched in each ceremony
ceremony_1 = ['Nurys', 'Alexis', 'Zoe', 'Keyana', 'Jada', 'Uche', 'Audrey', 
'Nicole','Diandre', 'Alivia', 'Geles']

ceremony_2 = ['Nurys', 'Alexis', 'Audrey', 'Keyana', 'Jada', 'Uche', 'Geles',
'Zoe', 'Nicole', 'Alivia', 'Diandre']

ceremony_3 = ['Geles', 'Diandre', 'Zoe', 'Audrey', 'Alexis', 'Uche', 'Keyana',
'Nicole', 'Nurys', 'Alivia', 'Jada']

ceremony_4 = ['Alivia', 'Nurys', 'Zoe', 'Geles', 'Nicole', 'Uche', 'Audrey',
'Jada', 'Alexis', 'Diandre', 'Keyana']

ceremony_5 = ['Diandre', 'Alexis', 'Zoe', 'Nurys', 'Geles', 'Jada', 'Audrey',
'Keyana', 'Uche', 'Alivia', 'Nicole']

ceremony_6 = ['Alivia', 'Zoe', 'Alexis', 'Uche', 'Jada', 'Geles', 'Audrey',
'Nicole', 'Diandre', 'Nurys', 'Keyana'] 

ceremony_7 = ['Alexis', 'Jada', 'Uche', 'Audrey', 'Zoe', 'Geles', 'Alivia',
'Nicole', 'Diandre', 'Nurys', 'Keyana'] 

ceremony_8 = ['Uche', 'Audrey', 'Jada', 'Keyana', 'Alexis', 'Geles', 'Zoe',
'Nicole', 'Diandre', 'Nurys', 'Alivia']

all_combinations = list(itertools.permutations(girls))

# list of matches
no_match_removed = list()

# Checks each set of combinations on the number of confirmed matches 
# and removes the combinations that don't match the number of confirmed matches.
for combo in all_combinations:
	if (combo[0] == 'Nurys' or combo[1] in ('Alivia', 'Alexis') or 
		combo[3] == 'Audrey' or combo[4] == 'Keyana' or 
		combo[5] == 'Uche' or combo[8] == 'Nicole' or combo[10] == 'Geles'):
		continue
	elif sum(np.array(combo) == np.array(ceremony_1)) != 3:
		continue
	elif sum(np.array(combo) == np.array(ceremony_2)) != 1:
		continue 
	elif sum(np.array(combo) == np.array(ceremony_3)) != 2:
		continue 
	elif sum(np.array(combo) == np.array(ceremony_4)) != 3:
		continue 
	elif sum(np.array(combo) == np.array(ceremony_5)) != 1:
		continue 
	elif sum(np.array(combo) == np.array(ceremony_6)) != 4:
		continue 
	elif sum(np.array(combo) == np.array(ceremony_7)) != 5:
		continue 
	elif sum(np.array(combo) == np.array(ceremony_8)) != 3:
		continue 
	else:
		no_match_removed.append(combo)

print(no_match_removed)



# Notes on efficacy
# No match removed half of the results 18M
# Ceremony 1 brought combos down to 400K
# Ceremony 2 brought combos down to 118K




																																																																																																																																	
