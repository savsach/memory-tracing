def convert_address_to_page(memory_address):
    page_number = memory_address  & ~((1<<12) -1)
    print("Converting\n")
    return page_number

# read input file
with open("pinatrace.out", "r") as file,open("page.txt", "w") as out:
  for line in file:
    elements = line.split()
    if len(elements) == 3:
        program_counter = int(elements[0].replace(':', ''), 16)
        memory_address = int(elements[2], 16)
        page_number = convert_address_to_page(memory_address)
        out.write(str(program_counter) + " " + str(page_number)+ '\n')

