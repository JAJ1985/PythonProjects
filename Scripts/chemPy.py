import pubchempy as pcp

# Take name as input
chemical_name = input("Enter the chemical name: ")

try:
    # Search PubChem for the compound by its name
    compound = pcp.get_compounds(chemical_name, 'name')[0]

    # Display information about the compound.
    print(f'IUPAC Name" {compound.iupac_name}')
    print(f'Common Name: {compound.synonyms[0]}')
    print(f'Molecular Weight: {compound.molecular_weight}')
    print(f'Formula: {compound.molecular_formula}')

    # You can access more properties as needed.
except IndexError:
    print(f'No information found for {chemical_name}.')
