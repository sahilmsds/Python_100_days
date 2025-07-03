PLACEHOLDER = "[name]"
with open("D:\\100 days bootcamp\\Day24\\Mail Merge Project Start\\Input\\Names\\invited_names.txt") as names_file:
    names = names_file.readlines()

with open("D:\\100 days bootcamp\Day24\\Mail Merge Project Start\Input\\Letters\\starting_letter.txt") as letter_file:
    contents = letter_file.read()
    for name in names:
        stripped_name = name.strip()
        new_letter = contents.replace(PLACEHOLDER, stripped_name)
        with open(f"D://100 days bootcamp//Day24//Mail Merge Project Start//Output//ReadyToSend//letter_for_{stripped_name}.txt", 'w') as final_letter:
            final_letter.write(new_letter)
        