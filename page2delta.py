prev_page_addr = None

with open("page.txt", "r") as f_in, open("delta.txt", "w") as f_out:
    for line in f_in:
        print("running\n")
        elements = line.split()
        pc = int(elements[0])
        page_addr = int(elements[1])
        if prev_page_addr is not None:
            delta = (page_addr - prev_page_addr)
            f_out.write(f"{(pc)} {delta}\n")
        else:
            f_out.write(f"{(pc)} {0}\n")

        prev_page_addr = page_addr
