class Paper:
    """Paper used for printing."""
    def __init__(self, paper_format: str):
        self.paper_format = paper_format


class Printer:
    """Printer for printing papers."""
    def __init__(self, paper_tray_size):
        self.paper_tray_size = paper_tray_size
        self.papers = []  # leave this

    def add_paper(self, paper: Paper) -> bool:
        paper_formats = []
        for i in self.papers:
            if i.paper_format not in paper_formats:
                paper_formats += [i.paper_format]
        if len(self.papers) >= self.paper_tray_size:
            return(False)
        elif len(self.papers) == 0:
            self.papers += [paper]
            return(True)
        elif((self.papers[-1].paper_format == paper.paper_format) or (paper.paper_format not in paper_formats)):
            self.papers += [paper]
            return(True)
        else:
            return(False)

    def print(self, paper_format: str, pages: int):
        printed_pages = []
        for i in self.papers:
            if i.paper_format == paper_format and len(printed_pages) < pages:
                printed_pages += [i]
        for y in range(len(printed_pages)):
            self.papers.remove(printed_pages[y])
        return(printed_pages)

paber1 = Paper("A4")
paber2 = Paper("A3")
paber3 = Paper("A4")
paber4 = Paper("A3")
printer = Printer(3)
print(printer.add_paper(paber1))
print(printer.add_paper(paber1))
print(printer.add_paper(paber2))
print(printer.add_paper(paber1))
print(printer.add_paper(paber1))
print(printer.papers)
print(printer.print("A4", 3))
print(printer.papers)